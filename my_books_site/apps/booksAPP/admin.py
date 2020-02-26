from django.contrib import admin
from .models import CitiesClass, BooksClass, LibrariesClass, AuthorsClass, GenreClass


admin.site.register(CitiesClass)
admin.site.register(BooksClass)
admin.site.register(LibrariesClass)
admin.site.register(AuthorsClass)
admin.site.register(GenreClass)
