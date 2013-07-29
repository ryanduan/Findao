#coding:utf8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import FindaoUserInfo, FindaoTag, FindaoShare
from forms import RegistUserForm, LoginUserForm
from db_control import oldUser, addUser, findUser, findShare
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
import hashlib

def dispshare(req):
    user = req.session.get('user', None)
    if user:
        shares = findShare(user)
        return render_to_response('dispshare.html',{'user':user, 'shares':shares})
    else:
	return HttpResponseRedirect('/index')

def logout(req):
    del req.session['user']
    return HttpResponseRedirect('/index/')

def login(req):
    if req.method == 'POST':
	uf = LoginUserForm(req.POST)
	if uf.is_valid():
	    username = uf.cleaned_data['username']
	    pw = uf.cleaned_data['password']
	    password = hashlib.md5(pw).hexdigest()
	    user = findUser(username, password)
	    if user:
		req.session['user'] = user
		return HttpResponseRedirect('/index/')
	    else:
		uf = LoginUserForm()
		errorinfo = '用户或密码不正确！'
	        return render_to_response('login.html',{'uf':uf, 'errorinfo':errorinfo})
    else:

        uf = LoginUserForm()
    return render_to_response('login.html',{'uf':uf})

def regist(req):
    if req.method == 'POST':
	uf = RegistUserForm(req.POST)
	if uf.is_valid():
	    username = uf.cleaned_data['username']
	    if oldUser(username):
		errorinfo = '用户已存在！'
                uf = RegistUserForm()
                return render_to_response('regist.html',{'uf':uf, 'errorinfo':errorinfo})
	    else:
	        p1 = uf.cleaned_data['password1']
	        p2 = uf.cleaned_data['password2']
	        if p1 == p2:
	            password = hashlib.md5(p1).hexdigest()
	            addUser(username, password)
	            return HttpResponseRedirect('/index/')
	        else:
	            errorinfo = '两次密码不匹配'
                    uf = RegistUserForm()
                return render_to_response('regist.html',{'uf':uf, 'errorinfo':errorinfo})
    else :
        uf = RegistUserForm()
    return render_to_response('regist.html',{'uf':uf})
	

def index(req):
    user = req.session.get('user', None)
    return render_to_response('index.html',{'user':user})
