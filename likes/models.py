from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Like model
    Related to User instance via the 'owner' FK.
    Related to Post instance via the 'post' FK.
    Ordering set to '-created_on' so the newest post is shown first.
    Unique together set to ensure both fields related are unique
    to add a like.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f"{self.owner}, {self.post}"
