# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20141128_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='myFile',
            field=models.ForeignKey(to='blog.UploadFile'),
            preserve_default=True,
        ),
    ]
