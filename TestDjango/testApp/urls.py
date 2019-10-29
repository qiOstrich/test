from django.urls import path

from testApp import views

urlpatterns = [
    path(r'index/', views.index, name='index', ),
]
