from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

import json

from .serializers import AccountSerializer


class LoginView(views.APIView):
    def post(self, request, format=None):
        b = request._request.body
        if isinstance(b, bytes):  # Python 3
            b = b.decode('utf-8')
        data = json.loads(b)
        username = data.get('username', None)
        password = data.get('password', None)

        account = authenticate(username=username, password=password)
        if account is None:
            u = User.objects.filter(email=username)
            if u:
                account = authenticate(username=u[0].username, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)
                serialized = AccountSerializer(account)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(selfself, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
