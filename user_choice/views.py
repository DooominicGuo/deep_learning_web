from django.shortcuts import render


from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone
from user_choice.forms import LoginForm, RegistrationForm, ChosenForm
from user_choice.models import Choice, Profile


# this method defines login action
def login_action(request):
    context = {}

    #if nothing is filled we just got into the login website.
    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'login.html', context)
    
    # if we have something filled which html send post
    form = LoginForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'login.html', context)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    login(request, new_user)
    return redirect(reverse('choose'))


def register_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'register.html', context)

    profile = Profile()
    profile.creation_time = timezone.now()
    form = RegistrationForm(request.POST, instance = profile)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    login(request, new_user)
    form.save()
    return redirect(reverse('choose'))

def choosing_section(request):
    context = {}

    if request.method == 'GET':
        context['form'] = ChosenForm()
        return render(request, 'choose.html', context)
    new_Choice = Choice(firstChoice  = request.POST['firstChoice'],
                        secondChoice = request.POST['secondChoice'],
                        thirdChoice = request.POST['thirdChoice'],
                        created_by = request.user.username,
                        creation_time = timezone.now())
    new_Choice.save()
    return redirect(reverse('ending'))

def ending(request):
    return render(request, 'ending.html')



