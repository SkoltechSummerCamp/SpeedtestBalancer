from django.core import validators
from django.db import models


class ServerAddress(models.Model):
    ip = models.GenericIPAddressField()
    port = models.IntegerField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(65535),
        ]
    )
    port_iperf = models.IntegerField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(65535),
        ]
    )
    time = models.DateTimeField()
