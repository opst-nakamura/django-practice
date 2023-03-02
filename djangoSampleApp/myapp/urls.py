# from django.urls import path
# from . import views
 
# urlpatterns = [
#     path('templates/', views.index_template, name='index_template'),
# ]

from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
]