# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_controll', '0003_auto_20160607_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zlecenie2',
            options={'verbose_name': 'zlecenie2', 'verbose_name_plural': 'zlecenia2'},
        ),
        migrations.AlterField(
            model_name='zlecenie2',
            name='nr_zamowienia',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
