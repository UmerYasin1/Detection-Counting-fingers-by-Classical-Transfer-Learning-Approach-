from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('image_upload', index, name='image_upload'),
]