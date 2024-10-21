from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.main, name="main"),
    path("sign-in/", views.sign_in, name="sign_in"),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("login/", views.sign_in, name="login"),  # 로그인 URL 추가
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("my_page", views.my_page, name="my_page"),
    path("product_sale",views.product_sale,name="product_sale"),
]
