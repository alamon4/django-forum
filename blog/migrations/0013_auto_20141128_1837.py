# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20141128_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='afile',
        ),
        migrations.AddField(
            model_name='entry',
            name='myFile',
            field=models.ForeignKey(default=False, to='blog.UploadFile'),
            preserve_default=True,
        ),
    ]
