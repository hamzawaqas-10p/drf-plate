# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150522_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(default=b'a', max_length=30, verbose_name=b'Middle Name'),
        ),
    ]
