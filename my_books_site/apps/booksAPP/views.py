from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import BooksClass


def index(request):
    books_list = BooksClass.objects.order_by('bookID')[:3]
    return render(request, 'booksAPP/bookPage.html', {'books_list': books_list})


def detail(request, book_id):
    try:
        book = BooksClass.objects.get(bookID=book_id)
    except:
        raise Http404("No such books!")
    return render(request, 'booksAPP/detail.html', {'book': book})
