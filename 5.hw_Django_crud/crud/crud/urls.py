"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import blog.views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.main,name='main'),
    path('<str:id>', blog.views.detail, name="detail"), # 데이터 베이스의 id값, 수정 & 삭제 기능과 같은 패턴 
    path('write/create/', blog.views.create, name="create"),
    path('edit/<str:id>',blog.views.edit,name="edit"),
    #path('update/<str:id>',blog.views.update,name="update"),
    path('delete/<str:id>',blog.views.delete,name="delete"),
]
