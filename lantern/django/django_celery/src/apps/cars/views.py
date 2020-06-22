from django.utils.decorators import method_decorator
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.cars.models import Car
from apps.cars.permissions import CarIsAuthenticatedOrPublicOnly
from apps.cars.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (CarIsAuthenticatedOrPublicOnly,)

    # def get_queryset(self):
    #     return Car.objects.filter(dealer=self.request.user)

    @action(detail=False, methods=('get', ))
    def public(self, request):
        queryset = self.filter_queryset(Car.objects.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
