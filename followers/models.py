from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model
    Related to User instance via the 'owner' and 'followed' FK.
    Ordering set to '-created_on' so the newest post is shown first.
    Unique together set to ensure both fields related are unique
    to add a Follower.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
        )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
