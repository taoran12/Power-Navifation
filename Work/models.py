# encoding=utf-8

import sys
reload(sys)

from django.db import models
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from utils import *
import datetime
import xlrd
import os
from django.conf import settings

import xlwt

class User(models.Model):
    _id = models.IntegerField(primary_key=True)
    unit = models.CharField(max_length=255,verbose_name='单位',null=True)
    power_unit = models.CharField(max_length=255,verbose_name="供电所",null=True)
    district_number = models.CharField(max_length=255,verbose_name="台区编码",null=True)
    district_name = models.CharField(max_length=255,verbose_name="台区名称",null=True)
    user_id = models.CharField(max_length=10,verbose_name="户号",unique=True)
    user_name = models.CharField(max_length=50,verbose_name="户名",null=True)
    user_addr = models.CharField(max_length=50,verbose_name="用户地址",null=True)
    addr_lng = models.DecimalField(max_digits=10,decimal_places=6,verbose_name="经度",null=True,default=None)
    addr_lat = models.DecimalField(max_digits=10,decimal_places=6,verbose_name="纬度",null=True,default=None)
    terminal_number = models.CharField(max_length=22,verbose_name="终端局号",null=True)
    meter_number = models.CharField(max_length=22,verbose_name="表计局号",null=True)
    logical_addr = models.CharField(max_length=22,verbose_name="逻辑地址",null=True)
    record_date = models.DateTimeField(verbose_name="用户信息在本地修改的时间",null=True)
    update_date = models.DateTimeField(verbose_name="用户信息上传到服务器的时间",null=True)
    collection_unit = models.CharField(max_length=255,verbose_name="采集单位",null=True)
    kva = models.IntegerField(verbose_name="受电容量(kva)",null=True)
    meter_type = models.CharField(max_length=30,verbose_name="表计规约",null=True)
    tel_addr = models.CharField(max_length=20,verbose_name="通信地址",null=True)
    manufacturer = models.CharField(max_length=255,verbose_name="生产厂家",null=True)
    line_type = models.CharField(max_length=255,verbose_name="接线方式",null=True,default=None)
    metering_method = models.CharField(max_length=50,verbose_name="计量方式",null=True)
    remark1 = models.CharField(max_length=255,verbose_name="remark",null=True)
    #ima = models.CharField(max_length=255, verbose_name="image", null=True)
    #photo = models.ImageField(upload_to='photos',null=True)
    class Meta:
        db_table = 'user'
        verbose_name = u'电网用户'
        verbose_name_plural = u'电网用户信息'

    def __unicode__(self):
        return self.user_id

class Route(models.Model):
    _id = models.AutoField(primary_key=True)
    route_id = models.CharField(max_length=255,unique=True,verbose_name="路线ID")
    start = models.CharField(max_length=255,verbose_name="路线起点",null=True)
    end = models.CharField(max_length=255,verbose_name="路线终点",null=True)
    record_date = models.DateTimeField(verbose_name="路线采集时间",null=True)
    update_date = models.DateTimeField(verbose_name="用户信息上传到服务器的时间",null=True)
    collector = models.CharField(max_length = 50,verbose_name="采集者名字",null=True)
    distance = models.FloatField(verbose_name="距离",null=True)

    class Meta:
        db_table = 'route'
        verbose_name = u'路线'
        verbose_name_plural = u'路线信息fsaf'

    def __unicode__(self):
        return self.route_id

class Location(models.Model):
    _id = models.AutoField(primary_key=True)
    route_id = models.CharField(max_length=255,verbose_name="路线ID")
    lng = models.DecimalField(max_digits=10,decimal_places=6,verbose_name="经度",null=True)
    lat = models.DecimalField(max_digits=10,decimal_places=6,verbose_name="纬度",null=True)
    class Meta:
        db_table = 'location'
        verbose_name = u'采集点'
        verbose_name_plural = u'采集点信息'

    def __unicode__(self):
        return self._id

class Node(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,verbose_name=u"节点名称")
    dis_num = models.CharField(max_length=255,verbose_name=u'所在台区名称')
    record_date = models.DateTimeField(verbose_name=u"节点采集时间",null=True)
    update_date = models.DateTimeField(verbose_name=u"用户信息上传到服务器的时间",null=True)
    lng = models.DecimalField(max_digits=10,decimal_places=6,verbose_name="经度",null=True)
    lat = models.DecimalField(max_digits=10,decimal_places=6,verbose_name="纬度",null=True)
    class Meta:
        db_table = 'node'
        verbose_name = "节点信息"
        verbose_name_plural = "节点信息"

    def __unicode__(self):
       return self.name

class Image(models.Model):
    _id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, verbose_name=u'户号')
    # md5 = models.CharField(max_length=255, verbose_name=u'md5值', unique=True)
    content = models.ImageField(upload_to='images',default='a')

    # def get_url(self):
    #     # return os.path.join(settings.MEDIA_URL, self.user_name)
    #     path =os.path.join(settings.MEDIA_URL, self.md5)
    #     return path

    class Meta:
        db_table = 'image'
        verbose_name = "图片信息"
        verbose_name_plural = "图片信息"

    def __unicode__(self):
        return self.user_name

