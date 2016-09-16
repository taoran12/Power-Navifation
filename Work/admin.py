# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.contrib import admin
from .models import Route,User,Node,Image,Radio,XlsAddr,XlsUser
from django.http import HttpResponse
import xlwt
from time import *

def export_user_xls(modeladmin, request, queryset):
    objs = [obj for obj in queryset]

    file_str = 'export_user.xls'
    result = write_user_xls(objs,file_str)

    if result:
        f = open(file_str, 'rb')
        response = HttpResponse(f, content_type='application/vnd.ms-excel')

        file_with_time = r'user-'+strftime('%Y-%m-%d-%H-%M-%S',localtime())+'.xls'
        response['Content-Disposition'] = 'attachment; filename=%s' % file_with_time
        return response

export_user_xls.short_description = u"下载选中用户的用户信息excel表"

def export_lnglat_xls(modeladmin,request,queryset):
    objs = [obj for obj in queryset]

    file_str = 'export_addr.xls'
    result = write_lnglat_xls(objs,file_str)

    if result:
        f = open(file_str, 'rb')
        response = HttpResponse(f, content_type='application/vnd.ms-excel')

        file_with_time = r'addr-'+strftime('%Y-%m-%d-%H-%M-%S',localtime())+'.xls'
        response['Content-Disposition'] = 'attachment; filename=%s' % file_with_time
        return response

export_lnglat_xls.short_description = u"下载选中用户的经纬度excel表"

def write_user_xls(objs,file_str,log=None):
    """
    从数据库中读取最新的user信息，写入到指定的xls里面,并返回给浏览器
    :param file_str: 要写入的文件名字
    :return:None
    """
    xls = xlwt.Workbook(encoding='utf8')
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'    # 指定“宋体”
    style.font = font

    xls_sheet = xls.add_sheet(u'用户信息',cell_overwrite_ok=True)

    #生成表头
    row0 = [u'单位',u'供电所',u'台区编码',u'台区名称',u'户号',u'户名',u'用户地址',u'终端局号',\
            u'逻辑地址',u'表计局号',u'采集单位',u'备用1',u'备用2',u'备用3',u'备用4']

    for i in range(0,len(row0)):
        xls_sheet.write(0,i,row0[i],style)

    #写入数据
    try:
        if objs:
            for i in range(len(objs)):
                xls_sheet.write(i+1,0,objs[i].unit,style)
                xls_sheet.write(i+1,1,objs[i].power_unit,style)
                xls_sheet.write(i+1,2,objs[i].district_number,style)
                xls_sheet.write(i+1,3,objs[i].district_name,style)
                xls_sheet.write(i+1,4,objs[i].user_id,style)
                xls_sheet.write(i+1,5,objs[i].user_name,style)
                xls_sheet.write(i+1,6,objs[i].user_addr,style)
                xls_sheet.write(i+1,7,objs[i].terminal_number,style)
                xls_sheet.write(i+1,8,objs[i].logical_addr,style)
                xls_sheet.write(i+1,9,objs[i].meter_number,style)
                xls_sheet.write(i+1,10,objs[i].collection_unit,style)
                xls_sheet.write(i+1,11,objs[i].remark1,style)
                

    except Exception,e:
        print u"导出失败："+str(e)
        return False
    else:
        xls.save(file_str)
        print u"导出数据结束，成功导出%d条数据！" % (i+1)
        return True

def write_lnglat_xls(objs,file_str,log=None):
    """
    从数据库中读取最新的user信息，写入到指定的xls里面
    :param file_str: 要写入的文件名字
    :return:None
    """

    xls = xlwt.Workbook(encoding='utf8')
    xls_sheet = xls.add_sheet(u'终端档案查询',cell_overwrite_ok=True)

    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'    # 指定“宋体”
    style.font = font

    #生成表头
    row0 = [u'户号',u'户名',u'用户地址',u'受电容量(kVA)',u'表计局号',u'表计规约',\
            u'通讯地址',u'表计厂家',u'接线方式',u'计量方式',u'经度',u'纬度']


    for i in range(0,len(row0)):
        xls_sheet.write(0,i,row0[i])

    #写入数据
    try:
        if objs:
            for i in range(len(objs)):
                xls_sheet.write(i+1,0,objs[i].user_id,style)
                xls_sheet.write(i+1,1,objs[i].user_name,style)
                xls_sheet.write(i+1,2,objs[i].user_addr,style)
                xls_sheet.write(i+1,3,objs[i].kva,style)
                xls_sheet.write(i+1,4,objs[i].meter_number,style)
                xls_sheet.write(i+1,5,objs[i].meter_type,style)
                xls_sheet.write(i+1,6,objs[i].tel_addr,style)
                xls_sheet.write(i+1,7,objs[i].manufacturer,style)
                xls_sheet.write(i+1,8,objs[i].line_type,style)
                xls_sheet.write(i+1,9,objs[i].metering_method,style)
                xls_sheet.write(i+1,10,objs[i].addr_lng,style)
                xls_sheet.write(i+1,11,objs[i].addr_lat,style)
    except Exception,e:
        print u"导出失败："+str(e)
        return False
    else:
        xls.save(file_str)
        print u"导出数据结束，成功导出%d经纬度数据！" % (i+1)
        return True


class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_id', 'start', 'end','record_date')

class UserAdmin(admin.ModelAdmin):
    list_display = ('_id','user_id','user_name','meter_number','addr_lng','addr_lat',\
                    'user_addr','district_name','district_number','remark1','get_url')
    actions = [export_user_xls,export_lnglat_xls]
    search_fields=('district_name','district_number','user_name','user_id')

    def get_url(self, obj):
        url = "/admin/Work/image?user_name=%s" % obj.user_id
        return "<a href='%s' target=\"_blank\">点击查看</a>" % url

    get_url.short_description = "所属图片"
    get_url.allow_tags = True

class NodeAdmin(admin.ModelAdmin):
    list_display = ('_id','name','dis_num','record_date','lng','lat')
    search_fields=('dis_num',)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('_id','user_name','get_url')
    search_fields=('dis_num',)

    # def get_photo(self, obj):
    #     url = "http://localhost:8000/api/photo?name=%s" % obj.md5
    #     return "<a href='%s' target=\"_blank\">点击查看</a>" % url

    def get_url(self, obj):
        return u'<a href="%s" target="_blank">查看</a>' % obj.content.url

    get_url.short_description = 'URL'
    get_url.allow_tags = True

    # get_photo.short_description = "所属图片"
    # get_photo.allow_tags = True
class RadioAdmin(admin.ModelAdmin):
    list_display = ('_id','user_name','md5')
    search_fields=('dis_num',)

admin.site.register(Route,RouteAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Node,NodeAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Radio,RadioAdmin)
admin.site.register(XlsUser)
admin.site.register(XlsAddr)
