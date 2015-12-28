# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20151227_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Career Name', max_length=100)),
                ('description', tinymce.models.HTMLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
