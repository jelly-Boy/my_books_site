# Generated by Django 3.0.2 on 2020-03-14 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksAPP', '0002_auto_20200314_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librariesclass',
            name='books_list',
        ),
    ]
