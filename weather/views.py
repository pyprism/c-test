from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from base.utils import IsAdmin
from .serializers import CityNameSerializer
from .models import CityName
from .utils import get_current_weather


class CityNameViewSet(ModelViewSet):
    queryset = CityName.objects.get_all_city()
    serializer_class = CityNameSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAdmin]

    @action(detail=True, methods=['get'])
    def get_current_weather(self, request, pk=None):
        current_weather = get_current_weather(pk)
        return Response({"current_weather": current_weather}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search_city(self, request):
        city_name = self.request.query_params.get('city_name', '')
        city_name_list = CityName.objects.search_city(city_name)
        page = self.paginate_queryset(city_name_list)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


