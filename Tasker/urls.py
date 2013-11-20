from django.conf.urls import patterns, url

from Tasker import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^complete/(?P<id>\w+)$', views.complete, name='complete'),
    url(r'^edit/(?P<id>\w+)$', views.edit, name='edit'),
)
