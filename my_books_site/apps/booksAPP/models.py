from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


def is_valid_birth(value):
    if value.year > (date.today().year - 10):
        raise ValidationError('Wrong birth data')

def is_valid_pub(value):
    if value > date.today():
        raise ValidationError('Choose correct publication date')

class CitiesClass(models.Model):
    cityID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False, unique=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

class GenreClass(models.Model):
    genreID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False, unique=True)
    features = models.TextField(max_length=300, blank=True, unique=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

class AuthorsClass(models.Model):
    authorID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    third_name = models.CharField(max_length=40, blank=True)
    year_of_birth = models.DateField(validators=[is_valid_birth])

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.third_name}'

class LibrariesClass(models.Model):
    libraryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False, unique=True)
    address = models.CharField(max_length=60, null=False, unique=True)
    cityID = models.ForeignKey(CitiesClass, models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'

    def __str__(self):
        return self.name

class BooksClass(models.Model):
    bookID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='books_images', default='default.jpg')
    name = models.CharField(max_length=40, unique=True)
    info_about_book = models.TextField(max_length=500, blank=True)
    pub_date = models.DateField(validators=[is_valid_pub])
    genreID = models.ForeignKey(GenreClass, models.SET_NULL, null=True)
    authorID = models.ForeignKey(AuthorsClass, models.SET_NULL, null=True, default="Author wasn't mentioned")
    av_in_libs = models.ManyToManyField(LibrariesClass)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name