class Radio(models.Model):
    _id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, verbose_name=u'户号')
    md5 = models.CharField(max_length=255, verbose_name=u'md5值')
    class Meta:
        db_table = 'radio'
        verbose_name = "语音信息"
        verbose_name_plural = "语音信息"

    def __unicode__(self):
        return self.name

class XlsUser(models.Model):
    xls_user = models.FileField(upload_to = './upload/user/',verbose_name=u"文件名")

    class Meta:
        db_table = 'xls_user'
        verbose_name = u'用户信息xls文件'
        verbose_name_plural = u'用户信息xls文件'

    def __unicode__(self):
        return str(self.xls_user).split('/')[-1]


class XlsAddr(models.Model):
    xls_addr = models.FileField(upload_to = './upload/lng_lat/',verbose_name=u"文件名")

    class Meta:
        db_table = 'xls_addr'
        verbose_name = u'用户经纬度信息xls文件'
        verbose_name_plural = u'用户经纬度信息xls文件'

    def __unicode__(self):
        return str(self.xls_addr).split('/')[-1]


def get_auto_increment_id(db_table):
    """
    获取自增 _id 的序号
    :return:
    """
    if db_table == 'User':
        no = User.objects.last()
    elif db_table == 'Route':
        no = Route.objects.last()
    elif db_table == 'Location':
        no = Location.objects.last()

    if no == None:
        return 1
    else:
        return no._id + 1

#Signals
@receiver(post_save, sender=XlsUser)
def insert_into_user_db(sender, instance, created, **kwargs):
    """
    用户上传xls文件后，加入到数据库中
    """

    if created:
        print os.path.dirname(__file__)
        data = xlrd.open_workbook(str(instance.xls_user))
        table = data.sheets()[0] #获取表
        nrows = table.nrows #获取行数
        try:
            for i in xrange(1,nrows):
		table.row_values(i)[2] = int(table.row_values(i)[2])
                row = map(lambda s:str(s).strip(),table.row_values(i))

                obj_list = User.objects.filter(user_id = row[4])
                if not obj_list:
                    obj = User.objects.create(user_id = row[4],_id = get_auto_increment_id('User'))
                else:
                    obj = obj_list[0]

                obj.unit=row[0]
                obj.power_unit=row[1]
                obj.district_number=row[2]
                obj.district_name=row[3]
                obj.user_name=row[5]
                obj.user_addr=row[6]
                obj.terminal_number=row[7]
                obj.logical_addr=row[8]
                obj.meter_number=row[9]
                obj.collection_unit=row[10]
                obj.record_date=str(datetime.datetime.today())
                obj.update_date=str(datetime.date.today())
                obj.save()

        except Exception,e:
            print 'error:'+str(e)
        else:
            print(u"导入完成，成功导入%d条用户数据！" % (i))

    else:
        print "not created"

@receiver(pre_delete,sender=XlsUser)
def delete_user_xls(sender,instance,**kwargs):
    print str(instance.xls_user)
    try:
        os.remove(str(instance.xls_user))
    except Exception,e:
        pass

@receiver(post_save, sender=XlsAddr)
def insert_into_addr_db(sender, instance, created, **kwargs):
    """
    用户addr上传xls文件后，加入到数据库中
    """

    if created:
        data = xlrd.open_workbook(str(instance.xls_addr))
        table = data.sheets()[0] #获取表
        nrows = table.nrows #获取行数
        try:
            for i in xrange(1,nrows):
                row = map(lambda s:str(s).strip(),table.row_values(i))

                obj_list = User.objects.filter(user_id = row[0])
                if not obj_list:
                    obj = User.objects.create(user_id = row[0],_id = get_auto_increment_id('User'))
                else:
                    obj = obj_list[0]

                obj.kva = int(row[3])
                obj.meter_type = row[5]
                obj.tel_addr = row[6]
                obj.manufacturer = row[7]
                if row[8]:
                    obj.line_type = row[8]

                obj.metering_method = row[9]
                if row[10]:
                    obj.addr_lng = float(row[10])
                if row[11]:
                    obj.addr_lat = float(row[11])
                obj.record_date=str(datetime.datetime.today())
                obj.update_date=str(datetime.date.today())
                #obj.save()

        except Exception,e:
            print 'error'+str(e)
        else:
            #if (i % 50!=0):
            #    log.append(u"完成进度：%d / %d" % (i,nrows-1))
            print (u"导入完成，成功导入%d条经纬度数据！" % (i))
    else:
        print "not created"

@receiver(pre_delete,sender=XlsAddr)
def delete_addr_xls(sender,instance,**kwargs):
    print str(instance.xls_addr)
    try:
        os.remove(str(instance.xls_addr))
    except Exception,e:
        pass
