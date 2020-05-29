# Generated by Django 3.0.2 on 2020-03-14 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authorsclass',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='booksclass',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='citiesclass',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='genreclass',
            options={'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='librariesclass',
            options={'verbose_name': 'Library', 'verbose_name_plural': 'Libraries'},
        ),
        migrations.RemoveField(
            model_name='librariesclass',
            name='num_of_books',
        ),
    ]
