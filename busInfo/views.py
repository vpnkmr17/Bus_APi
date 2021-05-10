from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import StopNameSerializer
from .models import StopName,Route,BusNo
from math import cos, asin, sqrt, pi

def find_stop_name(bus_no):
    bus_obj=BusNo.objects.filter(bus_no=bus_no)
    buses=Route.objects.filter(bus_id=bus_obj[0]).values_list('stop_id',flat=True)
    stop_names=[]
    for val in buses:
        latiude=StopName.objects.get(id=val).latitude
        longitude=StopName.objects.get(id=val).longitude
        stop_name=StopName.objects.get(id=val).stop_name
        # print("Latitude is ",StopName.objects.get(id=val).latitude)
        # print("Longitude is ",StopName.objects.get(id=val).longitude)
        stop_names.append([stop_name,latiude,longitude])
    return stop_names


# Find Distance between two points on earth
# using Haversine formula
def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a)) 


# http://127.0.0.1:8000/search/
# Data--->  {
#     "source":"Airoli Bus Station",
#     "destination":"Ankur Hospital"
# }
@api_view(['POST'])
def searchView(request):
    data=request.data or None
    src_id=StopName.objects.filter(stop_name=data['source'])
    dest_id=StopName.objects.filter(stop_name=data['destination'])
    list1=Route.objects.filter(stop_id=src_id[0]).values_list('bus_id',flat=True)
    list2=Route.objects.filter(stop_id=dest_id[0]).values_list('bus_id',flat=True)
    bus1=[]
    bus2=[]
    for val in list1:
        bus1.append(BusNo.objects.get(id=val).bus_no)
    for val in list2:
        bus2.append(BusNo.objects.get(id=val).bus_no)
    common_bus={}
    for val in bus2:
        if val in bus1:
            common_bus[val]=find_stop_name(val)
    #print(common_bus)
    for values in common_bus:
        dist=0
        flag=0
        for i in range(len(common_bus[values])-1):
            val1=common_bus[values][i]
            val2=common_bus[values][i+1]
            if val1[0]==data['source'] or val1[0]==data['destination']:
                if flag==0:
                    flag=1
                else:
                    break
            if flag==1:
                # print(val1[0])
                dist+=distance(val1[1],val1[2],val2[1],val2[2])
        common_bus[values]+=[int(dist)]
       
   
    print(common_bus)

    common_bus=dict(sorted(common_bus.items(),key=lambda val:val[1][-1]))

    return Response({"Bus":common_bus})


#http://127.0.0.1:8000/busno/
# Data--> {
#     "bus_no":"545 LTD"
# }
@api_view(['POST'])
def searchBusno(request):
    data=request.data
    bus_no=data['bus_no']
    stop_names={}
    stop_names[bus_no]=find_stop_name(bus_no)
   
    return Response({"Accepted":stop_names})

