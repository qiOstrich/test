from django.urls import path

from li import views

urlpatterns=[
    path(r'xueting/', views.xueting, name='xueting'),

]