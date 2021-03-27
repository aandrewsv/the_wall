from django.urls import path
from . import views
                    
urlpatterns = [
    path('wall', views.wall),
    path('message-post', views.message_post),
    path('comment-post', views.comment_post),
    path('delete-message/<int:idn>', views.delete_message)
    ]
    