from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("orderinfo",views.orderinfo,name="orderinfo"),
    path("bill",views.bill,name="bill")
]