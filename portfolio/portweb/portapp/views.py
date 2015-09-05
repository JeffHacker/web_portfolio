from django.http import request
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


def landing(request):
    return render_to_response('landing.html', context_instance=RequestContext(request))
