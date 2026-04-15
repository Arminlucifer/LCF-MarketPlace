import uuid

from django.db import models
from  account.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(default='category_default.png', null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, )
    caption = models.TextField(max_length=100, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='productlikes', blank=True)
    is_approved = models.BooleanField(default=False)
    image = models.ImageField(default='product_default.png', null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-added']

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='commentlikes', blank=True)

    def __str__(self):
        return self.body[0:50]

    def total_likes(self):
        return self.likes.count()
