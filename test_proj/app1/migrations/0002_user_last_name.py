# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.TextField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]
