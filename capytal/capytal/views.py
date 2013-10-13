"""
General application wide views.
"""

from django.contrib.auth.views import login, logout
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def homepage(request, *args, **kwargs):
    """Display the website homepage"""
    return render_to_response('base.html', RequestContext(request))

def user_login(request, *args, **kwargs):
    """Log the user in"""
    return login(request, template_name='login.html', *args, **kwargs)

def user_options(request, *args, **kwargs):
    """go to user options page"""
    return render_to_response('options.html', RequestContext(request))

def user_logout(request, *args, **kwargs):
    """Log the user out and redirect him/her to the homepage"""
    logout(request, *args, **kwargs)
    return redirect('capytal.views.homepage')
