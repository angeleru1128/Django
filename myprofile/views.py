from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def top(request):
    context = {
        'name': 'たろう',
    }
    return render(request, 'myprofile/top.html', context)

def resume(request):
    context = {
        'job': '職務経歴書です',
    } 
    return render(request, 'myprofile/resume.html', context)
