"""dataspeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from trade.views import getList,getAppjson,getLonlatjson,getLowspeedJson,getCell,map001,map002,herolist
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', getList),
    path('list/', getList),
    re_path(r'^$', getList),
    path('appjson/',getAppjson),
    path('lonlatjson/',getLonlatjson),
    path('lowspeed/',getLowspeedJson),
    path('getCell/',getCell),
    path('map001/', map001),
    #path('list/', getList),
    path('map002/', map002),
    path('herolist/', herolist)

]
