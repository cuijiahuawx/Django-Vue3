from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

import jwt
import json

from Utils.utils import send_email
from .models import NewUser
from .serializers import RegisterSerializer


# 发送激活邮箱
class RegisterViewSet(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            user_data = serializers.data
            user = NewUser.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            abs_url = 'http://' + current_site + '/#verify/' + str(token)
            email_body = f"你好，{user.user_name}! 请点击下面的链接激活你的账号，否则你的账号将会不可用！！！\n" + abs_url
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': '验证账户'}
            send_email(data)
            return response.Response(serializers.data, status=status.HTTP_201_CREATED)
        return response.Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# 新用户邮箱确认逻辑
class VerifyEmailViewSet(APIView):

    def post(self, request):
        result = json.loads(request.body)
        token = result["token"]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        user = NewUser.objects.get(id=payload['user_id'])
        if not user.is_useful:
            user.is_useful = True
            user.save()
        resp = {'账户激活': 'success'}

        return HttpResponse(json.dumps(resp), content_type="application/json")

# 更改用户信息逻辑
class EditProfileViewSet(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        if request.method == 'POST':
            result = json.loads(request.body)
            token = result["token"]
            user_name = result["user_name"]
            avatar = result["avatar"]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            user = NewUser.objects.get(id=payload['user_id'])
            if user.is_useful:
                user.user_name = user_name
                user.avatar = avatar
                user.save()
                resp = {'更改信息': 'success'}
            else:
                resp = {'用户信息错误': '该用户没有权限'}
            return HttpResponse(json.dumps(resp), content_type="application/json")

# 发送重置密码邮箱
class ForgetPasswordViewSet(APIView):

    def post(self, request):
        if request.method == 'POST':
            result = json.loads(request.body)
            email = result["email"]
            user = NewUser.objects.get(email=email)
            if user.is_useful:
                token = RefreshToken.for_user(user).access_token
                current_site = get_current_site(request).domain
                abs_url = 'http://' + current_site + "/#resetPassword/" + str(token)
                email_body = f"你好，{user.user_name}! 请点击下面的链接重置你的密码\n" + abs_url
                data = {'email_body': email_body, 'to_email': user.email, 'email_subject': '重置密码'}
                send_email(data)
                resp = {'重置密码邮箱发送': 'success'}
            else:
                resp = {'用户信息错误': '该用户没有权限'}
            return HttpResponse(json.dumps(resp), content_type="application/json")

# 执行更改密码操作
class ChangePasswordViewSet(APIView):

    def post(self, request):
        result = json.loads(request.body)
        token = result["token"]
        new_password = result["password"]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        user = NewUser.objects.get(id=payload['user_id'])
        if user.is_useful:
            user.set_password(new_password)
            user.save()
            resp = {'重置密码': 'success'}
        else:
            resp = {'用户信息错误': '该用户没有权限'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

# 执行更改邮箱操作
class ChangeEmailViewSet(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        result = json.loads(request.body)
        token = result["token"]
        new_email = result["email"]
        password = result["password"]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        user = NewUser.objects.get(id=payload['user_id'])
        if user.is_useful:
            user = authenticate(request, username=user.email, password=password)
            if user is not None:
                user.email = new_email
                user.save()
                resp = {'更改邮箱成功': 'success'}
            else:
                resp = {'更改邮箱失败': 'failed'}
        else:
            resp = {'用户信息错误': '该用户没有权限'}
        return HttpResponse(json.dumps(resp), content_type="application/json")