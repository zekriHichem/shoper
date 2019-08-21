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
    path('product/<int:id>', views.sup_product, name="sup_product"),

    path('addP/', views.addProduct, name="addProduct"),
    path('singleP/<int:id>', views.signleProduct, name="signleProduct"),
    path('buy/', views.buy, name="buy"),
    path('recive_buy/', views.recive_buy, name="recive_buy"),
    path('recive_cart/', views.recive_cart, name="recive_cart"),

    path("profile/",views.profile,name="profile"),
    path("contact_us/", views.contact_us, name="contact_us")

]
