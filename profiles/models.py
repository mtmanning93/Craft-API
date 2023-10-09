from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from companies.models import Company


class Profile(models.Model):
    """
    Profile model, related to 'owner' via the User FK.
    Image set to a default user icon, for new users.
    Ordering set to 'name' to enable easy searching
    when in list view.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    job = models.CharField(max_length=100, blank=True)
    employer = models.ForeignKey(
        Company, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='current_employee'
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../user_defualt_icon_d7nivg.png'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Creates the profile instance when a user is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
