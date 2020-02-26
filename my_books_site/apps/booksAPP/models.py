from django.db import models


class CitiesClass(models.Model):
    cityID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class GenreClass(models.Model):
    genreID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False)
    features = models.TextField(max_length=300, blank=True)

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
    year_of_birth = models.DateField(blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        name = self.first_name + " " + self.second_name + " " + self.third_name
        return name


class BooksClass(models.Model):
    bookID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False)
    info_about_book = models.TextField(max_length=500, blank=True)
    pub_date = models.DateField(blank=True)
    genreID = models.ForeignKey(GenreClass, models.SET_NULL, null=True)
    authorID = models.ForeignKey(AuthorsClass, models.SET_NULL, null=True, default="Author wasn't mentioned")

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name


class LibrariesClass(models.Model):
    libraryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    address = models.CharField(max_length=60, null=False)
    num_of_books = models.BigIntegerField(default=0)
    cityID = models.ForeignKey(CitiesClass, models.SET_NULL, null=True)
    books_list = models.ManyToManyField(BooksClass)

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'

    def __str__(self):
        return self.name
# Create your models here.
