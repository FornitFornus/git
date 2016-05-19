# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest 
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.template import RequestContext, Template, Context
from datetime import datetime
from django.utils import timezone
import time
import MySQLdb
from sms_controll.forms import KierowcaForm # AddKierowcaForm
from sms_controll.models import Kierowca
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView

# Create your views here.

def index(request):
    """Strona glowna aplikacji"""
    #return HttpResponse("Witaj w aplikacji Sms Controll System")
    assert isinstance(request, HttpRequest)
    return render(request, "sms_controll/index.html",
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(request, "sms_controll/home.html",
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )
    
#moje

def sms_list(request):
        
    db = MySQLdb.connect(user='firefly_4', db='firefly_4', passwd='ZgX3.14.2xY', host='sql.firefly.nazwa.pl')
    cursor = db.cursor()
     
    
    cursor.execute("SELECT * FROM inbox WHERE textdecoded = 'zaladowany'") #updatedindb, sendernumber, textdecoded FROM inbox")
    results = cursor.fetchall()

    data = []
    czas = []
    nr_tel = []
    status = []
    result_list = []


    for row in results:
        data.append(row[0].strftime("%Y-%m-%d %H:%M:%S"))
        nr_tel.append(row[3])
        status.append(row[8])
    
    x = 0
    for dane in data:
        result_list.insert(x,(x+1,data[x], nr_tel[x], status[x]))
        x += 1   
    
    db.close()
      

    """Renders the sms page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'sms_controll/sms_list.html',
        context_instance = RequestContext(request,
        {
            'title':'SMS - przychodzacy',
            'lista_sms':result_list,
            #'lista_data':data, 
            #'lista_nr_tel': nr_tel,                                    
            #'wiadomosci': wiadomosci
                    
        })
    )
        
    
#koniec moje 
  

def kierowca_new(request):
    form = KierowcaForm #AddKierowcaForm
    return render(request, 'sms_controll/kierowca.html', {'form': form})   


def loguj(request):
    """Logowanie uzytkownika"""
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostales zalogowany!")
            return redirect(reverse('sms_controll:home'))

    kontekst = {'form': AuthenticationForm()}
    return render(request, 'sms_controll/loguj.html', kontekst)


def wyloguj(request):
    """Wylogowanie uzytkownika"""
    logout(request)
    messages.info(request, "Zostales wylogowany!")
    return redirect(reverse('sms_controll:index'))

class UtworzKierowce(CreateView):
    model = Kierowca
    fields = '__all__'
    context_object_name = 'kierowcy'
    template_name = 'sms_controll/kierowca_form.html'
    success_url = '/home/kierowcy'
    
    def get_initial(self):
        initial = super(UtworzKierowce, self).get_initial()
        return initial

    def get_context_data(self, **kwargs):
        context = super(UtworzKierowce, self).get_context_data(**kwargs)
        context['kierowcy'] = Kierowca.objects.all()
        return context

    def form_valid(self, form):
        kierowca = form.save(commit=False)
        kierowca.save()
        messages.success(self.request, "Dodano nowego kierowce!")
        return super(UtworzKierowce, self).form_valid(form)
    
class EdytujKierowce(UpdateView):
    model = Kierowca
    from sms_controll.forms import KierowcaForm
    form_class = KierowcaForm
    context_object_name = 'kierowcy'
    template_name = 'sms_controll/kierowca_form.html'
    success_url = '/home/kierowcy'

    def get_context_data(self, **kwargs):
        context = super(EdytujKierowce, self).get_context_data(**kwargs)
        #context['kierowcy'] = Kierowca.objects.filter(kierowca=self.request.user)
        return context

    def get_object(self, queryset=None):
        kierowca = Kierowca.objects.get(id=self.kwargs['pk'])
        return kierowca    
    
class KierowcyList(ListView):
    model = Kierowca 
    #success_url = '/home/kierowcy'   

