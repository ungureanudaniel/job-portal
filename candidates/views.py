from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Skill, AppliedJobs, SavedJobs, AvailableCountry
from recruiters.models import Job, Applicant, Selected, JobCategory
from users.models import About, BlogPost, Testimonial
from .forms import ProfileUpdateForm, NewSkillForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.template.defaulttags import register


def maintenance(request):
    template = 'candidates/maintenance.html'

    context = {}
    return render(request, template, context)


def get_category_count():
    cats = Category.objects.all().annotate(num_posts = Count('postcategory'))
    return cats

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]
#--------------------------------home view-------------------------------------
def home(request):
    if request.user.is_authenticated:
        template = 'candidates/logged-in-home.html'
    else:
        template = 'candidates/logged-out-home.html'
    countries_list = AvailableCountry.objects.all()
    jobs_cat = JobCategory.objects.all()[:8]
    featured_jobs = Job.objects.all()[:8]
    countries = featured_jobs.values_list("country")
    posts = BlogPost.objects.all().order_by("created_date")[:3]
    reviews = Testimonial.objects.all()
    print(countries)

    context = {
        'home_page': "active",
        "featured_jobs": featured_jobs,
        'countries_list': countries_list,
        "jobs_cat": jobs_cat,
        "countries": countries,
        "posts": posts,
        "reviews": reviews,
    }
    return render(request, template, context)

#-------------------------------CATEGORY VIEW-----------------------------------
def category(request, cat_slug):
    template_name = 'candidates/category.html'
    category = get_object_or_404(JobCategory, slug=cat_slug)
    jobsbycategory = Job.objects.filter(category=category)
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
def my_post_list(request):
    template = 'candidates/my_post_list.html'
    countries_list = AvailableCountry.objects.all()
    query_keywords = request.GET.get('keyword')
    query_location = request.GET.get('loc')
    query_cat = request.GET.get('cat')
    object_list = []
    if(query_keywords == None):
        object_list = Job.objects.all()
    else:
        title_list = Job.objects.filter(title__icontains=query_keywords).order_by('-date_posted')
        skill_list = Job.objects.filter(skills_req__icontains=query_keywords).order_by('-date_posted')
        company_list = Job.objects.filter(company__icontains=query_keywords).order_by('-date_posted')
        job_type_list = Job.objects.filter(job_type__icontains=query_keywords).order_by('-date_posted')
        Job.objects.filter(category__icontains=query_keywords).order_by('-date_posted')
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
        locat = Job.objects.all()
    else:
        locat = Job.objects.filter(
            country__icontains=query_location).order_by('-date_posted')
    if(query_cat==None):
        cat = Job.objects.all()
    else:
        query_cat = Job.objects.filter(category__icontains=query_cat).order_by('-date_posted')

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

#----------------------------job search list ----------------------------------
def job_search_list(request):
    template = 'candidates/job_search_list.html'
    countries_list = AvailableCountry.objects.all()
    query_keywords = request.GET.get('keyword')
    query_location = request.GET.get('loc')
    query_cat = request.GET.get('cat')
    object_list = []
    if(query_keywords == None):
        object_list = Job.objects.all()
    else:
        title_list = Job.objects.filter(title__icontains=query_keywords).order_by('-date_posted')
        skill_list = Job.objects.filter(skills_req__icontains=query_keywords).order_by('-date_posted')
        company_list = Job.objects.filter(company__icontains=query_keywords).order_by('-date_posted')
        job_type_list = Job.objects.filter(job_type__icontains=query_keywords).order_by('-date_posted')
        Job.objects.filter(category__icontains=query_keywords).order_by('-date_posted')
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
        locat = Job.objects.all()
    else:
        locat = Job.objects.filter(
            country__icontains=query_location).order_by('-date_posted')
    if(query_cat==None):
        cat = Job.objects.all()
    else:
        query_cat = Job.objects.filter(category__icontains=query_cat).order_by('-date_posted')

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
    # nr_comments = Job.objects.values('comments').annotate(Count('comments'))
    # count = nr_comments.values('comments', 'comments__count')
    #end nr of comments
    #model = Post
    job = get_object_or_404(Job, pk=pk)
    jobs = Job.objects.filter(pk=pk)
    # form = CommentForm(request.POST or None)
    job_object = Job.objects.get(pk=job.pk)
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
#     job = get_object_or_404(Job, slug=slug)
#     apply_button = 0
#     save_button = 0
#     profile = Profile.objects.filter(user=request.user).first()
#     if AppliedJobs.objects.filter(user=request.user).filter(job=job).exists():
#         apply_button = 1
#     if SavedJobs.objects.filter(user=request.user).filter(job=job).exists():
#         save_button = 1
#     relevant_jobs = []
#     jobs1 = Job.objects.filter(
#         company__icontains=job.company).order_by('-date_posted')
#     jobs2 = Job.objects.filter(
#         job_type__icontains=job.job_type).order_by('-date_posted')
#     jobs3 = Job.objects.filter(
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
