from django.shortcuts import render

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import App
from .serializers import AppSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.order_by('slug')
    serializer_class = AppSerializer

    def get_permissions(self):
        # if self.request.method in permissions.SAFE_METHODS:
        return (permissions.AllowAny(),)


class CategoryAppsViewSet(viewsets.ViewSet):
    queryset = App.objects.select_related('category').all()
    serializer_class = AppSerializer

    def list(self, request, category=None):
        queryset = self.queryset.filter(category=category)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
