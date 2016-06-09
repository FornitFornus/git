from django.conf.urls import patterns, url
from django.views.generic import ListView
from sms_controll import views
from sms_controll.models import Kierowca
from sms_controll.views import KierowcyList, EdytujKierowce, WyslijSMS
from django.views.generic.edit import DeleteView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loguj/$', views.loguj, name='loguj'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/sms_list_zaladowany$', views.sms_list_zaladowany, name='sms_list_zaladowany'),
    url(r'^home/sms_list_rozladowany$', views.sms_list_rozladowany, name='sms_list_rozladowany'),
    url(r'^home/sms_list_all$', views.sms_list_all, name='sms_list_all'),
    #url(r'^home/kierowca$', views.kierowca_new, name='kierowca_new'),
    url(r'^home/kierowca', views.UtworzKierowce.as_view()),
    url(r'^home/zlecenie', views.UtworzZlecenie.as_view()),##views.utworz_zlecenie, name='utworz_zlecenie'),##views.UtworzZlecenie.as_view()),
    url(r'^home/zlecenia', views.PokazZlecenia.as_view()),
    url(r'^home/edytuj/(?P<pk>\d+)/', views.EdytujKierowce.as_view(), name = 'edytuj'),
    url(r'^home/wyslij_sms/(?P<pk>\d+)/', WyslijSMS.as_view(model=Kierowca, template_name = 'sms_controll/sms_form.html', success_url = '/home/kierowcy'), name = 'wyslij_sms'),
    url(r'^home/usun/(?P<pk>\d+)/', DeleteView.as_view(model=Kierowca, template_name = 'sms_controll/kierowca_usun.html', success_url = '/home/kierowcy'), name = 'usun'),
    #url(r'^home/kierowcy$', ListView.as_view(model = Kierowca, context_object_name = 'kierowca'), name='kierowca_list'),
    url(r'^home/kierowcy/', KierowcyList.as_view()),
    url(r'^wyloguj/$', views.wyloguj, name='wyloguj'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout',{'next page': 'index',}, name='logout'),
]