# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_uploadfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='file',
            field=models.ForeignKey(default=2, to='blog.UploadFile'),
            preserve_default=False,
        ),
    ]
