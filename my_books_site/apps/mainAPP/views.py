from django.shortcuts import render

from django.http import HttpResponse



from django.views.generic import CreateView


def index(request):
    return render(request, 'mainAPP/homePage.html')

def firstplot(request):
    return




