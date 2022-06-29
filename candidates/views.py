from django.shortcuts import render, redirect, get_object_or_404
from .models import ServicePost, Profile, Skill, Category, SubCategory
from django.core.mail import send_mail, BadHeaderError
import random
from users.models import About, BlogPost, Testimonial
from .forms import ProfileUpdateForm, NewSkillForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.models import Users, Subscriber
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.template.defaulttags import register



#----------generate unique code for email subscription conf--------------------
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)
# def maintenance(request):
#     template = 'candidates/maintenance.html'
#     duplicate_message = ""
#     if request.method == "POST":
#         #---------------fetch the user input -----------------------------------
#
#         newsletter_email = request.POST.get('sub_email')
#         print(newsletter_email)
#         #--------------check if newsletter email exists already---------
#         if newsletter_email:
#             print(f"email ok")
#             try:
#                 duplicate = Subscriber.objects.get(email=newsletter_email)
#                 if duplicate:
#                     messages.warning(request, "This email already exists!")
#
#                     context = {
#
#                     }
#                     return render(request, template, context)
#             except Exception as e:
#                 print(e)
#                 #-----------------------SAVE IN DATABASE----------------
#                 sub = Subscriber(email=newsletter_email, conf_num=random_digits(), timestamp=datetime.datetime.now())
#                 sub.save()
#                 messages.success(request, "A confirmation link is on its way to your email inbox!")
#                 #---------------------send confirmation email settings------
#                 sub_subject = "Newsletter Dincolo Freelancers"
#                 from_email=settings.FROM_EMAIL
#                 sub_message = ''
#                 html_content='Thank you for subscribing to our newsletter!\
#                             Finalize the process by \
#                                 <a href="{}subscription_confirmation/?email={}&conf_num={}"> clicking this link \
#                                     </a>.'.format(request.build_absolute_uri(''), sub.email, sub.conf_num)
#                 try:
#                     send_mail(sub_subject, sub_message, from_email, [sub], html_message=html_content)
#                 except Exception as e:
#                     messages.error(request,f"Error is {e}")
#     context = {}
#     return render(request, template, context)


