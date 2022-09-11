from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

#---------------------------------LOGIN VIEW-----------------------------------

def user_login(request):
    template = 'users/login.html'

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("login")
    else:
        return render(request, template, {})

#---------------------------------LOGOUT VIEW-----------------------------------
def user_logout(request):
    try:
        logout(request)
    except (Exception, ValueError) as e:
        print(e)
    return redirect('/')
