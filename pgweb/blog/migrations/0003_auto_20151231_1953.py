# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151228_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='feature_image',
            field=models.ImageField(default=None, upload_to=b'images/featured_blog', blank=True, help_text=b'Image to be displayed when the blog is featured on the home page', null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(default=False, help_text=b'Main featured blog post (we can only have one)'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='url_slug',
            field=models.TextField(unique=True),
        ),
    ]
