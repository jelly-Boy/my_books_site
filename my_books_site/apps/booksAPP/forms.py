from django import forms
from .models import BooksClass
from django.core.exceptions import ValidationError
from datetime import date

class BookForm(forms.Form):
    name = forms.CharField(max_length=40)
    info_about_book = forms.Textarea()
    pub_date = forms.DateField()
    genreID = forms.IntegerField()
    authorID = forms.IntegerField()

    def validate_pubdate(self):
        if self.pub_date > date.today():
            raise ValidationError('Wrong publication date')
        else:
            return self.pub_date

    def save(self):
        new_book = BooksClass.objects.create(
            name=self.cleaned_data['name'],
            info_about_book=self.cleaned_data['info_about_book'],
            pub_date=self.cleaned_data['pub_date'],
            genreID=self.cleaned_data['genreID'],
            authorID=self.cleaned_data['authorID'])
        return new_book
