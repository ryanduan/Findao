#coding:utf8
from django import forms
from django.contrib.auth.models import User
class UserForm(forms.Form):
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
