# Generated by Django 5.2 on 2025-04-12 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contactmodel_website'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactLink',
        ),
    ]
