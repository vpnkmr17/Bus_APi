from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import StopNameSerializer
from .models import StopName,Route,BusNo

def find_stop_name(bus_no):
    temp=[]
    bus_obj=BusNo.objects.filter(bus_no=bus_no)
    buses=Route.objects.filter(bus_id=bus_obj[0]).values_list('stop_id',flat=True)
    stop_names=[]
    for val in buses:
        temp.append(StopName.objects.get(id=val).stop_name)
    return temp

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

