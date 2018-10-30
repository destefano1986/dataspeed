from django.shortcuts import render
from .models import Trade,Test,Lowspeed,Lowspeedpre,SHMC
from django.http import HttpResponseRedirect,HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
import decimal
import json
import numpy as np

# Create your views here.
def getList(request):
    return render(request,"index.html")

def getAppjson(request):
    trades_list = Trade.objects.filter()
    resp=serializers.serialize("json", Trade.objects.all())
    print(resp)
    return HttpResponse(resp, content_type="application/json")

def getLonlatjson(request):
    test_list = Test.objects.filter(longitude__gte=118).values("longitude","latitude","downspeed")[0:10000]
    print(test_list)
    #resp=serializers.serialize("json", test_list)
    resp=json.dumps(list(test_list))
    print(resp)
    return HttpResponse(resp, content_type="application/json")


def getLowspeedJson(request):
    lowspeed = Lowspeed.objects.filter(lon__gte=118).values("lon", "lat")[0:1000]
    resp = json.dumps(list(lowspeed))
    print(resp)
    return HttpResponse(resp, content_type="application/json")

#前端dataTable兼容的JSON格式
def getCell(request):
    lowspeedpre = Lowspeedpre.objects.filter().values("cgi","userlabel","maintenancesubdept","region","longitude","latitude")
    resp2={"data":list(lowspeedpre)}
    resp = json.dumps(resp2)
    print(resp)
    return HttpResponse(resp, content_type="application/json")


def map001(request):
    map001 = SHMC.objects.filter().values()[0:1000]
    resp2={"data":list(map001)}
    resp = json.dumps(resp2)
    print(resp)
    return HttpResponse(resp, content_type="application/json")


def map002(request):
    map002 = SHMC.objects.filter(predict=1).values()[0:1000]
    resp2 = {"data": list(map002)}
    resp = json.dumps(resp2)
    print(resp)
    return HttpResponse(resp, content_type="application/json")
    #return render(request, "map002.html", {"map002": map002})


def herolist(request):
    herolist=SHMC.objects.all().order_by("Id").values()[0:1000]
    resp2 = {"data": list(herolist)}
    resp = json.dumps(resp2)
    print(resp)
    return HttpResponse(resp, content_type="application/json")
