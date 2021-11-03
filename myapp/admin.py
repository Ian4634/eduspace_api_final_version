from django.contrib import admin
from .models import Category, Video
# Register your models here.

admin.site.register(Video)
admin.site.register(Category)