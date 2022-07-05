import datetime

from rest_framework import serializers

import services.models as models


class ServerAddressResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServerAddress
        fields = ('ip', 'port', 'port_iperf', 'time')


class ServerAddressRequestSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        return {'time': datetime.datetime.utcnow(), **attrs}

    class Meta:
        model = models.ServerAddress
        fields = ('ip', 'port', 'port_iperf')
