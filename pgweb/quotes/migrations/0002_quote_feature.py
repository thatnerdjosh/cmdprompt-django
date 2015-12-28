# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='feature',
            field=models.BooleanField(default=False, help_text=b'Display on home page, only one quote can be displayed at a time'),
            preserve_default=True,
        ),
    ]
