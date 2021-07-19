from django.contrib import admin
from django.urls import path
from abishek_app import views
  
urlpatterns = [
    path('camera/',views.home_view),
    path('',views.check),
    path('external/',views.external)
]


