# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
