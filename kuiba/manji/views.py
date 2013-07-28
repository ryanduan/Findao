from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import FindaoUserInfo, FindaoTag, FindaoShare
from django.contrib.auth.models import User

def index(req):
    userinfo = User.objects.get(username='ryan')
    usershare = FindaoShare.objects.get(whose=userinfo)
    return render_to_response('index.html',{'userinfo':userinfo, 'usershare':usershare})
