# Generated by Django 4.0.3 on 2023-01-01 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_alter_books_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'book'},
        ),
    ]
