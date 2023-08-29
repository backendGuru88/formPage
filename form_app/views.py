from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        usern = request.POST.get('userName')
        password = request.POST.get('passwd')
        user_object = authenticate(request, username=usern, password=password)
        if user_object is not None:
            login(request, user_object)
            return redirect('welcome')
        else:
            pass

    return render(request, 'login.html')
def welcome(request):
    return render(request, 'welcome.html')

