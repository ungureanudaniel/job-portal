from django.shortcuts import render

# Create your views here.
#---------------------------SUBS CONFIRMATION VIEW----------------------------
def subscription_confirmation_view(request):
    template = 'artisan_app/subscription_confirmation.html'
    try:
        sub = Subscriber.objects.get(email=request.GET['email'])
        if sub.conf_num == request.GET['conf_num']:
            try:
                sub.confirmed = True
                sub.save()
            except:
                messages.warning(request, "Eroare! Emailul dvs nu poate fi inregistrat. Va rugam sa ne contactati la +40757484560")
            return render(request, template, {'email': sub.email, 'action': 'confirmed'})
        else:
            return render(request, template, {'email': sub.email, 'action': 'denied'})
    except:
        messages.warning(request, "Acest exista deja in baza noastra de date!")
        return render(request, template, {})

#---------------------------SUBS DELETION VIEW------------------------------
def delete_subscribers_view(request):
    template = 'artisan_app/unsubscribe.html'
    if request.method == 'POST':
        try:
            unsub_email = request.POST.get('unsub_email')
            sub = Subscriber.objects.get(email=unsub_email)
            if sub:
                sub.delete()
                messages.success(request, "Emailul dvs a fost dezabonat cu succes!")
                return render(request, template, {'email': sub.email, 'action': 'unsubscribed'})
            else:
                return render(request, template, {'email': sub.email, 'action': 'denied'})
        except:
            messages.error(request, "Emailul acesta nu exista in baza noastra de date!")
            return render(request, template, {'action': 'denied'})
    else:
        return render(request, template, {})
