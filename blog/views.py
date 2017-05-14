from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

from .models import User
from .tasks import send_email_task
from ._forms import LoginForm, RegisterForm

import json


# Create your views here.
def login(r):
    if r.method == 'POST':
        loginForm = LoginForm(r.POST)
        if not loginForm.is_valid():
            return render()
            return HttpResponse(json.dumps({
                'status': -1,
                'message': '参数传递错误',
            }))

        user = User.objects.filter(
            account=loginForm['account'], password=loginForm['password'])
        if not user:
            return HttpResponse(json.dumps({
                'status': -2,
                'message': '账号密码错误',
            }))

        r.session['account'] = loginForm['account']
        return HttpResponse(json.dumps({
            'status': 0,
            'message': '登陆成功',
        }))
    if r.method == 'GET':
        return render(r, template_name='blog/login.html')


def logout(r):
    return HttpResponse("logout")


def register(r):
    if r.method == 'POST':
        # 获取参数
        registerForm = RegisterForm(r.POST)
        # 参数校验
        if not registerForm.is_valid():
            return HttpResponse(json.dumps({
                'status': -1,
                'message': '参数传递错误',
            }))

        if User.objects.filter(account=registerForm['account']):
            # return -2
            return HttpResponse(json.dumps({
                'status': -2,
                'message': '用户已存在',
            }))

        # 新增用户入数据库
        newUser = User(
            account=registerForm['account'], 
            password=registerForm['password'],
            nickname=registerForm['nickname'], 
            email=registerForm['email'],
            sex=registerForm['sex'], 
            age=registerForm['age'], 
            address=registerForm['address'],
            last_login_time=datetime.now(),
        )
        newUser.save()

        # 发送邮件
        subject = '请激活你的邮箱，完成注册'
        to = email
        login_url = 'http://localhost:8000/blog/login'
        verify_email_url = 'http://localhost:8000/blog/verify_email?' \
                           'account=%s' % account
        #TODO
        content = '''

        ''' % (nickname, login_url, verify_email_url)
        send_email_task.delay(subject, to, content)

        # return 1
        return HttpResponse(json.dumps({
            'status': 0,
            'message': '注册成功',
        }))

    if r.method == 'GET':
        return render(r, template_name='blog/register.html')


def change_password(r):
    return HttpResponse("change_password")


def add_article(r):
    return HttpResponse("add_article")


def delete_article(r):
    return HttpResponse("delete_article")


def view_article(r):
    return HttpResponse("view_article")


def edit_article(r):
    return HttpResponse("edit_password")


def add_article_type(r):
    return HttpResponse("add_article_type")


def delete_article_type(r):
    return HttpResponse("delete_article_type")


def view_article_type(r):
    return HttpResponse("view_article_type")


def edit_article_type(r):
    return HttpResponse("edit_password_type")


def add_comment(r):
    return HttpResponse("add_comment")


def delete_comment(r):
    return HttpResponse("delete_comment")


def view_comment(r):
    return HttpResponse("view_comment")
