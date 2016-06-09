# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_controll', '0002_auto_20160607_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zlecenie2',
            name='nr_zamowienia',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
