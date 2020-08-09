from django.urls import path
from . import views
from .views import create_new_post

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.create_user),
    path('dashboard', views.dashboard),
    path('create_new_post', views.create_new_post),
    path('user/<int:user_id>/profile', views.user_profile),
    path('logout', views.logout),

    # path('logout', views.logout)

    # path('dashboard', views.dashboard),
    # path('video/', views.video),
]
