# Generated by Django 3.1.2 on 2020-11-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default='', verbose_name='Текст'),
        ),
    ]