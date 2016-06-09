from django.db import models
from django.template.defaultfilters import default
from pip.cmdoptions import editable
#from django.contrib.auth.models import User


# Create your models here.
class Kierowca(models.Model):
    """Klasa reprezentujaca Kierowce w systemie"""
    Imie = models.CharField(max_length = 50)
    Nazwisko = models.CharField(max_length = 50)
    Prefix_tel = models.CharField(max_length = 3)
    Nr_tel_kom = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 50)
    Nr_rej_sam = models.CharField(max_length = 10)
    Typ_sam = models.CharField(max_length = 200)
    Dane_sam = models.CharField(max_length = 200)
    
    class Meta:
        verbose_name = u'kierowca'
        verbose_name_plural = u'kierowcy'
        
    def __unicode__(self):
        return '%s %s %s' % (self.Imie, self.Nazwisko, self.Nr_tel_kom)
    
class Zamowienie(models.Model):
    """Klasa reprezentujace Zamowienie w systemie"""
    zam_id = models.IntegerField()
    data_zamowienia = models.DateField()
    firma_zamawiajaca = models.IntegerField()
    firma_realizujaca = models.IntegerField()
    data_zal = models.DateField(auto_now=True)
    godz_zal = models.TimeField()
    miejsce_zal = models.CharField(max_length=200)
    data_roz = models.DateField()
    godz_roz = models.TimeField()
    miejsce_roz = models.CharField(max_length=200)
    uwagi_transport = models.CharField(max_length=200)
    id_przyj_zam = models.IntegerField()
    id_kierowcy = models.IntegerField()

    class Meta:
        verbose_name = u'zamowienie'
        verbose_name_plural = u'zamowienia'


class Spedytor(models.Model):
    id_firmy = models.IntegerField()
    nazwa = models.CharField(max_length=200)
    kod = models.CharField(max_length=10)
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=200)
    nr_lokal = models.CharField(max_length=5)
    nip = models.CharField(max_length=13)
    regon = models.CharField(max_length=10)
    mail = models.EmailField()
    tel_stac = models.CharField(max_length=20)
    tel_kom = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = u'spedytor'
        verbose_name_plural = u'spedytorzy'
        
    def __unicode__(self):
        return '%s %s %s %s' % (self.nazwa, self.miasto, self.ulica)

'Firma zlecajaca przwoz'
class Firma(models.Model):
    id_firmy = models.IntegerField()
    nazwa = models.CharField(max_length=200)
    kod = models.CharField(max_length=10)
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=200)
    nr_lokal = models.CharField(max_length=5)
    nip = models.CharField(max_length=13)
    regon = models.CharField(max_length=10)
    mail = models.EmailField()
    tel_stac = models.CharField(max_length=20)
    tel_kom = models.CharField(max_length=20)
        
    class Meta:
        verbose_name = u'firma'
        verbose_name_plural = u'firmy'

    def __unicode__(self):
        return '%s %s %s' % (self.nazwa, self.miasto, self.ulica)
    
'Model firmy wystawiajcej fakture'
class FirmaFaktura(models.Model):
    id_firmy = models.IntegerField()
    nazwa = models.CharField(max_length=200)
    kod = models.CharField(max_length=10)
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=200)
    nr_lokal = models.CharField(max_length=5)
    nip = models.CharField(max_length=13)
    regon = models.CharField(max_length=10)
    timo = models.CharField(max_length=9) 
    mail = models.EmailField()
    tel_stac1 = models.CharField(max_length=20)
    tel_stac2 = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    tel_ksiegowosc = models.CharField(max_length=20)
    tel_kom1 = models.CharField(max_length=20)
    tel_kom2 = models.CharField(max_length=20)
        
    class Meta:
        verbose_name = u'firmafaktura'
        verbose_name_plural = u'firmyfaktury'

    def __unicode__(self):
        return '%s %s %s' % (self.nazwa, self.miasto, self.ulica)    

class Uzytkownik(models.Model):
    id_uzytkownika = models.IntegerField()
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    mail = models.EmailField()
    tel_stac = models.CharField(max_length=20)
    tel_kom = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = u'uzytkownik'
        verbose_name_plural = u'uzytkownicy'
        
    def __unicode__(self):
        return '%s %s %s %s' % (self.imie, self.nazwisko, self.mail)

class Trasa(models.Model):
    data_zal = models.DateField()
    godz_zal = models.TimeField()
    nazwa_zal = models.CharField(max_length=200)
    miasto_zal = models.CharField(max_length=100)
    ulica_zal = models.CharField(max_length=100)
    nr_ulica_zal = models.CharField(max_length=5)
    
    data_rozl = models.DateField()
    godz_rozl = models.TimeField()
    nazwa_rozl = models.CharField(max_length=200)
    miasto_rozl = models.CharField(max_length=100)
    ulica_rozl = models.CharField(max_length=100)
    nr_ulica_rozl = models.CharField(max_length=5)
    
    class Meta:
        verbose_name = u'trasa'
        verbose_name_plural = u'trasy'   
        
    def __unicode__(self):
        return '%s %s' % (self.nazwa_zal, self.nazwa_rozl)         
    

