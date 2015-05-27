# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150522_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'First Name')),
                ('middle_name', models.CharField(default=b'a', max_length=30, verbose_name=b'Middle Name')),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Last Name')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
