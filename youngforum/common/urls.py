# -*- coding:utf-8 -*-
from django.urls import path
from rest_framework import routers

from common.views import ArticleViewSet, TopicViewSet, SpecialColumnViewSet, CustomUserViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'user', CustomUserViewSet, 'user')
router.register(r'topic', TopicViewSet, 'topic')
router.register(r'special-column', SpecialColumnViewSet, 'special-column')
router.register(r'article', ArticleViewSet, 'article')


urlpatterns = router.urls
