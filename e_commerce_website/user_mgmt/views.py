from django.shortcuts import render, redirect

from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.

@unauthenticated_user
def signupPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            f_name = form.cleaned_data.get('first_name')
            l_name = form.cleaned_data.get('last_name')
            messages.success(request, "User successfully created for "+f_name +' '+l_name)
            return redirect('login')

    context = {'form': form}
    return render(request, 'account-pages/signup.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, "Incorrect Username or Password")
            return redirect('login')
    context = {}
    return render(request, 'account-pages/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# def homePage(request):
#     return render(request, 'pages/index.html')

# @login_required(login_url='login')
# def cartPage(request):
#     return render(request, 'pages/cart.html')
    