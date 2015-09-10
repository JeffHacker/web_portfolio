from django.http import request
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


def landing(request):
    return render_to_response('landing.html', context_instance=RequestContext(request))

def portfolio_links(request):
    return render_to_response('portfolio_links.html', context_instance=RequestContext(request))

def resume(request):
    return render_to_response('resume.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def contacts(request):
    return render_to_response('contacts.html', context_instance=RequestContext(request))
