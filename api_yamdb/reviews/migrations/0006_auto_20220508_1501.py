# Generated by Django 2.2.16 on 2022-05-08 12:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='ID отзыва'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
    ]
