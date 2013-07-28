#coding:utf8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import FindaoUserInfo, FindaoTag, FindaoShare
from forms import UserForm
from db_control import addUser
from django.contrib.auth.models import User

def regist(req):
    if req.method == 'POST':
	uf = UserForm(req.POST)
	if uf.is_valid():
	    username = uf.cleaned_data['username']
	    p1 = uf.cleaned_data['password1']
	    p2 = uf.cleaned_data['password2']
	    if p1 == p2:
		password = p1
		addUser(username, password)
	        return HttpResponseRedirect('/index/')
	    else:
		errorinfo = '两次密码不匹配'
                uf = UserForm()
            return render_to_response('regist.html',{'uf':uf, 'errorinfo':errorinfo})
    else :
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf})
	

def index(req):
    return render_to_response('index.html',{})
