# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContentBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Content Block Title', max_length=100)),
                ('content', models.TextField()),
                ('display', models.BooleanField()),
                ('position', models.CharField(max_length=1, choices=[(1, b'top'), (2, b'bottom')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Team Member Name', max_length=100)),
                ('title', models.CharField(help_text=b'Team Member Role', max_length=100)),
                ('profile_pic', models.ImageField(help_text=b'Dimensions must be equal, ex: 100x100', upload_to=b'media/images/team')),
                ('bio', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
