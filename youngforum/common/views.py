from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from common.serializers import ArticleSerializer, SpecialColumnSerializer, TopicSerializer, CustomUserSerializer
from common.models import CustomUser, Article, SpecialColumn, Topic


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TopicSerializer


class SpecialColumnViewSet(ModelViewSet):
    queryset = SpecialColumn.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SpecialColumnSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ArticleSerializer


