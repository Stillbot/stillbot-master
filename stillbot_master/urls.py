from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from webapp.models import Thermistor, Temperature
from webapp.views import *
from django.views.generic import TemplateView
from rest_framework import routers
from django.contrib import admin
admin.autodiscover()


# Routers provide an easy way of automatically determing the URL conf.
#
# Issue: Could not resolve URL for hyperlinked relationship using view name "permission-detail"
# See:   https://github.com/tomchristie/django-rest-framework/issues/1249
# 
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'thermistors', ThermistorViewSet)
router.register(r'temperatures', TemperatureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stillbot_master.views.home', name='home'),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^dashboard', TemplateView.as_view(template_name='dashboard.html')),
    #url(r'^grappelli', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
