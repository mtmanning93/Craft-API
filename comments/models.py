from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    Comment model, related to 'owner' via the User FK and
    'post' via the Post FK.
    Ordering set to '-created_on' to see the newest comment first,
    like a text conversation.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content