def get_category_count():
    cats = Category.objects.all().annotate(num_posts = Count('postcategory'))
    return cats

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]
#--------------------------------home view-------------------------------------
def home(request):
    context = {}
    x = settings.FROM_MAINTENANCE
    if not request.user.is_authenticated and x == True:
        template = 'candidates/maintenance.html'
        duplicate_message = ""
        if request.method == "POST":
            #---------------fetch the user input -----------------------------------

            newsletter_email = request.POST.get('sub_email')
            print(newsletter_email)
            #--------------check if newsletter email exists already---------
            if newsletter_email:
                print(f"email ok")
                try:
                    duplicate = Subscriber.objects.get(email=newsletter_email)
                    if duplicate:
                        messages.warning(request, "This email already exists!")

                        context = {

                        }
                        return render(request, template, context)
                except Exception as e:
                    print(e)
                    #-----------------------SAVE IN DATABASE----------------
                    sub = Subscriber(email=newsletter_email, conf_num=random_digits(), timestamp=datetime.datetime.now())
                    sub.save()
                    messages.success(request, "A confirmation link is on its way to your email inbox!")
                    #---------------------send confirmation email settings------
                    sub_subject = "Newsletter Dincolo Freelancers"
                    from_email=settings.FROM_EMAIL
                    sub_message = ''
                    html_content='Thank you for subscribing to our newsletter!\
                                Finalize the process by \
                                    <a href="{}subscription_confirmation/?email={}&conf_num={}"> clicking this link \
                                        </a>.'.format(request.build_absolute_uri(''), sub.email, sub.conf_num)
                    try:
                        send_mail(sub_subject, sub_message, from_email, [sub], html_message=html_content)
                    except Exception as e:
                        messages.error(request,f"Error is {e}")
            if request.POST.get('form-type') == "signin-form":
                user = None
                try:
                    username = request.POST.get('signin-name')
                    password = request.POST.get('signin-password')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        context['user'] = username
                        return redirect('/')
                except (Exception, ValueError) as e:
                    print(f"The error is {e}")
        context = {}
        return render(request, template, context)
    else:
        if request.user.is_authenticated:
            template = 'candidates/logged-in-home.html'
        else:
            template = 'candidates/logged-out-home.html'
        jobs_cat = Category.objects.all()[:8]
        featured_jobs = ServicePost.objects.all()[:8]
        posts = BlogPost.objects.all().order_by("created_date")[:3]
        reviews = Testimonial.objects.all()
        # form = CaptchaForm(request.POST)
        form = True
        if request.method=="POST":
            print(f"The form type is : {request.POST.get('form-type')}")
            if request.POST.get('form-type') == "signup-form":
                username = request.POST.get('signup-name')
                email = request.POST.get('signup-email')
                password = request.POST.get('signup-password')
                check = request.POST.get('password-check')
                checkbox = request.POST.get('checkbox')
                # print(username)
                # print(email)
                # print(check)
                # print(checkbox)
                first_name =""
                last_name=""
                phone=""
                gender=""
                birth=""
                img=""
                type =""
                if form == True:
                    if checkbox == "Agree":
                        if check != password:
                            messages.error(request, "Please check so that both passwords are identical.")
                            return redirect('.')
                        else:
                            try:
                                user_check = User.objects.get(username=username)
                                email_check = User.objects.get(email=email)
                                if user_check:
                                    messages.warning(request, "This user name already exists!")
                                    return redirect('/')
                                elif email_check:
                                    messages.error(request, "This user email address already exists!")
                                    return redirect('/')
                            except Exception as e:
                                print(e)
                                try:
                                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_active = False)
                                    new_users = Users.objects.create(user=user, email=email, phone=phone, gender=gender, birthdate = birth, image=img, type=type, conf_number=random_digits())
                                    conf_number=random_digits()
                                    user.save()
                                    new_users.save()
                                    #---------------------send confirmation email settings------
                                    conf_subject = "DINCOLO account confirmation"
                                    from_email=settings.FROM_EMAIL
                                    conf_message = ''
                                    html_content='Thank you for joining our job platform! You will not regret it.\
                                        To finalize the process please \
                                                <a href="{}registration_confirmation/?email={}&conf_number={}"> click this link \
                                                </a>.'.format(request.build_absolute_uri(''), new_users.email, new_users.conf_number)
                                    try:
                                        send_mail(conf_subject, conf_message, from_email, [user.email], html_message=html_content)
                                        context = {
                                                }

                                    except Exception as e:
                                        messages.error(request, e)
                                        return HttpResponse('Invalid header found.')
                                except Exception as e:
                                        messages.error(request, e)
                                        return redirect('/')

                    else:
                        messages.error(request, "Please check box to agree to our terms and conditions.")
                        return redirect('.')
            elif request.POST.get('form-type') == "signin-form":
                user = None
                try:
                    username = request.POST.get('signin-name')
                    password = request.POST.get('signin-password')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        context['user'] = username
                        return redirect('/')
                except (Exception, ValueError) as e:
                    print(f"The error is {e}")

            else:
                return render(request, "candidates/logged-out-home.html", {})

        data_keys = [
        'home_page',
        "featured_jobs",
        "jobs_cat",
        "posts",
        "reviews"
        ]
        data_val = [
        "active",
        featured_jobs,
        jobs_cat,
        posts,
        reviews
        ]
        combined = zip(data_keys,data_val)
        context.update(combined)
        return render(request, template, context)

#-------------------------------CATEGORY VIEW-----------------------------------
def category(request, cat_slug):
    template_name = 'candidates/category.html'
    category = get_object_or_404(JobCategory, slug=cat_slug)
    jobsbycategory = ServicePost.objects.filter(category=category)
    cat_menu = JobCategory.objects.all()
    context = {
        'cat_menu': cat_menu,
        'category': category,
        'jobsbycategory': jobsbycategory,
    }
    return render(request, template_name, context)
