from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from .serializers import CarParkSerializer, UnparkCarSerializer
from park.services.parking_services import ParkingService, UnparkService
from park.services.parking_info_service import ParkingInfoService


# Create your views here.

def index(request):
    return HttpResponse("Hello, world")


class ParkCar(APIView):
    throttle_classes = [UserRateThrottle]

    def post(self, request, format=None):
        serializer = CarParkSerializer(data=request.data)
        if serializer.is_valid():
            obj = ParkingService(serializer.data)
            return_response = obj.park_car()
            return Response(return_response , status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_200_OK)

class UnparkCar(APIView):
    throttle_classes = [UserRateThrottle]

    def post(self, request, format=None):
        serializer = UnparkCarSerializer(data=request.data)
        if serializer.is_valid():
            obj = UnparkService(serializer.data)
            return_response = obj.unpark_car()
            return Response(return_response , status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_200_OK)

class GetCarSlotInfo(APIView):
    throttle_classes = [UserRateThrottle]
    
    def get(self, request, format=None):
        slot = request.GET.get('slot', None)
        car_number = request.GET.get('car_number', None)
        obj = ParkingInfoService(slot = slot, car_number = car_number)
        return_response  = obj.get_info()
        
        return Response(return_response, status=status.HTTP_200_OK)