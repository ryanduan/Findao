#coding:utf8
from django.db import models
from django.contrib.auth.models import User

class FindaoUserInfo(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=(('1','男'),('0','女')), default='1', blank=True)
    birthday = models.DateField(default='1990-01-01')
    address = models.CharField(max_length=40)
    ctime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username

class FindaoTag(models.Model):
    tagname = models.CharField(max_length=40)
    ctime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tagname

class FindaoShare(models.Model):
    tags = models.ManyToManyField(FindaoTag)
    whose = models.ForeignKey(User)
    title = models.CharField(max_length=60)
    codes = models.TextField()
    status = models.CharField(max_length=1, choices=(('0','draft'),('1','release'),('2','trash')), default='1', blank=True)
    ctime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    

