from django.db import models
from django.conf import settings

class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Customer'),
        (1, 'Admin'),
    )
    user = models.OneToOneField (
                                 settings.AUTH_USER_MODEL,\
                                 primary_key=True,\
                                 on_delete=models.CASCADE
                                )

    user_type = models.IntegerField(default=0, null=True, choices=USER_TYPES)
    name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return "{}".format(self.user.username)
    class Meta:
        abstract = True

class AdminProfile(models.Model):
    admin_email = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        abstract = True


class CustomerProfile(models.Model):
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    class Meta:
        abstract = True


class Profile(BaseProfile, AdminProfile, CustomerProfile):
    pass
