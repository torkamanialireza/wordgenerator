from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [

    url(r'^$', views.index),
    # url(r'^generate$', views.generate),
    url(r'^reset$', views.reset)




       # This line has changed! Notice that urlpatterns is a list, the comma is in
]                            # anticipation of all the routes that will be coming soon
