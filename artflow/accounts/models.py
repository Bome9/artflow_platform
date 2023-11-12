from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    coverimg = models.ImageField(upload_to='cover_images', default='cover_default.png')
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username