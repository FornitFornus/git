# -*- coding: utf-8 -*-

from django.forms import forms, ModelForm, Textarea
from django.contrib import messages
from sms_controll.models import Kierowca


class AddKierowcaForm(forms.Form):
    
    class Meta:
        model = Kierowca
        fields = '__all__' #['pub_date', 'headline', 'content', 'reporter']
    

class KierowcaForm(ModelForm):
    class Meta:
        model = Kierowca
        fields = '__all__' #['pub_date', 'headline', 'content', 'reporter']
        
    def form_valid(self, form):
        model = Kierowca
        Kierowca = form.save(commit=False)
        Kierowca.save()
        messages.success(self.request, "Dodano nowego kierowce")
        return super(Kierowca, self).form_valid(form)
    
class SmsForm(forms.Form):
    class Meta:
        model = Kierowca
        fields = ['Imie', 'Nazwisko', 'Nr_tel_kom'] #['pub_date', 'headline', 'content', 'reporter'],