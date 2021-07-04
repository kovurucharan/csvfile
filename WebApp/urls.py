from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #path('',views.file),
    path('th/',views.thanks),
    path('upload/',views.simple_upload),

]