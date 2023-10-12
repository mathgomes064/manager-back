from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users", views.RegisterView.as_view()),
    path("users/<uuid:user_id>", views.UserDetailView.as_view()),
    path("self-profile", views.UserProfileView.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path("refresh", jwt_views.TokenRefreshView.as_view()),
]