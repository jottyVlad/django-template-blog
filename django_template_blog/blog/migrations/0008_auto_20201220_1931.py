# Generated by Django 3.1.4 on 2020-12-20 16:31

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201219_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(default='Default content'),
        ),
    ]