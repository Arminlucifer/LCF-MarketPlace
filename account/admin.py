from django.contrib import admin
from .models import User
from base.models import Category, Product, Comment,CommentLike



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'role')

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(CommentLike)
