from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Report(models.Model):
    ip = models.CharField('pvs ip address', max_length=20,default='')
    hardware = models.CharField('pi hardware', max_length=20,default='')
    revision = models.CharField('pi revision', max_length=20,default='')
    serial = models.CharField('pi serial', max_length=20,default='')
    dbconfig = models.TextField('pvs dbconfig', default='{}')
    last_update_time = models.DateTimeField('last update time',default=datetime.now)

class DbConfig(models.Model):
    serial = models.CharField('pi serial', max_length=20)
    dbconfig = models.TextField('pvs dbconfig', default='{}')
    create_time = models.DateTimeField('created time', default=datetime.now)
    pvs_update_time = models.DateTimeField('pvs update time', null=True)
    pvs_updated = models.BooleanField('pvs update acked', default=False)