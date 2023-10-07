from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    """
    Company model, related to 'owner' via the User FK.
    Ordering set to 'name' to enable easy searching
    when in list view.
    """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
