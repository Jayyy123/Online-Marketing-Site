from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from sklearn.feature_extraction import image
import uuid

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    profile_picture = models.ImageField(default = 'userr.jpeg')
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4 , primary_key= True, unique=True, editable=False)
    

    def __str__(self) -> str:
        return self.username
