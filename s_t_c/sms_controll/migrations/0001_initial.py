# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_firmy', models.IntegerField()),
                ('nazwa', models.CharField(max_length=200)),
                ('kod', models.CharField(max_length=10)),
                ('miasto', models.CharField(max_length=50)),
                ('ulica', models.CharField(max_length=200)),
                ('nr_lokal', models.CharField(max_length=5)),
                ('nip', models.CharField(max_length=13)),
                ('regon', models.CharField(max_length=10)),
                ('mail', models.EmailField(max_length=254)),
                ('tel_stac', models.CharField(max_length=20)),
                ('tel_kom', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'firma',
                'verbose_name_plural': 'firmy',
            },
        ),
        migrations.CreateModel(
            name='FirmaFaktura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_firmy', models.IntegerField()),
                ('nazwa', models.CharField(max_length=200)),
                ('kod', models.CharField(max_length=10)),
                ('miasto', models.CharField(max_length=50)),
                ('ulica', models.CharField(max_length=200)),
                ('nr_lokal', models.CharField(max_length=5)),
                ('nip', models.CharField(max_length=13)),
                ('regon', models.CharField(max_length=10)),
                ('timo', models.CharField(max_length=9)),
                ('mail', models.EmailField(max_length=254)),
                ('tel_stac1', models.CharField(max_length=20)),
                ('tel_stac2', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('tel_ksiegowosc', models.CharField(max_length=20)),
                ('tel_kom1', models.CharField(max_length=20)),
                ('tel_kom2', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'firmafaktura',
                'verbose_name_plural': 'firmyfaktury',
            },
        ),
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
            options={
                'verbose_name': 'kierowca',
                'verbose_name_plural': 'kierowcy',
            },
        ),
        migrations.CreateModel(
            name='Spedytor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_firmy', models.IntegerField()),
                ('nazwa', models.CharField(max_length=200)),
                ('kod', models.CharField(max_length=10)),
                ('miasto', models.CharField(max_length=50)),
                ('ulica', models.CharField(max_length=200)),
                ('nr_lokal', models.CharField(max_length=5)),
                ('nip', models.CharField(max_length=13)),
                ('regon', models.CharField(max_length=10)),
                ('mail', models.EmailField(max_length=254)),
                ('tel_stac', models.CharField(max_length=20)),
                ('tel_kom', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'spedytor',
                'verbose_name_plural': 'spedytorzy',
            },
        ),
        migrations.CreateModel(
            name='Trasa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_zal', models.DateField()),
                ('godz_zal', models.TimeField()),
                ('nazwa_zal', models.CharField(max_length=200)),
                ('miasto_zal', models.CharField(max_length=100)),
                ('ulica_zal', models.CharField(max_length=100)),
                ('nr_ulica_zal', models.CharField(max_length=5)),
                ('data_rozl', models.DateField()),
                ('godz_rozl', models.TimeField()),
                ('nazwa_rozl', models.CharField(max_length=200)),
                ('miasto_rozl', models.CharField(max_length=100)),
                ('ulica_rozl', models.CharField(max_length=100)),
                ('nr_ulica_rozl', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_uzytkownika', models.IntegerField()),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('tel_stac', models.CharField(max_length=20)),
                ('tel_kom', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'uzytkownik',
                'verbose_name_plural': 'uzytkownicy',
            },
        ),
        migrations.CreateModel(
            name='WyslijSMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zam_id', models.IntegerField()),
                ('data_zamowienia', models.DateField()),
                ('firma_zamawiajaca', models.IntegerField()),
                ('firma_realizujaca', models.IntegerField()),
                ('data_zal', models.DateField(auto_now=True)),
                ('godz_zal', models.TimeField()),
                ('miejsce_zal', models.CharField(max_length=200)),
                ('data_roz', models.DateField()),
                ('godz_roz', models.TimeField()),
                ('miejsce_roz', models.CharField(max_length=200)),
                ('uwagi_transport', models.CharField(max_length=200)),
                ('id_przyj_zam', models.IntegerField()),
                ('id_kierowcy', models.IntegerField()),
            ],
            options={
                'verbose_name': 'zamowienie',
                'verbose_name_plural': 'zamowienia',
            },
        ),
        migrations.CreateModel(
            name='Zlecenie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr_zamowienia', models.IntegerField()),
                ('data_zamowienia', models.DateField()),
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
                ('kierowca_przewoz', models.ForeignKey(to='sms_controll.Kierowca')),
                ('trasa_przewoz', models.ForeignKey(to='sms_controll.Trasa')),
            ],
            options={
                'verbose_name': 'zlecenie',
                'verbose_name_plural': 'zlecenia',
            },
        ),
    ]
