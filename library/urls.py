from django.conf.urls import url
from .import views

url patterns =[
    url('^$',view.index, name ='index'),  # matching with an empty string 

]