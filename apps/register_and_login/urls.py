from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('registermethod', views.registermethod),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    ]