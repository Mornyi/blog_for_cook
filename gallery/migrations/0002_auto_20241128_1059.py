# Generated by Django 3.2.25 on 2024-11-28 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'галлерею', 'verbose_name_plural': 'Галлереи'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'фотографию', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
