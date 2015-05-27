# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150522_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(default=b'a', max_length=30, verbose_name=b'Last Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=30, verbose_name=b'Designation'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name=b'First Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name=b'Last Name'),
        ),
    ]
