# Generated by Django 3.1.4 on 2020-12-16 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]