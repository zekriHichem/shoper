from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('login/', views.login_page,name = "login_page"),
    path('signup/', views.signup_page, name="signup_page"),

]
