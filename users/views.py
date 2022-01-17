from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import CaptchaForm
from django.core.mail import send_mail, BadHeaderError
from .models import Candidate, Company
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
import random

def login(request):
    return render(request, 'users/login.html')
#-------------------------------LOGIN VIEW-----------------------------------
def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                user1 = Candidate.objects.get(user=user)
                if user1.type == "candidate":
                    login(request, user)
                    return redirect("candidate_dashboard")
            else:
                return render(request, "users/login.html", {})
    return render(request, "users/login.html")
#-----------------------GENERATE RANDOM SUBSCRIBER ID--------------------------
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)
#-------------------------------REGSTER VIEW-----------------------------------
def register(request):
    form = CaptchaForm(request.POST)
    if request.method=="POST":
        type = request.POST.get('type', False)
        if type == 'freelancer':
            username = request.POST['emailaddress-register']
            first_name=request.POST['first-name-register']
            last_name=request.POST['last-name-register']
            password1 = request.POST['password-register']
            password2 = request.POST['password-repeat-register']
            phone = request.POST['phone-register']
            birth = request.POST['birth-register']
            gender = request.POST['gender-register']
            img = request.FILES['image2']
            check = request.POST['checks[]']
            if form.is_valid():
                if password1 != password2:
                    messages.error(request, "Passwords do not match.")
                    return redirect('register')
                elif check != "Agree":
                    messages.error(request, "Please check box to agree to our terms and conditions.")
                    return redirect('register')
                try:
                    user_check = User.objects.get(username=username)
                    email_check = User.objects.get(email=username)
                    if user_check:
                        messages.error(request, "This user name already exists!")
                        return redirect('register')
                    elif email_check:
                        messages.error(request, "This user email address already exists!")
                        return redirect('register')
                except Exception as e:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=username, password=password1)
                    candidates = Candidate.objects.create(user=user, email=username, phone=phone, gender=gender, birthdate = birth, image=img, type=type, conf_number=random_digits())
                    conf_number=random_digits()
                    user.save()
                    candidates.save()
                    #---------------------send confirmation email settings------
                    conf_subject = "DINCOLO account confirmation"
                    from_email=settings.FROM_EMAIL
                    conf_message = ''
                    html_content='Thank you for joining our job platform! You will not regret it.\
                        To finalize the process please \
                                <a href="{}registration_confirmation/?email={}&conf_number={}"> click this link \
                                </a>.'.format(request.build_absolute_uri(''), user.email, candidates.conf_number)
                    try:
                        send_mail(conf_subject, conf_message, from_email, [user.email], html_message=html_content)

                        context = {
                            }

                    except Exception as e:
                        return HttpResponse('Invalid header found.')
                    return redirect('login')
            return render(request, "users/login.html", {'form':form})
        elif type == 'employer':
            username = request.POST['emailaddress-register']
            company_name=request.POST['company_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            phone = request.POST['phone-reg']
            identification_nr = request.POST['id-register']
            img = request.FILES['image1']
            check = request.POST['checks[]']
            if form.is_valid():
                if password1 != password2:
                    messages.error(request, "Passwords do not match.")
                    return redirect('register')
                elif check is None:
                    messages.error(request, "Please check box to agree to our terms and conditions.")
                    return redirect('register')
                try:
                    user = User.objects.create_user(first_name="", last_name=company_name, username=username, email=username, password=password1)
                    print(user)
                except Exception as e:
                    messages.error(request, "This user email already exists.")
                    return redirect('register')
                try:
                    companies = Company.objects.create(user=user, email=username, phone=phone, identification = identification_nr, company_name = company_name, description = "", address = "", image=img, type=type, conf_number=random_digits())
                    user.save()
                    companies.save()
                    #---------------------send confirmation email settings------
                    conf_subject = "DINCOLO account confirmation"
                    from_email=settings.FROM_EMAIL
                    conf_message = ''
                    html_content='Thank you for joining our job platform!\
                        To finalize the process please \
                                <a href="{}registration_confirmation/?email={}&conf_number={}"> click this link \
                                </a>.'.format(request.build_absolute_uri(''), user.email, companies.conf_number)
                    try:
                        send_mail(conf_subject, conf_message, from_email, [user.email], html_message=html_content)

                        context = {
                            }

                    except Exception as e:
                        print(e)
                        messages.error(request, str(e))
                        return redirect('register')
                except Exception as e:
                    messages.error(request, str(e))
                    return redirect('register')
            return render(request, "users/login.html", {'form':form, 'username':username})
    return render(request, 'users/register.html', {'form':form})
#-------------------------------REGISTER CONFIRMATION VIEW----------------------
@csrf_protect
def registration_conf_view(request):
    template = 'users/registration_conf.html'
    try:
        x = Company.objects.get(email=request.GET['email'])
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
#-------------------------ACCOUNT VIEW---------------------------------------
@login_required
def account(request):
    context = {
        'account_page': "active",
    }
    return render(request, 'users/account.html', context)

def privacy(request):
    return render(request, 'users/privacy.html')


def terms(request):
    return render(request, 'users/terms.html')


def pricing(request):
    context = {
        'rec_navbar': 1,
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
                    ['contact@ninjaweb.tech']
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
