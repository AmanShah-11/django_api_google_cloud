from django.urls import path
from rest_framework import routers

from . import views

urlpatterns = [
    path('object', views.object_detail),
    path('some_view', views.some_view)
]