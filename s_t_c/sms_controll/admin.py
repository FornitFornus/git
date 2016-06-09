from django.contrib import admin
from sms_controll.models import Kierowca, Zlecenie, Zlecenie2, FirmaFaktura, Firma, Uzytkownik, Trasa #import modelu Kierowca


# Register your models here.
admin.site.register(FirmaFaktura)
admin.site.register(Zlecenie)
admin.site.register(Zlecenie2)
admin.site.register(Trasa)
admin.site.register(Kierowca)
admin.site.register(Firma)
admin.site.register(Uzytkownik)
