#coding:utf8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import FindaoUserInfo, FindaoTag, FindaoShare
from forms import RegistUserForm, LoginUserForm, ShareForm, UserInfo
from db_control import oldUser, addUser, findUser, findShare, addShare, addUserInfo, allShare, getUserInfo, getShare, onlyShare, updateShare, deleteShare, trashShare, getTrash
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import hashlib

def userinfo(req):
    user = req.session.get('user',None)
    if user:
        userinfo = getUserInfo(user)
        return render_to_response('userinfo.html',{'user':user, 'userinfo':userinfo})

def createuserinfo(req):
    user = req.session.get('user',None)
    if req.method == 'POST':
	ui = UserInfo(req.POST)
	if ui.is_valid():
	    gender = 'm'
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
        shares = findShare(user)
        return render_to_response('dispuser.html',{'user':user, 'shares':shares})
    else:
	return HttpResponseRedirect('/index/')

def trashshare(req):
    user = req.session.get('user', None)
    share_id = req.session.get('share_id', None)
    trashShare(share_id)
    return HttpResponseRedirect('/dispshare/')

def deleteshare(req):
    user = req.session.get('user', None)
    share_id = req.session.get('share_id', None)
    deleteShare(share_id)
    return HttpResponseRedirect('/dispshare/')

def createshare(req):
    user = req.session.get('user', None)
    share_id = req.session.get('share_id', None)
    if req.method == 'POST':  
        title = req.POST.get('title')	
	codes = req.POST.get('content')
	tags = req.POST.get('tag')
	if share_id:
	    updateShare(share_id, title, codes, tags)
	    del req.session['share_id']
	else:
	    addShare(user, title, codes, tags)
	return HttpResponseRedirect('/dispshare/')
    else:
        if share_id:
	    print share_id
            share = onlyShare(share_id)
	else:
	    share = None
        return render_to_response('createshare.html',{'user':user, 'share':share})

def trash(req):
    user = req.session.get('user', None)
    shares = getTrash(user)
    return render_to_response('disptrash.html',{'shares':shares, 'user':user})
    

def dispsearched(req, share_id):
    user = req.session.get('user', None)
    if req.method == 'POST':
	sd = req.POST.get('search')
	req.session['sd'] = sd
	return HttpResponseRedirect('/dispsearch/')
    else:
        share_id = int(share_id)
	req.session['share_id'] = share_id
        share = onlyShare(share_id)
        return render_to_response('share.html',{'user':user, 'share':share}) 

def dispshare(req):
    user = req.session.get('user', None)
    if user:
        shares = findShare(user)
	print shares[0].codes
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
	    password = hashlib.sha256(pw).hexdigest()
	    user = findUser(username, password)
	    #user = authenticate(username=username, password=password)
	    if user:
		req.session['user'] = user
		return HttpResponseRedirect('/dispuser/')
	    else:
		uf = LoginUserForm()
		errorinfo = '* 用户或密码不正确！'
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
		errorinfo = '* 用户已存在！'
                uf = RegistUserForm()
                return render_to_response('regist.html',{'uf':uf, 'errorinfo':errorinfo})
	    else:
	        p1 = uf.cleaned_data['password1']
	        p2 = uf.cleaned_data['password2']
	        if p1 == p2:
	            password = hashlib.sha256(p1).hexdigest()
		    email = uf.cleaned_data['email']
	            addUser(username, password, email)
		    user = findUser(username, password)
		    if user:
		        req.session['user'] = user
	                return HttpResponseRedirect('/dispuser/')
	        else:
	            errorinfo = '* 两次密码不匹配'
                    uf = RegistUserForm()
                return render_to_response('regist.html',{'uf':uf, 'errorinfo':errorinfo})
    else :
        uf = RegistUserForm()
    return render_to_response('regist.html',{'uf':uf})
	

def index(req):
    user = req.session.get('user', None)
    if req.method == 'POST':
	sd = req.POST.get('search')
	req.session['sd'] = sd
	return HttpResponseRedirect('/dispsearch/')
    else:
	shares = None
    return render_to_response('index.html',{'user':user, 'shares':shares, 'shares':shares})

def dispsearch(req):
    user = req.session.get('user', None)
    if req.method == 'POST':
	sd = req.POST.get('search')
        if sd:
            shares = getShare(sd)
            if not shares:
        	shares = None
            return render_to_response('dispsearch.html',{'user':user, 'shares':shares})
	else:
	    return HttpResponseRedirect('/index/')
    else:
        sd = req.session.get('sd', None)
        if sd:
            shares = getShare(sd)
	    if not shares:
	        shares = None
            return render_to_response('dispsearch.html',{'user':user, 'shares':shares})
        else:
	    return HttpResponseRedirect('/index/')

def teaminfo(req):
    user = req.session.get('user', None)
    return render_to_response('teaminfo.html',{'user':user})
    
