from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    is_user  = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)


