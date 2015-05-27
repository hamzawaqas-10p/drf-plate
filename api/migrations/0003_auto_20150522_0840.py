# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150522_0831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='middle_name',
            new_name='designation',
        ),
    ]