#-------------------------------ADD POST VIEW-----------------------------------
@login_required(login_url="/login/")
def add_post(request):
    template_name = 'obcinastanisoarei_app/add_post.html'
    author = request.user

    if request.method == 'POST':
        form = AddNewJobForm(request.POST, request.FILES or None)
        # print(form)
        if form.is_valid():
            try:
                # title = form.cleaned_data['title']
                # # slg = slugify(form.cleaned_data["title"])
                # cat = form.cleaned_data['category']
                # feat = form.cleaned_data['featured']
                # txt = form.cleaned_data['text']
                # img = request.FILES.get('image')
                # stat = form.cleaned_data['status']
                # newpost = BlogPost(author=request.user, text=txt, title=title, image=img, category=cat, featured = feat, status = stat)
                # newpost.save(commit=False)
                #
                # print(newpost.id)
                # tags = form.cleaned_data['tags']
                # print(tags)
                # for tag in tags:
                #     newpost.tags.add(tag)
                # newpost.save()
                newpost = form.save(commit=False)
                newpost.slug = slugify(newpost.title)
                newpost.save()
                return redirect("/blog_list")
                messages.success(request, _('Succes!'))
            except Exception as e:
                messages.error(request, _('Nereusit!') + str(e))
        else:
            messages.warning(request, _('Verificati datele introduse!'))
            form = AddNewPostForm()

    else:
        form = AddNewPostForm()
    context = {
        "form": form,
    }
    return render(request, template_name, context)

#----------------------------job search list ----------------------------------
def search_results(request):
    template = 'users/search_results.html'
    query_keywords = request.GET.get('keyword')
    # query_location = request.GET.get('loc')
    # query_cat = request.GET.get('cat')
    object_list = []
    if(query_keywords == None):
        object_list = ServicePost.objects.all()
    else:
        title_list = ServicePost.objects.filter(title__icontains=query_keywords).order_by('-date_posted')
        skill_list = ServicePost.objects.filter(skills_req__icontains=query_keywords).order_by('-date_posted')
        company_list = ServicePost.objects.filter(company__icontains=query_keywords).order_by('-date_posted')
        job_type_list = ServicePost.objects.filter(job_type__icontains=query_keywords).order_by('-date_posted')
        ServicePost.objects.filter(category__icontains=query_keywords).order_by('-date_posted')
        for i in title_list:
            object_list.append(i)
        for i in skill_list:
            if i not in object_list:
                object_list.append(i)
        for i in company_list:
            if i not in object_list:
                object_list.append(i)
        for i in job_type_list:
            if i not in object_list:
                object_list.append(i)
        for i in category_list:
            if i not in object_list:
                object_list.append(i)
    # if(query_location == None):
    #     locat = ServicePost.objects.all()
    # else:
    #     locat = ServicePost.objects.filter(
    #         country__icontains=query_location).order_by('-date_posted')
    # if(query_cat==None):
    #     cat = ServicePost.objects.all()
    # else:
    #     query_cat = ServicePost.objects.filter(category__icontains=query_cat).order_by('-date_posted')

    final_list = []
    for i in object_list:
        final_list.append(i)
    #     if i in locat:
    #
    paginator = Paginator(final_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj,
        'query_keywords': query_keywords,
    }
    return render(request, template, context)

#----------------------------job search list ----------------------------------
def job_search_list(request):
    template = 'candidates/job_search_list.html'
    query_keywords = request.GET.get('keyword')
    query_location = request.GET.get('loc')
    query_cat = request.GET.get('cat')
    object_list = []
    if(query_keywords == None):
        object_list = ServicePost.objects.all()
    else:
        title_list = ServicePost.objects.filter(title__icontains=query_keywords).order_by('-date_posted')
        skill_list = ServicePost.objects.filter(skills_req__icontains=query_keywords).order_by('-date_posted')
        company_list = ServicePost.objects.filter(company__icontains=query_keywords).order_by('-date_posted')
        job_type_list = ServicePost.objects.filter(job_type__icontains=query_keywords).order_by('-date_posted')
        ServicePost.objects.filter(category__icontains=query_keywords).order_by('-date_posted')
        for i in title_list:
            object_list.append(i)
        for i in skill_list:
            if i not in object_list:
                object_list.append(i)
        for i in company_list:
            if i not in object_list:
                object_list.append(i)
        for i in job_type_list:
            if i not in object_list:
                object_list.append(i)
        for i in category_list:
            if i not in object_list:
                object_list.append(i)
    if(query_location == None):
        locat = ServicePost.objects.all()
    else:
        locat = ServicePost.objects.filter(
            country__icontains=query_location).order_by('-date_posted')
    if(query_cat==None):
        cat = ServicePost.objects.all()
    else:
        query_cat = ServicePost.objects.filter(category__icontains=query_cat).order_by('-date_posted')

    final_list = []
    for i in object_list:
        if i in locat:
            final_list.append(i)
    paginator = Paginator(final_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj,
        'query_keywords': query_keywords,
        "countries_list": countries_list,
    }
    return render(request, template, context)

