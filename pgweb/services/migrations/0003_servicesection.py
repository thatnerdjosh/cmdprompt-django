# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20160111_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', tinymce.models.HTMLField()),
                ('service', models.ForeignKey(blank=True, to='services.Service', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
