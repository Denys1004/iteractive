from django.urls import path
from . import views
from .views import create_new_image_post

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.create_user),
    path('dashboard', views.dashboard),
    path('create_new_text_post', views.create_new_text_post),
    path('create_new_image_post', views.create_new_image_post),
    path('create_new_video_post', views.create_new_video_post),
    path('user/<int:user_id>/profile', views.user_profile),


    path('add_comment/post/<int:post_id>', views.add_comment),

    path('post_comment', views.post_comment_with_ajax),


    path('logout', views.logout)
]
