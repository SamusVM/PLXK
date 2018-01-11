# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_pip'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_it_admin',
            field=models.BooleanField(default=False),
        ),
    ]
