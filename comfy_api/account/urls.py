from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("", views.UserCreateView.as_view(), name="users"),
    path("login/", views.LoginUserView.as_view(), name="login user"),
]