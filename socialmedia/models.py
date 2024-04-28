from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    backgroundImage = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)
    qoute = models.CharField(max_length=255, blank=True, default='not qoute')
    def __str__(self):
        return self.user.username

class Post(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete = models.CASCADE, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/%Y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = likes = models.ManyToManyField(UserProfile, related_name='liked_posts', blank=True)
    def __str__(self):
        return f'Post by {self.user_profile.user.username}'
    class Meta:
        ordering = ['-created_at']
