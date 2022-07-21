from django.urls import path
from . import views
# from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("", views.UserCreateView.as_view(), name="users"),
    path("<int:pk>", views.UserDetailView.as_view(), name="user detail"),

    path("login/", views.LoginUserView.as_view(), name="login user"),
]