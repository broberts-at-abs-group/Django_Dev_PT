from django.conf.urls import url
from pemex_app import views

urlpatterns = [
        url(r'^home/$', views.home, name='home'),

        #url(r'^add_evidence/$', views.add_evidence, name='add_evidence'),

        url(r'^upload/$', views.model_form_upload, name='upload'),
        url(r'^fileretrieve/$', views.file_retrieve, name='fileretrieve'),
        url(r'^assign/$', views.assign, name='assign'),


        url(r'^q_all/$', views.queue_all, {'prefilter' : 'none'}, name='q_all'),
        url(r'^q_user/$', views.queue_all, {'prefilter' : 'user'}, name='q_user'),
        url(r'^q_team/$', views.queue_all, {'prefilter' : 'users team group'}, name='q_team'),
        url(r'^q_rev/$', views.queue_all, {'prefilter' : 'reviewer'}, name='q_rev'),
        url(r'^q_trans/$', views.queue_translator, name='q_trans'),

        url(r'^update/(?P<pk>\d+)/$', views.compliance_update, name='compliance_update'),

        ]
