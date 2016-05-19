from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kierowca(models.Model):
    """Klasa reprezentujaca Kierowce w systemie"""
    Imie = models.CharField(max_length = 50)
    Nazwisko = models.CharField(max_length = 50)
    Prefix_tel = models.CharField(max_length = 3)
    Nr_tel_kom = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 50)
    Firma_id = models.IntegerField()
    Firma = models.CharField(max_length = 50)
    Nr_rej_sam = models.CharField(max_length = 10)
    Typ_sam = models.CharField(max_length = 200)
    Dane_sam = models.CharField(max_length = 200)
    
    class Meta:
        verbose_name = u'kierowca'
        verbose_name_plural = u'kierowcy'
        
    def __unicode__(self):
        return '%s %s %s' % (self.Imie, self.Nazwisko, self.Nr_tel_kom)