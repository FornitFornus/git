from django.conf.urls import patterns, url
from django.views.generic import ListView
from sms_controll import views
from sms_controll.models import Kierowca
from sms_controll.views import KierowcyList, EdytujKierowce
from django.views.generic.edit import DeleteView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loguj/$', views.loguj, name='loguj'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/sms_list$', views.sms_list, name='sms_list'),
    #url(r'^home/kierowca$', views.kierowca_new, name='kierowca_new'),
    url(r'^home/kierowca', views.UtworzKierowce.as_view()),
    url(r'^home/edytuj/(?P<pk>\d+)/', views.EdytujKierowce.as_view(), name = 'edytuj'),
    url(r'^home/usun/(?P<pk>\d+)/', DeleteView.as_view(model=Kierowca, template_name = 'sms_controll/kierowca_usun.html', success_url = '/home/kierowcy'), name = 'usun'),
    #url(r'^home/kierowcy$', ListView.as_view(model = Kierowca, context_object_name = 'kierowca'), name='kierowca_list'),
    url(r'^home/kierowcy/', KierowcyList.as_view()),
    url(r'^wyloguj/$', views.wyloguj, name='wyloguj'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout',{'next page': 'index',}, name='logout'),
]