#coding:utf8
from django import forms
from django.contrib.auth.models import User
from models import FindaoShare, FindaoTag, FindaoUserInfo

class UserInfo(forms.ModelForm):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    email = forms.CharField(max_length=30)
    class Meta:
        model = FindaoUserInfo
        fields = ('gender', 'birthday', 'address')

class ShareForm(forms.ModelForm):
    tags = forms.CharField(max_length=20)
    class Meta:
        model = FindaoShare
	fields = ('title', 'codes')

class RegistUserForm(forms.Form):
    username = forms.CharField(
        label='用户名', 
	min_length=5, 
	max_length=30,
	)
    password1 = forms.CharField(
        widget=forms.PasswordInput, 
	label='密码', 
	min_length=8, 
	max_length=40,
	)
    password2 = forms.CharField(
        widget=forms.PasswordInput, 
	label='确认密码', 
	min_length=8, 
	max_length=40,
	)

class LoginUserForm(forms.Form):
    username = forms.CharField(
        label='用户名', 
	min_length=5, 
	max_length=30,
	)
    password = forms.CharField(
        widget=forms.PasswordInput, 
	label='密码', 
	min_length=8, 
	max_length=40,
	)
