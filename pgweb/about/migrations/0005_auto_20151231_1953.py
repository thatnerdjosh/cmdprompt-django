# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='profile_pic',
            field=models.ImageField(help_text=b'Dimensions must be equal, ex: 100x100', upload_to=b'images/team'),
        ),
    ]
