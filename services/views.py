from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from services import serializers, models


class ServiceRegistrationView(mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              GenericAPIView):
    serializer_class = serializers.ServerAddressRequestSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ServiceAcquirementView(GenericAPIView):
    queryset = models.ServerAddress.objects.all()[:1]

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return serializers.ServerAddressReponseSerializer(instance=instance)
