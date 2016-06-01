from django.conf.urls import url

from . import views

urlpatterns = [
	# /control
	url(r'^$', views.index, name='index'),

	# /control/lights
	url(r'^lights/$', views.lights, name='lights'),

	# /control/fanspeeds
	url(r'^fanspeeds/$', views.fanspeeds, name='fanspeeds'),

	# /control/5
	url(r'^(?P<toggler_id>[0-9]+)/$', views.detail, name='detail'),
	
	# /lights/3/toggle
	url(r'^(?P<toggler_id>[0-9]+)/toggle/$', views.toggle, name='toggle'),
]
