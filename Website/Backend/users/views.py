from django.conf import settings
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

import jwt
import json

from Utils.utils import send_email, gen_code
from .models import User
from .serializers import RegisterSerializer

# 用户注册逻辑
class RegisterViewSet(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            resp = {'status': True}
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
            musicEmail = result["musicEmail"]
            musicID = result["musicID"]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            user = User.objects.get(id=payload['user_id'])
            user.user_name = user_name
            user.avatar = avatar
            user.musicEmail = musicEmail
            user.musicID = musicID
            user.save()
            resp = {'status': True}

            return HttpResponse(json.dumps(resp), content_type="application/json")

def send_code(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        code = gen_code()
        email_body = f"你好, 这是来自网站的的验证码，如果你没有注册的操作请忽略此邮件。您的验证码是：\n{code}"
        data = {'email_body': email_body, 'to_email': email, 'email_subject': '验证账户'}
        send_email(data)
        resp = {'code': code}
        return HttpResponse(json.dumps(resp), content_type="application/json")
