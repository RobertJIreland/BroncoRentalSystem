from rest_framework import generics
from car_rental_system.models import Vehicle, Reservations
from .serializers import ReservationSerializer, VehicleSerializer
from django_filters import rest_framework as filters

# when queryset has duplicate results, return only one of each
def distinct(queryset):
    d = {}
    for item in queryset:
        field_value = getattr(item, "vehicle_model")
        if field_value not in d:
            d[field_value] = item
    return d.values()


class VehicleList(generics.ListAPIView):
    serializer_class = VehicleSerializer


    def get_queryset(self):
        queryset = Vehicle.objects.all()

        vehicle_type = self.request.query_params['vehicleType']
        vehicle_class = self.request.query_params['vehicleClass']
        seats = self.request.query_params['seats']
        
        if vehicle_type != 'showAll':
            queryset = queryset.filter(vehicle_type=vehicle_type)
        if vehicle_class != 'showAll':
            queryset = queryset.filter(vehicle_class=vehicle_class)
        if seats != 'showAll':
            queryset = queryset.filter(seats=seats)

        return distinct(queryset)


class VehicleDetail(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    pass


class ReservationDetail(generics.RetrieveAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer
    pass


