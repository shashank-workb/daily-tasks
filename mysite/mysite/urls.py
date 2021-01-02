"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

#REST-API
from django.conf.urls import include
from rest_framework import routers # help in form urls for api
from myapp.views import taskviewset

router = routers.DefaultRouter()
router.register(r'taskbydate', taskviewset)

urlpatterns = [
    path('rest/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.update, name='update'),
    path('deleteall/', views.deleteall, name='deleteall'),
    path('cbvlist/', views.Tasklistview.as_view(), name='cbvlist'),
    path('cbvdetail/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),
]
