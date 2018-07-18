# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate


from .forms import SignUpForm

# Create your views here.


def logout_view(request):
        """logs out user"""
        logout(request)
        return HttpResponseRedirect(reverse('tasks:index'))


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = SignUpForm()
    else:
        # Process completed form.
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            username = new_user.username
            password = request.POST['password1']
            authenticated_user = authenticate(username=username, password=password)
            # Log the user in and then redirect to home page.
            # login(request, authenticated_user)
            return HttpResponseRedirect(reverse('tasks:index'))
 
    context = {'form': form}
    return render(request, 'users/register.html', context)
