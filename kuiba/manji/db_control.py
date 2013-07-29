#coding:utf8
#from models import FindaoUserInfo, FindaoTag, FindaoShare
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from models import FindaoShare, FindaoUserInfo, FindaoTag
#class Auths(object):

#def __init__(self):
#    Group.objects.create(name='findaousers')
    
def getTags(share):
    tags = share.tags.all()
    return tags

def oldUser(username):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        user = None
    return user
    

def addUser(username, password):
    User.objects.create(username=username, password=password)
        
#    user = User.objects.get(username=username, password=password)
#    group = Group.objects.get(name='findaousers')
#    print group
#    print group.id
#    Group.objects.create(user_id=user.id)

def findUser(username, password):
    try:
        user = User.objects.get(username=username, password=password)
    except ObjectDoesNotExist:
        user = None
    return user

def findShare(username):
    shares = FindaoShare.objects.filter(whose__exact=username)
    return shares

