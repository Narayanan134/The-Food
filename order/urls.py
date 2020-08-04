from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("",views.order,name="order"),
    path("breakfast",views.breakfast,name="breakfast"),
    path("lunch",views.lunch,name="lunch"),
    path("dinner",views.dinner,name="dinner"),
    path("orderinfo",views.orderinfo,name="orderinfo"),
    path("orderinfob",views.orderinfob,name="orderinfob"),
    path("orderinfod",views.orderinfod,name="orderinfod"),
    path("bill",views.bill,name="bill")
]