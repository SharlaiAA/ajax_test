from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.authenticate_user, name='auth'),
    path('auth/check-username/', views.check_username),
    path('stav_like/', views.stav_like, name='stav_like'),
    path('stav_like/like/', views.like),
]
