#encoding=utf-8
# Create your views here.
import hashlib
import json
import datetime
from django.views.generic import View
from django.http import HttpResponse
from .models import User, Route, Image, Radio, Location, Node
import os


def index(request):
    return HttpResponse("欢迎使用电力作业导航系统！")


class UserHandler(View):

    def get(self,request):
        """
        根据时间戳，获取未更新的用户信息
        :param request:
        :return:
        """
        date = request.GET.get('date')
        year, month, day = str(date).strip().split('-')
        users = User.objects.filter(update_date__gte=datetime.date(int(year),int(month),int(day)))
        resp = []
        for user in users:
            data = {
                "unit":user.unit,
                "power_unit":user.power_unit,
                "district_number":user.district_number,
                "district_name":user.district_name,
                "user_id":user.user_id,
                "user_name":user.user_name,
                "user_addr":user.user_addr,
                "addr_lng":str(user.addr_lng),
                "addr_lat":str(user.addr_lat),
                "terminal_number":user.terminal_number,
                "meter_number":user.meter_number,
                "logical_addr":user.logical_addr,
                "record_date":str(user.record_date),
                "collection_unit":user.collection_unit,
                "remark1":str(user.remark1)
            }
            resp.append(data)
        return HttpResponse(json.dumps(resp),status=200)

    def post(self,request):
        """
        接受客户端向服务器发送的更新信息，更新user表
        :param request:
        :return:
        """
        post_data = json.loads(request.body)
        try:
            for data in post_data:
                obj = User.objects.get(user_id=data['user_id'])
                if obj:
                    obj.unit = data["unit"]
                    obj.power_unit = data["power_unit"]
                    obj.district_number = data["district_number"]
                    obj.district_name = data["district_name"]
                    obj.user_name = data["user_name"]
                    obj.user_addr = data["user_addr"]
                    obj.user_id = data["user_id"]
                    obj.addr_lng = data["addr_lng"]
                    obj.addr_lat = data["addr_lat"]
                    obj.terminal_number = data["terminal_number"]
                    obj.meter_number = data["meter_number"]
                    obj.logical_addr = data["logical_addr"]
                    obj.collection_unit = data["collection_unit"]
                    obj.record_date = data["record_date"]
                    obj.update_date = str(datetime.date.today())
                    obj.remark1 = data["remark1"]
                    obj.save()
                else:
                   print "user_id not found."

        except Exception,e:
            return_code = -1
            return_msg = "error:"+str(e)
            status_code = 202
        else:
            return_code = 0
            return_msg = "ok"
            status_code = 200

        return self._response(return_code,return_msg,status_code)

    def _response(self, return_code,return_msg, status_code):
        result = {'code': return_code, 'msg': return_msg}
        return HttpResponse(json.dumps(result), status=status_code)

class ImageHandler(View):

    def get(self, request):
        d = request.GET.get('name')
        photos = Image.objects.filter(user_name=d)
        resp = []
        for photo in photos:
            p_url = photo.content.url
            resp.append(p_url)
        return HttpResponse(json.dumps(resp), status=200)

    def post(self,request):
        try:
            data = request.FILES['image']
            d = request.GET.get('name')
            new_img = Image(user_name=d, content=data)
            print new_img.content.url
            new_img.save()
            return_code = 0
            return_msg = "ok"
            status_code = 200
        except Exception, e:
            return_code = -1
            return_msg = "error:" + str(e)
            status_code = 202
        return self._response(return_code, return_msg, status_code)

    def _response(self,return_code,return_msg,status_code):
        result = {'code' : return_code, 'msg':return_msg}
        return HttpResponse(json.dumps(result),status=status_code)

class RadioHandler(View):

    def get(self, request):
        d = request.GET.get('name')
        radios = Radio.objects.filter(user_name=d)
        resp = []
        for radio in radios:
            r_url = radio.content.url
            resp.append(p_url)

        return HttpResponse(json.dumps(resp), status=200)

    def post(self, request):
        try:
            data = request.FILES['image'].read()
            d=request.GET.get('name')
            m = hashlib.md5()
            m.update(data)
            hashed = m.hexdigest()
            path = '/Users/taoran/radio' + d
            if not os.path.exists(path):
                os.makedirs(path)
            photo_path = path + '/' + hashed
            f = open(photo_path, 'wb')
            f.write(data)
            f.close()
            i = Redio(user_name=d, md5=hashed)
            i.save()
            return_code = 0
            return_msg = "ok"
            status_code = 200
        except Exception, e:
            return_code = -1
            return_msg = "error:" + str(e)
            status_code = 202
        return self._response(return_code, return_msg, status_code)

    def _response(self,return_code,return_msg,status_code):
        result = {'code' : return_code, 'msg':return_msg}
        return HttpResponse(json.dumps(result),status=status_code)


class RouteHandler(View):

    def get(self, request):
        date = request.GET.get('date')
        year, month, day = str(date).strip().split('-')
        resp = {'route': [], 'node': []}
        #获取路线
        routes = Route.objects.filter(update_date__gte=datetime.date(int(year),int(month),int(day)))
        if routes.exists():
            for route in routes:
                data = {
                    "route_id": route.route_id,
                    "start": route.start,
                    "end": route.end,
                    "record_date": str(route.record_date),
                    "collector": route.collector,
                    "distance":route.distance
                }
                location_set = Location.objects.filter(route_id=route.route_id)
                locations = []
                for location in location_set:
                    locations.append(
                        {
                        "lng":str(location.lng),
                        "lat":str(location.lat),
                        }
                    )
                data["locations"] = locations
                resp['route'].append(data)

        #获取节点描述
        nodes = Node.objects.filter(update_date__gte=datetime.date(int(year), int(month), int(day)))
        if nodes.exists():
            for node in nodes:
                data = {
                    "name": node.name,
                    "dis_num": node.dis_num,
                    "record_date":str(node.record_date),
                    "lng":str(node.lng),
                    "lat":str(node.lat)
                }
                resp['node'].append(data)

        return HttpResponse(json.dumps(resp),status=200)

    def post(self, request):
        post_data = json.loads(request.body)
        try:
            for data in post_data['route']:
                route, created = Route.objects.update_or_create(route_id=data["route_id"])
                route.start = data["start"]
                route.end = data["end"]
                route.collector = data["collector"]
                route.record_date = data["record_date"]
                route.distance = data["distance"]
                route.update_date = str(datetime.date.today())
                for location in data["locations"]:
                    obj = Location.objects.create(route_id=data["route_id"])
                    obj.lng = location["lng"]
                    obj.lat = location["lat"]
                    obj.save()
                route.save()

            if post_data.has_key('node'):
                for data in post_data['node']:
                    node,created = Node.objects.update_or_create(name = data["name"])
                    node.name = data['name']
                    node.dis_num = data['dis_num']
                    node.record_date = data["record_date"]
                    node.update_date = str(datetime.date.today())
                    node.lng = data['lng']
                    node.lat = data['lat']
                    node.save()

        except Exception, e:
            return_code = -1
            return_msg = "error:"+str(e)
            status_code = 202
        else:
            return_code = 0
            return_msg = "ok"
            status_code = 200

        return self._response(return_code, return_msg, status_code)

    def _response(self,return_code,return_msg,status_code):
        result = {'code': return_code, 'msg':return_msg}
        return HttpResponse(json.dumps(result),status=status_code)
