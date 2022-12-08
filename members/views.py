from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterUserForm

# user logout


def user_logout(request):
    messages.success(request, ('User successfuly logged out!'))
    return redirect('index')


# admin login
def login_account(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            messages.success(
                request, 'Sorry there was an error loging inn. Try again!')
            return redirect('user-account')
    else:
        return render(request, 'authentication/login.html', {})


# user logout
def trial_logout(request):
    logout(request)
    messages.success(request, ('User successfuly logged out!'))
    return redirect('index')


def signup_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succesful!"))
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/signup.html', {'form': form, })
