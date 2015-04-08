# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unique_name',
            field=models.CharField(default=datetime.datetime(2015, 4, 8, 12, 47, 15, 121000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
