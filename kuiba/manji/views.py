#coding:utf8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import FindaoUserInfo, FindaoTag, FindaoShare
from forms import RegistUserForm, LoginUserForm, ShareForm, UserInfo
from db_control import oldUser, addUser, findUser, findShare, addShare, addUserInfo, allShare, getUserInfo
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
import hashlib

def userinfo(req):
    user = req.session.get('user',None)
    if user:
	print user.username
	print user.email
        userinfo = getUserInfo(user)
        return render_to_response('userinfo.html',{'user':user, 'userinfo':userinfo})

def createuserinfo(req):
    user = req.session.get('user',None)
    if req.method == 'POST':
	ui = UserInfo(req.POST)
	if ui.is_valid():
	    gender = ui.cleaned_data['gender']
	    birthday = ui.cleaned_data['birthday']
	    address = ui.cleaned_data['address']
	    firstname = ui.cleaned_data['first_name']
	    lastname = ui.cleaned_data['last_name']
	    email = ui.cleaned_data['email']
	    addUserInfo(user, gender, birthday, address, firstname, lastname, email)
	    return render_to_response('dispuser.html',{'user':user})
	
    else:
	ui = UserInfo()
	return render_to_response('createuserinfo.html',{'user':user, 'ui':ui})

def dispuser(req):
    user = req.session.get('user',None)
    if user:
        return render_to_response('dispuser.html',{'user':user})
    else:
	return HttpResponseRedirect('/index/')

def createshare(req):
    user = req.session.get('user', None)
    if req.method == 'POST':  
	sf = ShareForm(req.POST)
	if sf.is_valid():
	    title = sf.cleaned_data['title']
	    codes = sf.cleaned_data['codes']
	    tags = sf.cleaned_data['tags']
	    addShare(user, title, codes, tags)
	return HttpResponseRedirect('/dispshare/')
    else:
	sf = ShareForm()
        return render_to_response('createshare.html',{'user':user, 'sf':sf})

def dispshare(req):
    user = req.session.get('user', None)
    if user:
        shares = findShare(user)
        return render_to_response('dispshare.html',{'user':user, 'shares':shares})
    else:
	return HttpResponseRedirect('/index/')

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
		return HttpResponseRedirect('/dispuser/')
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
		    user = findUser(username, password)
		    if user:
		        req.session['user'] = user
	                return HttpResponseRedirect('/createuserinfo/')
	        else:
	            errorinfo = '两次密码不匹配'
                    uf = RegistUserForm()
                return render_to_response('regist.html',{'uf':uf, 'errorinfo':errorinfo})
    else :
        uf = RegistUserForm()
    return render_to_response('regist.html',{'uf':uf})
	

def index(req):
    user = req.session.get('user', None)
    if req.method == 'POST':
	sd = req.POST.get('search')
	return HttpResponseRedirect('/dispsearch/')
    else:
	shares = None
    return render_to_response('index.html',{'user':user, 'shares':shares, 'shares':shares})

def dispsearch(req):
    user = req.session.get('user', None)
    shares = allShare()
    return render_to_response('dispsearch.html',{'user':user, 'shares':shares})

