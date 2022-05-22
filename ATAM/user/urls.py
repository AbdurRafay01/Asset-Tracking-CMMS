from knox import views as knox_views
from .views import ChangePasswordView, LoginAPI ,RegisterAPI,user_login,user_logout, user_register

from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='api_register'),
    path('api/login/', LoginAPI.as_view(), name='api_login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='api_logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='api_logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('login/',user_login,name="login"),
    path('register/',user_register,name="register"),
    path('logout/',user_logout,name="logout")
]