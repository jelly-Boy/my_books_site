from django.contrib import admin

from booksAPP.models import CitiesClass, GenreClass, AuthorsClass, BooksClass, LibrariesClass

admin.site.register(CitiesClass)
admin.site.register(GenreClass)
admin.site.register(AuthorsClass)
admin.site.register(BooksClass)
admin.site.register(LibrariesClass)
# Register your models here.
