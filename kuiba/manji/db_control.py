#coding:utf8
#from models import FindaoUserInfo, FindaoTag, FindaoShare
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from models import FindaoShare, FindaoUserInfo, FindaoTag
#class Auths(object):

#def __init__(self):
#    Group.objects.create(name='findaousers')
    

def addUserInfo(user, gender, birthday, address, firstname, lastname, email):
    FindaoUserInfo.objects.create(user=user, gender=gender, birthday=birthday,address=address)
    User.objects.filter(id=user.id).update(first_name=firstname, last_name=lastname, email=email)
#    User.objects.create(first_name=firstname, last_name=lastname, email=email)

def addShare(user, title, codes, tags):
    user.findaoshare_set.create(title=title, codes=codes)
    share = FindaoShare.objects.get(title=title, codes=codes)
#    for tag in tags:
#	try:
#	    rtag = FindaoTag.objects.get(tagname=tag)
#        except ObjectDoesNotExist:
#	    rtag = None
#	if rtag:
#	    share.tags.add(rtag)
#	else:
#            share.tags.create(tagname=tag)
    try:
        rtag = FindaoTag.objects.get(tagname=tags)
    except ObjectDoesNotExist:
        rtag = None
    if rtag:
        share.tags.add(rtag)
    else:
         share.tags.create(tagname=tags)
 
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

