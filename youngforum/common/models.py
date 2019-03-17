from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    city = models.CharField(max_length=32, blank=True, null=True, verbose_name='城市')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='电话号码')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Topic(BaseModel):
    name = models.CharField(max_length=64, unique=True, verbose_name='话题名称')
    desc = models.TextField(verbose_name='描述')
    creator = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='创建人')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '话题'
        verbose_name_plural = verbose_name


class SpecialColumn(BaseModel):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='所属人')
    name = models.CharField(max_length=128, verbose_name='专栏名称')

    def __str__(self):
        return self.name + '-' + self.owner.username

    class Meta:
        verbose_name = '专栏'
        verbose_name_plural = verbose_name
    

class Article(BaseModel):
    title = models.CharField(max_length=128, verbose_name='文章标题')
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creator', verbose_name='创建人')
    on_topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, related_name='on_topic', verbose_name='所属话题')
    special_column = models.ForeignKey(SpecialColumn, on_delete=models.DO_NOTHING, related_name='special_column',
                                       blank=True, null=True, verbose_name='所属专栏')
    content = models.TextField(verbose_name='文章内容')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
