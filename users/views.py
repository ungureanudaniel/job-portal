from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import CaptchaForm
from django.core.mail import send_mail, BadHeaderError
from .models import About, Users
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
import random

#---------------------------------LOGOUT VIEW-----------------------------------
def user_logout(request):
    try:
        logout(request)
    except (Exception, ValueError) as e:
        print(e)
    return redirect('/')

#-----------------------GENERATE RANDOM SUBSCRIBER ID--------------------------
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)
#-------------------------------REGSTER VIEW-----------------------------------
def register(request):
    # form = CaptchaForm(request.POST)
    form = True
    if request.method=="POST":
        username = request.POST.get('signup-name')
        email = request.POST.get('signup-email')
        password = request.POST.get('signup-password')
        check = request.POST.get('password-check')
        checkbox = request.POST.get('checkbox')
        print(username)
        print(email)
        print(check)
        print(checkbox)
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
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
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
                                    </a>.'.format(request.build_absolute_uri(''), user.email, new_users.conf_number)
                        try:
                            send_mail(conf_subject, conf_message, from_email, [user.email], html_message=html_content)
                            context = {
                                    }

                        except Exception as e:
                            return HttpResponse('Invalid header found.')
            else:
                messages.error(request, "Please check box to agree to our terms and conditions.")
                return redirect('.')
            return redirect('registration_confirmation')
        return render(request, "users/register.html", {'form':form})
    return render(request, 'users/register.html', {'form':form})
#-------------------------------REGISTER CONFIRMATION VIEW----------------------
@csrf_protect
def registration_conf_view(request):
    template = 'users/registration_conf.html'
    try:
        x = Company.objects.get(email=request.GET['emailaddress-register'])
        print(x.email)
        if x.conf_number == request.GET['conf_number']:
            try:
                x.confirmed = True
                x.save()
            except:
                messages.warning(request, "Error! Your email cannot be registered. Please contact us!")
            return render(request, template, {'email': x.email, 'action': 'confirmed'})
        else:
            return render(request, template, {'email': x.email, 'action': 'denied'})
    except:
        y = Candidate.objects.get(email=request.GET['email'])
        if y.conf_number == request.GET['conf_number']:
            try:
                y.confirmed = True
                y.save()
            except:
                messages.warning(request, "Error! Your email cannot be registered. Please contact us!")
            return render(request, template, {'email': y.email, 'action': 'confirmed'})
        else:
            return render(request, template, {'email': y.email, 'action': 'denied'})

#-------------------------------REGISTER SUCCESS VIEW----------------------
@csrf_protect
def registration_success_view(request):
    template = 'users/registration_success.html'

    try:
        sub = NewsletterUser.objects.get(email=request.GET['email'])
        if sub.conf_number == request.GET['conf_number']:
            try:
                sub.confirmed = True
                sub.save()
            except:
                messages.warning(request, "Error! Your email cannot be registered. Please contact us at +40757484560")
            return render(request, template, {'email': sub.email, 'action': 'confirmed'})
        else:
            return render(request, template, {'email': sub.email, 'action': 'denied'})
    except:
        messages.warning(request, "This email already exists in our database!")
        return render(request, template, {})
#-------------------------PROFILE VIEW---------------------------------------
@login_required
def profile(request):
    context = {
        'profile_page': "active",
    }
    return render(request, 'users/profile.html', context)
#------------------------------DASHBOARD VIEW----------------------------
@login_required
def dashboard(request):

    context = {
        'dashboard': "active",
    }
    return render(request, 'users/dashboard.html', context)

def privacy(request):
    return render(request, 'users/privacy.html')


def terms(request):
    return render(request, 'users/terms.html')


def pricing(request):
    context = {
        'rec_navbar': 1,
    }
    return render(request, 'users/pricing.html', context)
def blog(request):
    template_name = "users/blog.html"
    context = {
    }
    return render(request, 'users/pricing.html', context)


def contact(request):
    template_name = 'users/contact.html'
    #--------------logo------------------------------
    # logos = Logo.objects.filter(status='active')
    form = CaptchaForm(request.POST)
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')
        #send email
        if message and message_name and message_email:
            if form.is_valid():
                try:
                    send_mail(
                    message_name,
                    message,
                    message_email,
                    ['contact@dincolo.eu']
                    )
                    messages.success(request, "Thank you for writting me {}! I will answer ASAP.".format(message_name))
                except BadHeaderError as e:
                    messages.error(request, str(e))
                    return redirect('contact')
                return redirect('contact')
            else:

                messages.warning(request, "Failed! Please fill in the captcha field again!")
                return redirect('contact')
        else:
            messages.warning(request, "Failed! Please make sure all fields are valid!")
            return redirect('contact')

        render(request, template_name, {'message_name': message_name, 'categories': categories, 'form': form,})
    else:
        return render(request, template_name, {'form': form})

#--------------------------ABOUT VIEW -----------------------------------------
def about(request):
    template_name = 'users/about.html'
    about_list = About.objects.all()
    #--------------logo------------------------------
    # logos = Logo.objects.filter(status='active')

    # form = AboutForm(request.POST or None)
    # categories = Category.objects.all()
    context = {
        # 'logos': logos,
        # 'form': form,
        # 'categories': categories,
        'about_list': about_list,
    }
    return render(request, template_name, context)
