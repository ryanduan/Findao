#coding:utf8
#from models import FindaoUserInfo, FindaoTag, FindaoShare
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def addUser(username, password):
    User.objects.create(username=username, password=password)

def findUser(username, password):
    try:
        user = User.objects.get(username=username, password=password)
    except ObjectDoesNotExist:
        user = None
    return user
