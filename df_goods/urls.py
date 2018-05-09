from django.conf.urls import url
import views
from views import MySearchView

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/$', views.detail),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^search/', MySearchView()),
]
