from django.db import models
from django.contrib.auth.models import User
'''
How imagefield works:
    - work by conda python interpreter (ctrl + shift + p), choose conda base interpreter
    - if the above step done after the terminal opened then close it and open new terminal 
'''


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/%y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Post by {self.user.username}'
    class Meta:
        # Ordering the objects by this attribute
        ordering = ['-created_at']
