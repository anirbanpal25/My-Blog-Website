# Generated by Django 4.1.5 on 2023-02-14 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_author_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='genre',
        ),
    ]
