# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcontentblock',
            name='position',
            field=models.CharField(max_length=1, choices=[(b'T', b'top'), (b'B', b'bottom')]),
        ),
    ]
