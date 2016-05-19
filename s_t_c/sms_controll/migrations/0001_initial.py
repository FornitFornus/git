# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kierowca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Imie', models.CharField(max_length=50)),
                ('Nazwisko', models.CharField(max_length=50)),
                ('Prefix_tel', models.CharField(max_length=3)),
                ('Nr_tel_kom', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=50)),
                ('Firma_id', models.IntegerField()),
                ('Firma', models.CharField(max_length=50)),
                ('Nr_rej_sam', models.CharField(max_length=10)),
                ('Typ_sam', models.CharField(max_length=200)),
                ('Dane_sam', models.CharField(max_length=200)),
            ],
        ),
    ]
