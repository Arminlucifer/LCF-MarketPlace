from django.forms import ModelForm
from . models import Product, Comment

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category' ,'name', 'caption', 'price', 'image']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']