'Zamowienie/Zlecenie  przewozowe'
class Zlecenie(models.Model):
    """Klasa reprezentujace Zamowienie w systemie"""
    nr_zamowienia = models.AutoField(primary_key=True)
    data_zamowienia = models.DateField()
    
    DO_REALIZACJI = 'DO REALIZACJI'
    REALIZOWANE = 'REALIZOWANE'
    ZREALIZOWANE = 'ZREALIZOWANE'
    STATUS_ZLECENIA_WYBOR = (
       (DO_REALIZACJI, 'DO REALIZACJI'),
       (REALIZOWANE, 'REALIZOWANE'),
       (ZREALIZOWANE, 'ZREALIZOWANE')              
    )
    status_zlecenia = models.CharField(max_length=14, choices=STATUS_ZLECENIA_WYBOR, default = DO_REALIZACJI)
    firma_realizujaca = models.ForeignKey(FirmaFaktura)
    firma_zamawiajaca = models.ForeignKey(Firma)
    kierowca_przewoz = models.ForeignKey(Kierowca)
    trasa_przewoz = models.ForeignKey(Trasa)
    towar = models.CharField(max_length=200)
    pojazd = models.CharField(max_length=200)
    fracht = models.FloatField()
    
    PLN = 'PLN'
    EUR = 'EUR'
    INNA = 'INNA'
    WALUTA_SYMBOL = (
       (PLN, 'PLN'),
       (EUR, 'EUR'),
       (INNA, 'INNA'),              
    )

    waluta_fracht = models.CharField(max_length=3, choices=WALUTA_SYMBOL, default = PLN) 
    uwagi_waluta = models.CharField(max_length=200)
    uwagi_fracht = models.CharField(max_length=200)
    odp_celna_export = models.CharField(max_length=50)
    odp_celna_przywozowa = models.CharField(max_length=50)
    uwagi = models.CharField(max_length=200)
    uwagi_opis = models.TextField()
    
    
    
    class Meta:
        verbose_name = u'zlecenie'
        verbose_name_plural = u'zlecenia'
        
    def __unicode__(self):
        return '%s %s' % (self.firma_realizujaca, self.firma_zamawiajaca)    
    
class Zlecenie2(models.Model):
    """Klasa reprezentujace Zamowienie w systemie"""
    #readonly_fields = ('id')
    nr_zamowienia = models.AutoField(primary_key=True)
    data_zamowienia = models.DateField()
    
    DO_REALIZACJI = 'DO REALIZACJI'
    REALIZOWANE = 'REALIZOWANE'
    ZREALIZOWANE = 'ZREALIZOWANE'
    STATUS_ZLECENIA_WYBOR = (
       (DO_REALIZACJI, 'DO REALIZACJI'),
       (REALIZOWANE, 'REALIZOWANE'),
       (ZREALIZOWANE, 'ZREALIZOWANE')              
    )
    status_zlecenia = models.CharField(max_length=14, choices=STATUS_ZLECENIA_WYBOR, default = DO_REALIZACJI)
    firma_realizujaca = models.ForeignKey(FirmaFaktura)
    firma_zamawiajaca = models.ForeignKey(Firma)
    kierowca_przewoz = models.ForeignKey(Kierowca)
    trasa_przewoz = models.ForeignKey(Trasa)
    towar = models.CharField(max_length=200)
    pojazd = models.CharField(max_length=200)
    fracht = models.FloatField()
    
    PLN = 'PLN'
    EUR = 'EUR'
    INNA = 'INNA'
    WALUTA_SYMBOL = (
       (PLN, 'PLN'),
       (EUR, 'EUR'),
       (INNA, 'INNA'),              
    )

    waluta_fracht = models.CharField(max_length=3, choices=WALUTA_SYMBOL, default = PLN) 
    uwagi_waluta = models.CharField(max_length=200)
    uwagi_fracht = models.CharField(max_length=200)
    odp_celna_export = models.CharField(max_length=50)
    odp_celna_przywozowa = models.CharField(max_length=50)
    uwagi = models.CharField(max_length=200)
    uwagi_opis = models.TextField()
    
    
    
    class Meta:
        verbose_name = u'zlecenie2'
        verbose_name_plural = u'zlecenia2'
        
    def __unicode__(self):
        return '%s %s' % (self.firma_realizujaca, self.firma_zamawiajaca)                



class WyslijSMS(models.Model):
    pass