# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_entry_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='file',
            new_name='myUploadFile',
        ),
        migrations.RenameField(
            model_name='uploadfile',
            old_name='file',
            new_name='afile',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='body',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
