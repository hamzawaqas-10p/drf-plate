# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150522_0840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Employee',
        ),
    ]
