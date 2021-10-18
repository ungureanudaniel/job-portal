from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CaptchaForm


def login(request):
    return render(request, 'users/login.html')


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
                    ['danielungureanu531@gmail.com']
                    )
                    messages.success(request, "Thank you for writting me {}! I will answer ASAP.".format(message_name))
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/contact/')
            else:

                messages.warning(request, "Failed! Please fill in the captcha field again!")
                return HttpResponseRedirect('/contact/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

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
    
