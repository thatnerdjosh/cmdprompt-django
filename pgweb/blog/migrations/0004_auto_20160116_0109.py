# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151231_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostCategoryRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog', models.ForeignKey(to='blog.BlogPost')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('url_slug', models.TextField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpostcategoryrelationship',
            name='category',
            field=models.ForeignKey(to='blog.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', through='blog.BlogPostCategoryRelationship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='short_description',
            field=models.TextField(default=datetime.date(2016, 1, 16), help_text=b'Description to be shown in snippets (Non-HTML to prevent collision with other HTML)'),
            preserve_default=False,
        ),
    ]
