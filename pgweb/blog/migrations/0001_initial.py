# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url_slug', models.CharField(default=None, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('body', tinymce.models.HTMLField()),
                ('meta_keywords', models.TextField(null=True, blank=True)),
                ('meta_description', models.TextField(null=True, blank=True)),
                ('list_on_side', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('feature_image', models.ImageField(default=None, upload_to=b'media/images/featured_blog', blank=True, help_text=b'Image to be displayed when the blog is featured on the home page', null=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
