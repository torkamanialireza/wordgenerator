from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^creat', views.creat), # This line has changed! Notice that urlpatterns is a list, the comma is in
]
