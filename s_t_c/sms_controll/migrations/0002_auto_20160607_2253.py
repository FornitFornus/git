# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_controll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zlecenie2',
            fields=[
                ('nr_zamowienia', models.AutoField(serialize=False, primary_key=True)),
                ('data_zamowienia', models.DateField()),
                ('status_zlecenia', models.CharField(default=b'DO REALIZACJI', max_length=14, choices=[(b'DO REALIZACJI', b'DO REALIZACJI'), (b'REALIZOWANE', b'REALIZOWANE'), (b'ZREALIZOWANE', b'ZREALIZOWANE')])),
                ('towar', models.CharField(max_length=200)),
                ('pojazd', models.CharField(max_length=200)),
                ('fracht', models.FloatField()),
                ('waluta_fracht', models.CharField(default=b'PLN', max_length=3, choices=[(b'PLN', b'PLN'), (b'EUR', b'EUR'), (b'INNA', b'INNA')])),
                ('uwagi_waluta', models.CharField(max_length=200)),
                ('uwagi_fracht', models.CharField(max_length=200)),
                ('odp_celna_export', models.CharField(max_length=50)),
                ('odp_celna_przywozowa', models.CharField(max_length=50)),
                ('uwagi', models.CharField(max_length=200)),
                ('uwagi_opis', models.TextField()),
                ('firma_realizujaca', models.ForeignKey(to='sms_controll.FirmaFaktura')),
                ('firma_zamawiajaca', models.ForeignKey(to='sms_controll.Firma')),
            ],
            options={
                'verbose_name': 'zlecenie',
                'verbose_name_plural': 'zlecenia',
            },
        ),
        migrations.AlterModelOptions(
            name='trasa',
            options={'verbose_name': 'trasa', 'verbose_name_plural': 'trasy'},
        ),
        migrations.RemoveField(
            model_name='kierowca',
            name='Firma',
        ),
        migrations.RemoveField(
            model_name='kierowca',
            name='Firma_id',
        ),
        migrations.RemoveField(
            model_name='zlecenie',
            name='id',
        ),
        migrations.AddField(
            model_name='zlecenie',
            name='status_zlecenia',
            field=models.CharField(default=b'DO REALIZACJI', max_length=14, choices=[(b'DO REALIZACJI', b'DO REALIZACJI'), (b'REALIZOWANE', b'REALIZOWANE'), (b'ZREALIZOWANE', b'ZREALIZOWANE')]),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='nr_zamowienia',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='zlecenie2',
            name='kierowca_przewoz',
            field=models.ForeignKey(to='sms_controll.Kierowca'),
        ),
        migrations.AddField(
            model_name='zlecenie2',
            name='trasa_przewoz',
            field=models.ForeignKey(to='sms_controll.Trasa'),
        ),
    ]
