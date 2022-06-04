from django.contrib import admin
from .models import Project

# Register your models here.
from blog.models import Category, Post, Comment

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)