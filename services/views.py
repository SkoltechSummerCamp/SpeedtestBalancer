from django.db import transaction
from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from services import serializers, models


class ServiceRegistrationView(mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              GenericAPIView):
    serializer_class = serializers.ServerAddressRequestSerializer

    def get_queryset(self):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return models.ServerAddress.objects.filter(ip=data['ip'],
                                                   port=data['port'],
                                                   port_iperf=data['port_iperf'])

    def get_object(self):
        return get_object_or_404(self.get_queryset())

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.get_object()
        return self.destroy(request, *args, **kwargs)


class ServiceAcquirementView(APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        instance = models.ServerAddress.objects.select_for_update(skip_locked=True).first()
        if not instance:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        instance.delete()
        serializer = serializers.ServerAddressResponseSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
