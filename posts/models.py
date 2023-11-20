from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner' via the User FK.
    Image default set to the site logo, if no image added.
    Ordering set to '-created_on' so the newest post
    is shown first.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../logo_nobg_aac6d9.png', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.id} {self.title}"
