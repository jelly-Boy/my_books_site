from django.urls import path
from . import views

app_name = 'booksAPP'
urlpatterns = [
    path('books/', views.indexBook, name='indexBook'),
    path('libraries/', views.indexLibraries, name='indexLibraries'),
    path('genres/', views.indexGenres, name='indexGenres'),
    path('authors/', views.indexAuthors, name='indexAuthors'),
    path('cities/', views.indexCities, name='indexCities'),
    path('', views.chart, name='chart'),
    path('<int:book_id>/', views.detailBook, name='detailBook'),
    # path('<slug:book_name>/', views.book_libs, name='book_libs'),
    path(r'^export/xls/$', views.export_books_data, name='export_books_data'),
]
