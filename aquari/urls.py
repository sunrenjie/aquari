"""aquari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from rest_framework_nested import routers

from .views import IndexView

from school.views import CategoryAppsViewSet, AppViewSet
from authentication.views import LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'apps', AppViewSet)

from django.conf.urls import patterns, url, include

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url('^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url('^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url('^.*$', IndexView.as_view(), name='index'),
]
