from django.conf.urls import url
from . import views



urlpatterns = [
    url('^$' ,views.index),
    url(r'^mycrude/$', views.mycrude_list),
    url(r'^mycrude/(?P<id>[0-9]+)$', views.mycrude_detail),
]
