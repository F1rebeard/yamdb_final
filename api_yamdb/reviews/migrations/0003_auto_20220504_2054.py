# Generated by Django 2.2.16 on 2022-05-04 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220504_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.DeleteModel(
            name='GenreTitle',
        ),
    ]
