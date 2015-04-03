# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pointDiary', '0002_auto_20150309_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='user',
            field=models.TextField(default='phil'),
            preserve_default=False,
        ),
    ]
