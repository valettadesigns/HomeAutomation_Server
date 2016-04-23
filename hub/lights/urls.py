from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# /lights/5
	url(r'^(?P<light_id>[0-9]+)/$', views.detail, name='detail'),
	# /lights/3/toggle
	url(r'^(?P<light_id>[0-9]+)/toggle/$', views.toggle, name='toggle'),
]
