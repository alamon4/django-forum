# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='myUploadFile',
        ),
        migrations.AddField(
            model_name='entry',
            name='afile',
            field=models.FileField(default=0, upload_to=b'files'),
            preserve_default=False,
        ),
    ]
