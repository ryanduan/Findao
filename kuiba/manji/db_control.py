#from models import FindaoUserInfo, FindaoTag, FindaoShare
from django.contrib.auth.models import User

def addUser(username,password):
    User.objects.create(username=username, password=password)