def job_details(request, pk):
    template_name = 'candidates/job_details.html'
    about_list = About.objects.all()[:1]
    cat_menu = JobCategory.objects.all()
    #count nr of comments
    # nr_comments = ServicePost.objects.values('comments').annotate(Count('comments'))
    # count = nr_comments.values('comments', 'comments__count')
    #end nr of comments
    #model = Post
    service = get_object_or_404(ServicePost, pk=pk)
    jobs = ServicePost.objects.filter(pk=pk)
    # form = CommentForm(request.POST or None)
    job_object = ServicePost.objects.get(pk=service.pk)
    # job_object.views_count = job_object.views_count + 1
    job_object.save()
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.instance.post = job
    #         form.save()
            #return redirect('post', kwargs={'pk':post.pk})
            # return redirect(reverse('home'))

    context = {
        'cat_menu': cat_menu,
        # 'count': count,
        'about_list': about_list,
        'jobs': jobs,
        # 'form': form,
    }
    return render(request, template_name, context)

#----------------------------JOB DETAIL VIEW-----------------------------------
# def job_details(request, slug):
#     template = 'candidates/job_details.html'
#     job = get_object_or_404(ServicePost, slug=slug)
#     apply_button = 0
#     save_button = 0
#     profile = Profile.objects.filter(user=request.user).first()
#     if AppliedJobs.objects.filter(user=request.user).filter(job=job).exists():
#         apply_button = 1
#     if SavedJobs.objects.filter(user=request.user).filter(job=job).exists():
#         save_button = 1
#     relevant_jobs = []
#     jobs1 = ServicePost.objects.filter(
#         company__icontains=job.company).order_by('-date_posted')
#     jobs2 = ServicePost.objects.filter(
#         job_type__icontains=job.job_type).order_by('-date_posted')
#     jobs3 = ServicePost.objects.filter(
#         title__icontains=job.title).order_by('-date_posted')
#     for i in jobs1:
#         if len(relevant_jobs) > 5:
#             break
#         if i not in relevant_jobs and i != job:
#             relevant_jobs.append(i)
#     for i in jobs2:
#         if len(relevant_jobs) > 5:
#             break
#         if i not in relevant_jobs and i != job:
#             relevant_jobs.append(i)
#     for i in jobs3:
#         if len(relevant_jobs) > 5:
#             break
#         if i not in relevant_jobs and i != job:
#             relevant_jobs.append(i)
#
#     context = {
#         'job': job,
#         'profile': profile,
#         'apply_button': apply_button,
#         'save_button': save_button,
#         'relevant_jobs': relevant_jobs,
#         'candidate_navbar': 1,
#         }
#     return render(request, template, context)

#--------------------------SAVED JOBS -----------------------------------------
@login_required
def saved_jobs(request):
    template = 'candidates/saved_jobs.html'
    jobs = SavedJobs.objects.filter(
        user=request.user).order_by('-date_posted')

    context = {
        'jobs': jobs,
        'candidate_navbar': 1,
        }
    return render(request, template, context)
#--------------------------CANDIDATE DASHBOARD ---------------------------------
def candidate_dashboard(request):
    template_name = 'users/employee.html'

    context = {
    }
    return render(request, template_name, context)
