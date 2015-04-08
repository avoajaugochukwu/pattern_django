from django.conf.urls import patterns, include, url
from pattern import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),

    url(r'check_result/$', views.check_result, name="check_result"),
)
