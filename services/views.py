from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Category, ServicePost, Review, NewsCategory, News
from blog.models import BlogPost
from users.models import Testimonial

def home(request):
    context = {
    "newscat":NewsCategory.objects.all()[:4],
    "news_obj":News.objects.all()[:4],
    "jobposts":ServicePost.objects.all(),
    "reviews":Review.objects.all(),
    }
    x = settings.DEVELOPMENT
    if not request.user.is_authenticated and x == True:
        template = 'services/maintenance.html'
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
            template = 'services/logged-in-home.html'
        else:
            template = 'services/logged-out-home.html'
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
            #------------------sign in form activation---------------------
            elif request.POST.get('form-type') == "signin-form":
                user = None
                try:
                    username = request.POST.get('signin-name')
                    password = request.POST.get('signin-password')
                    # user_check = User.object.get(username = username)
                    user = authenticate(username=username, password=password)

                    if user is not None:
                        login(request, user)
                        context['user'] = username
                        return redirect('/')
                    else:
                        messages.warning(request, f"User does not exist!")
                except (Exception, User.DoesNotExist) as e:
                    messages.warning(request, f"Error! {e}")

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
#-------------------------dashboard view---------------------------------------
@login_required
def dashboard(request):
    template="services/dashboard.html"

    context = {
    # "":
    # "":
    }
    return render(request, template, context)
#-------------------------profile view---------------------------------------
@login_required
def profile(request):
    template="services/profile.html"

    context = {
    # "":
    # "":
    }
    return render(request, template, context)
