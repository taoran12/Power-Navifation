#encoding=utf-8
from django.test import TestCase

# Create your tests here.

from unittest import TestCase
#from django.test import TestCase
from Work.models import Route,Location

MAXLENGTH = 999999

class RouteTestCase(TestCase):
    routes = Route.objects.filter()
    point_set = set()
    locations_list = {}
    geo = {}

    #数据初始化
    for route in routes:
        point_set.add(route.start)
        point_set.add(route.end)
        locations = Location.objects.filter(route_id = route.route_id)
        geo[route.start] = (locations[0].lng,locations[0].lat)
        geo[route.end] = (locations[len(locations)-1].lng,locations[len(locations)-1].lat)
        locations_list[route.route_id] = []
        for location in locations:
            locations_list[route.route_id].append(location._id)

        print route
        print geo[route.start]
        print geo[route.end]
        print locations_list[route.route_id]
        print '\n'

    #每两点之间都通过SPFA算法找到最短路径，并加入数据库
    for start in point_set:
        for end in point_set:
            if (start==end):
                pass
            elif ((Route.objects.filter(start=start).filter(end=end).exists()) or
                (Route.objects.filter(start=end).filter(end=start).exists())):
                print start+'to'+end+"exists"
            else:
                print start+'to'+end

