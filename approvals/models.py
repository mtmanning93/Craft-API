from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Approval(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'profile']

    def __str__(self):
        return f"{self.owner}, {self.profile}"
