# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgfile',
            field=models.FileField(upload_to='files/%Y/%m/%d', default=datetime.datetime(2015, 8, 21, 7, 8, 34, 766223, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
