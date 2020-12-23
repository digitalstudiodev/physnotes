from django.urls import path, include
from .views import (register, profile, profile_update, login_view, logout_view, base)

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile-update/', profile_update, name='profile_update'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('base/', base, name='base'),
]