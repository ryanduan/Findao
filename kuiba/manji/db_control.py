#coding:utf8
#from models import FindaoUserInfo, FindaoTag, FindaoShare
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from models import FindaoShare, FindaoUserInfo, FindaoTag
#class Auths(object):

#def __init__(self):
#    Group.objects.create(name='findaousers')
    
def getUserInfo(user):
    userinfo = FindaoUserInfo.objects.get(user = user)
    return userinfo
    
def onlyShare(id):
    share = FindaoShare.objects.get(id=id)
    return share

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
    

def addUser(username, password, email):
    User.objects.create(username=username, password=password, email=email)
        
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

def getShare(search):
    shares = []
    sh1 = FindaoShare.objects.filter(title__contains=search)
    sh2 = FindaoShare.objects.filter(codes__contains=search)
    tag = FindaoTag.objects.filter(tagname__contains=search)
    if tag:
	for t in tag:
	    sh3 = t.findaoshare_set.all()
	    for sh in sh3:
	        if sh not in shares:
	            shares.append(sh)
    if sh1:
	for sh in sh1:
	    if sh not in shares:
	        shares.append(sh)
    if sh2:
	for sh in sh2:
	    if sh not in shares:
	        shares.append(sh)
    return shares


def allShare():
    shares = FindaoShare.objects.all()
    return shares
