# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('url_slug', models.TextField(unique=True)),
                ('description', models.TextField()),
                ('picture', models.ImageField(help_text=b'Dimensions must be equal, ex: 100x100', upload_to=b'images/product')),
                ('short_description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductFeatureGrid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_name', models.TextField()),
                ('product', models.ForeignKey(blank=True, to='products.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductFeatureGridObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('feature_grid', models.ForeignKey(blank=True, to='products.ProductFeatureGrid', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', tinymce.models.HTMLField()),
                ('product', models.ForeignKey(blank=True, to='products.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
