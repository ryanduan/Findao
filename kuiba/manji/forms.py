#coding:utf8
from django import forms
from django.contrib.auth.models import User
from models import FindaoShare, FindaoTag, FindaoUserInfo

class UserInfo(forms.Form):
    first_name = forms.CharField(max_length=10, label="姓:")
    last_name = forms.CharField(max_length=10, label="名:")
#    gender = forms.CharField(label='性别', ChoiceField=(('m','男'),('f','女')))
    birthday = forms.DateField(label='出生日期')
    address = forms.CharField(label='地址', max_length=40)
    email = forms.CharField(max_length=30, label="邮箱")
#    class Meta:
#        model = FindaoUserInfo
#        fields = ('gender', 'birthday', 'address')
#	widgets = {
#	    'gender':forms.CharField(max_length=1, choices=(('m','男'),('f','女'))),
#	    'birthday':forms.DateField(),
#	    'address':forms.CharField(max_length=40),
#	    }

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
    email = forms.CharField(
        max_length=30,
	label='邮箱',
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
