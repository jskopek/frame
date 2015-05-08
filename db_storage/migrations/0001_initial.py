# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('file_name', models.CharField(max_length=255, unique=True, serialize=False, primary_key=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('data', models.BinaryField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
