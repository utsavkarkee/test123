from django.conf.urls import patterns,include,url

from messAPP import views

urlpatterns= patterns('',
                      url(r'^$',views.form,name='form'),
                      url(r'^login/$',views.login,name='login'),
                      url(r'^dbRequest/$', views.dbRequest, name='dbRequest'),

                        );
