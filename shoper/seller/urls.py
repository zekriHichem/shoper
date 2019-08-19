from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('activate/<str:uidb64>/<str:token>/<int:id>',views.activate, name='activate'),
    path('login/', views.login_page,name = "login_page"),
    path('signup/', views.signup_page, name="signup_page"),

    path('dashboard/',views.dashboard,name="dashboard"),
    path('product/', views.products, name="products"),
    path('addP/', views.addProduct, name="addProduct"),
    path('singleP/', views.signleProduct, name="signleProduct"),
    path('buy/', views.buy, name="buy"),

]
