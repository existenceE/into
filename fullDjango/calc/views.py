from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
# Create your views here.


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    return HttpResponse(str(int(a)+int(b)))

def index(request):
    return render(request, 'home.html')

def old_redirect(request,a,b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))
