from django.contrib import admin
from django.contrib.admin import ModelAdmin

from common.models import CustomUser, Topic, SpecialColumn, Article


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'city', 'is_active', 'is_superuser')


@admin.register(Topic)
class TopicAdmin(ModelAdmin):
    list_display = ('id', 'name', 'desc', 'creator', 'created_time')


@admin.register(SpecialColumn)
class SpecialColumnAdmin(ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_time')


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('id', 'title', 'creator', 'content', 'on_topic', 'special_column', 'created_time', 'update_time')