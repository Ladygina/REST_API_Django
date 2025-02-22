# переделать под себя
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer
from rest_framework.generics import  ListAPIView, RetrieveAPIView
from rest_framework import status

sensor = Sensor(name = "microvawe", description='kitchen')
sensor.save()
sensor = Sensor(name = "lamp", description='coridor')
sensor.save()
sensor = Sensor(name = "boiler", description='bedroom')
sensor.save()

measure1 = Measurement(id_sensor='1',
                       temperature = '45')
measure1.save()
measure2 = Measurement(id_sensor='2',
                       temperature = '0')
measure2.save()
measure3 = Measurement(id_sensor='3',
                       temperature = '100')
measure3.save()

# 3 add measurement
@api_view(["POST"])
def add_measurement(name, temperature):
    measure = Measurement(name=name, temperature=temperature)
    measure.save()
    return Response('OK')

# 4
class List_sensors(ListAPIView):
  # 4 get sensors
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer     
# 1 create 
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class find_sensor(RetrieveAPIView):
    # 5 find sensor's info
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


    # 2 update
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
# if need - delete notes
# Sensor.objects.all().delete()
# Measurement.objects.all().delete()
