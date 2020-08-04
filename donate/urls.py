from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("donate",views.donate,name="donate"),
    path("donateyou",views.donateyou,name="donateyou"),
    path("thedonate",views.thedonate,name="thedonate"),
    path("end1",views.end1,name="end1"),
    path("end2",views.end2,name="end2")
]