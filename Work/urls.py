# coding:utf-8
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin

from . import views

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=[
    url(r'^$', views.index, name='index'),
    url(r'^route', views.RouteHandler.as_view()),
    url(r'^user', views.UserHandler.as_view()),
    url(r'^image', views.ImageHandler.as_view()),
    url(r'^audio', views.RadioHandler.as_view()),
]

admin.site.site_header='富阳市电力局导航管理系统'
admin.site.site_title = '数据管理'
