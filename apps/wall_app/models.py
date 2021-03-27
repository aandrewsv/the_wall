from django.db import models
from datetime import *
from ..register_and_login.models import *

# Create your models here.

class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="message_users_id", on_delete=models.CASCADE)
    message = models.TextField(max_length=140)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message_id = models.ForeignKey(Message, related_name="message_id", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name="comment_users_id", on_delete=models.CASCADE)
    comment = models.TextField(max_length=140)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

