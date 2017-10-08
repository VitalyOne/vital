from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main_page, name='main_page'),
    url(r'^detals/$', views.search_list, name='search_list'),
    url(r'^detal/(?P<pk>[0-9]+)/$', views.detal_detail, name='detal_detail'),
    url(r'^detal/new/$', views.detal_new, name='detal_new'),
    url(r'^detal/(?P<pk>[0-9]+)/edit/$', views.detal_edit, name='detal_edit'),
    url(r'^detal/search/$', views.search, name='search'),
    url(r'^detal/detal_delete/(?P<pk>[0-9]+)/$', views.detal_delete, name='detal_delete'),
    url(r'^detal/search_for_category/$', views.poisk_primenimost, name='poisk_primenimost'),
]

