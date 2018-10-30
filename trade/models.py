from django.db import models

# Create your models here.
class Trade(models.Model):
    app_type=models.BigIntegerField(verbose_name="APP类型",primary_key="True")
    appName=models.CharField(max_length=50,verbose_name="APP名字")
    usernum=models.CharField(max_length=20,verbose_name="用户数")
    ULSpeed=models.DecimalField(max_digits=8, decimal_places=2,verbose_name="上行速率")
    DLSpeed=models.DecimalField(max_digits=8, decimal_places=2,verbose_name="下行速率")
    bigdataDLSpeed=models.DecimalField(max_digits=8, decimal_places=2,verbose_name="大包下载速率")

    class Meta:
        verbose_name="app表"
        db_table="app"


class Test(models.Model):
    cgi=models.CharField(max_length=20,verbose_name="APP名字",primary_key="True")
    downspeed=models.DecimalField(max_digits=8,decimal_places=2,verbose_name="下载速率")
    bigdownspeed=models.DecimalField(max_digits=8,decimal_places=2,verbose_name="大包下载速率")
    longitude=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="经度")
    latitude=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="维度")
    class Meta:
        verbose_name="test表"
        db_table="test"

class Lowspeed(models.Model):
    id = models.BigIntegerField(verbose_name="ID", primary_key="True")
    lon=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="经度")
    lat=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="维度")
    class Meta:
        verbose_name="lowspeed表"
        db_table="lowspeed"



class Lowspeedpre(models.Model):
    cgi = models.CharField(max_length=20, verbose_name="CGI", primary_key="True")
    LOWSPEED=models.BigIntegerField(verbose_name="LOWSPEED")
    downspeed=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="下载速率")
    SUC_CALL_RATE=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="无线接通率")
    PRB_UTILIZE_RATE=models.DecimalField(max_digits=8, decimal_places=6, verbose_name="prb利用率")
    SUC_CALL_RATE_QCI1=models.DecimalField(max_digits=8, decimal_places=6, verbose_name="volte无线接通率")
    mr=models.DecimalField(max_digits=8, decimal_places=6, verbose_name="mr覆盖率")
    cover_type=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="覆盖类型")
    erabnbrmaxestab1=models.BigIntegerField(verbose_name="qci1最大erab数")
    longitude=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="经度")
    latitude=models.DecimalField(max_digits=8,decimal_places=6,verbose_name="维度")
    userlabel=models.CharField(max_length=20, verbose_name="userlabel")
    maintenancesubdept=models.CharField(max_length=20, verbose_name="维护部门")
    region=models.CharField(max_length=20, verbose_name="行政区域")
    Y_pre=models.CharField(max_length=20, verbose_name="预测值")
    class Meta:
        verbose_name="lowspeed预测表"
        db_table="lowspeedpre"


class SHMC(models.Model):
    Id = models.BigIntegerField(primary_key=True, default=0, verbose_name=u"id")
    lon_lat_tag = models.CharField(max_length=20, unique=True, verbose_name=u"lon_lat_tag")
    ant_height = models.CharField(max_length=20, unique=True,verbose_name=u"ant_height")
    rs = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="rs")
    rrc_conn_times = models.DecimalField(max_digits=20,decimal_places=2, verbose_name=u"rrc_conn_times")
    prb_usage = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"prb_usage")
    senario = models.CharField(max_length=20, unique=True, verbose_name=u"senario")
    mr_cov = models.CharField(max_length=20, unique=True, verbose_name=u"mr_cov")
    high_inf_ratio = models.CharField(max_length=20, unique=True, verbose_name=u"high_inf_ratio")
    ue_power = models.CharField(max_length=20, unique=True, verbose_name=u"ue_power")
    flow = models.CharField(max_length=20, unique=True, verbose_name=u"flow")
    site_type = models.CharField(max_length=20, unique=True, verbose_name=u"site_type")
    ring_info= models.CharField(max_length=20, unique=True, verbose_name=u" ring_info")
    reason = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="reason")
    lon=models.DecimalField(max_digits=20, decimal_places=2, verbose_name="lon")
    lat = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="lat")
    predict = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="predict")
    class Meta:
        verbose_name= u"SHMC"
        db_table = u"trade"