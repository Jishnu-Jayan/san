from django.contrib import admin
from django.urls import path, include
from sanashapp1 import views
admin.site.site_header="Sanash Dashboard"
urlpatterns = [

    path('',views.home, name="home"),

]
