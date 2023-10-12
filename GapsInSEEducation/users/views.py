from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
import logging

# Create your views here.
from users.models import Details

logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        details = Details.objects.all().get(user=user)
        details.age_range = request.POST.get('age-range')
        messages.add_message(request,
                             messages.SUCCESS,
                             "You successfully register with the username: %s" % user.username)
        return redirect('GapsInSoftwareEngineeringEducation:gaps_home')
    else:
        return render(request, "users/user/register.html")


def profile(request, username):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        first_name = request.POST.get('first-name').strip()
        last_name = request.POST.get('last-name').strip()
        age_range = request.POST.get('age-range')
        role = request.POST.get('role')
        user = User.objects.get(username=username)
        details = Details.objects.all().get(user=user)
        if email != '':
            user.email = email
        if password != '':
            user.set_password(password)
        if first_name != '':
            user.first_name = first_name
        if last_name != '':
            user.last_name = last_name
        if age_range != '':
            details.age_range = age_range
        if role is not None and role != '':
            details.role = role
        user.save()
        details.save()

        return render(request,
                      "users/user/profile.html",
                      {"user": user})
    else:
        user1 = get_object_or_404(User, username=username)
        return render(request,
                      "users/user/profile.html",
                      {"user": user1})


# Login functionality
def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    logger.warning(username)
    logger.warning(password)

    user = authenticate(username=username, password=password)
    logger.warning(user)
    if user is not None:
        request.session['username'] = user.username
        request.session['role'] = user.details.role
        # messages.add_message(request,
        #                      messages.SUCCESS,
        #                      "You successfully logged in with the username: %s" % user.username)
        return redirect('GapsInSoftwareEngineeringEducation:gaps_home')
    else:
        # messages.add_message(request,
        #                      messages.ERROR,
        #                      "Invalid username or password")
        return redirect('GapsInSoftwareEngineeringEducation:gaps_home')


# Logout functionality
def logout_user(request):
    del request.session['username']
    del request.session['role']
    return redirect('GapsInSoftwareEngineeringEducation:gaps_home')
