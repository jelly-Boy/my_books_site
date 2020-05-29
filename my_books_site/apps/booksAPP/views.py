import xlwt

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *



def indexBook(request):
    books_list = BooksClass.objects.order_by('pub_date')[:8]
    return render(request, 'booksAPP/bookMainPage.html', {'books_list': books_list})

def indexLibraries(request):
    libraries_list = LibrariesClass.objects.order_by('name')
    return render(request, 'booksAPP/libMainPage.html', {'libraries_list': libraries_list})

def indexGenres(request):
    genres_list = BooksClass.objects.order_by('pub_date')
    return render(request, 'booksAPP/bookMainPage.html', {'genres_list': genres_list})

def indexAuthors(request):
    authors_list = BooksClass.objects.order_by('pub_date')
    return render(request, 'booksAPP/bookMainPage.html', {'authors_list': authors_list})

def indexCities(request):
    cities_list = BooksClass.objects.order_by('pub_date')
    return render(request, 'booksAPP/bookMainPage.html', {'cities_list': cities_list})

def detailBook(request, book_id):
    try:
        book = BooksClass.objects.get(bookID=book_id)
    except:
        raise Http404("No such books!")
    return render(request, 'booksAPP/detailBook.html', {'book': book})

"""def book_libs(request, book_name):
    b = BooksClass.objects.get(name=book_name)
    lib = b.av_in_libs.v
    lib_list = []
    for i in lib:
        lib_list.__add__(LibrariesClass.objects.filter(name=i))
    if lib_list is None:
        raise Http404("This book is not available in libraries")
    else:
        return render(request, 'booksAPP/libs_book.html', {'lib_list': lib_list})
"""



def chart(request):
    genres_list = GenreClass.objects.order_by('name')
    books_list = BooksClass.objects.order_by('bookID')
    num_list = []
    gen_list = []
    for genre in genres_list:
        i = 0
        for book in books_list:
            if genre.genreID == book.genreID.genreID:
                i = i+1
        num_list.append(i)
        gen_list.append(genre.name)

    data = {"genres": genres_list, "num": num_list}
    return render(request, 'booksAPP/chartsPage.html', context=data)

def export_books_data(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="books.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Books')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Book', 'Author name', 'Author surname', 'Author lastname', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = BooksClass.objects.all().values_list('name', 'authorID__first_name', 'authorID__second_name', 'authorID__third_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



