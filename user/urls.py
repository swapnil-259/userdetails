from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.registeruser, name='registeruser'),
    path('login/',views.loginuser, name='loginuser' ),
    path('logoutuser/',views.logoutuser, name='logoutuser' ),
    path('createtask/',views.createtask, name='createtask'),
]