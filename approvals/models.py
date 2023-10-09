from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Approval(models.Model):
    """
    Approval model.
    Related to User instance via 'owner and 'profile' FK.
    Ordering set to '-created_on' to see the newest Approval first.
    Unique together set to ensure both fields related are unique
    to add an Approval.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'profile']

    def __str__(self):
        return f"{self.owner}, {self.profile}"
