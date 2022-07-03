from rest_framework import serializers

import services.models as models


class ServerAddressReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServerAddress
        fields = ('ip', 'port', 'port_iperf', 'time')


class ServerAddressRequestSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        ip = self.context['request'].META.get('REMOTE_ADDR')
        if ip is None:
            raise serializers.ValidationError(detail="Could not recognize service address")
        return {'ip': ip, **attrs}

    class Meta:
        model = models.ServerAddress
        fields = ('port', 'port_iperf', 'time')
