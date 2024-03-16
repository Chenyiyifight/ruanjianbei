from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from user_info.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate


class ApiUser(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(methods=['post'], detail=False)
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            result = {
                "code": -1,
                "msg": "用户名或密码不能为空",
                "body": ""
            }
            return Response(result)
        user = authenticate(username=username, password=password)

        # user = User.objects.filter(username=username).first()

        if user is not None and check_password(password, user.password):
            result = {
                "code": 200,
                "msg": "登录成功",
                "body": ""
            }
        else:
            result = {
                "code": -1,
                "msg": "登录失败，用户名或密码错误",
                "body": ""
            }

        return Response(result)

    @action(methods=['post'], detail=False)
    def register(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            result = {
                "code": -1,
                "msg": "用户名或密码不能为空",
                "body": ""
            }
            return Response(result)

        hashed_password = make_password(password)  # 对密码进行哈希加密
        User.objects.create(username=username, password=hashed_password)
        result = {
            "code": 200,
            "msg": "注册成功",
            "body": ""
        }

        return Response(result)
