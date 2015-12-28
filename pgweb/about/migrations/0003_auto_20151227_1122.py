# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20151227_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcontentblock',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
