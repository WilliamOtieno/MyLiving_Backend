from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from .models import Building
from .serializers import BuildingSerializer


class BuildingListAPIView(ListAPIView):
    """
    Returns JSON of all available buildings
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingCreateAPIView(CreateAPIView):
    """
    Creates a building given valid json request data
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingUpdateAPIView(UpdateAPIView):
    """
    Updates object fields
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingDeleteAPIView(DestroyAPIView):
    """
    Deletes objects from the DB
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingRetrieveAPIView(RetrieveAPIView):
    """
    Retrieves/GETs a single object from the DB
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
