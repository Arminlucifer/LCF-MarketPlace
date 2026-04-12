import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)

    avatar = models.ImageField(default='default.png', null=True)


    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    ROLE_CHOICES = (
        ("admin","Admin"),
        ("seller","Seller"),
        ("Customer","Customer")
    )

    role = models.CharField(choices=ROLE_CHOICES, default='Customer', max_length=10)

    referral_id = models.UUIDField(blank=True, null=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'username']



    def __str__(self):
        return self.username

