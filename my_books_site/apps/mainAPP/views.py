from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import city
class city_create_view (CreateView):
    model = city
    fields = ('name', 'country')


def index(request):
    return render(request, 'mainAPP/homePage.html')
# return render(request, 'mainAPP/homePage.html')
# return HttpResponse("startPage  http://127.0.0.1:8000/books")