# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 07:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvs', '0002_auto_20160920_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=20, verbose_name='pi serial')),
                ('dbconfig', models.TextField(default='{}', verbose_name='pvs dbconfig')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='created time')),
                ('pvs_update_time', models.DateTimeField(null=True, verbose_name='pvs update time')),
                ('pvs_updated', models.BooleanField(default=False, verbose_name='pvs update acked')),
            ],
        ),
    ]
