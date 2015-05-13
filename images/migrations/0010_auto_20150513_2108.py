# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_auto_20150104_1003'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='image',
            index_together=set([('variation', 'hash')]),
        ),
    ]
