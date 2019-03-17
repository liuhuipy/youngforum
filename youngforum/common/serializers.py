# -*- coding:utf-8 -*-

from rest_framework import serializers
from common.models import Article, CustomUser, Topic, SpecialColumn


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone', 'city', 'is_active', 'is_superuser')


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'name', 'desc', 'created_time')


class SpecialColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialColumn
        fields = ('id', 'name', 'owner', 'created_time')


class ArticleSerializer(serializers.ModelSerializer):
    # creator = serializers.CharField(source='creator.username')
    # on_topic = serializers.CharField(source='on_topic.name')

    class Meta:
        model = Article
        fields = ('id', 'title', 'creator', 'on_topic', 'special_column', 'content', 'created_time')