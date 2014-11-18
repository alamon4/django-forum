# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='body',
            field=models.CharField(default=b' ', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=b' ', max_length=40),
            preserve_default=True,
        ),
    ]
