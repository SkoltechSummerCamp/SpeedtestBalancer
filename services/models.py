from django.db import models


class ServerAddress(models.Model):
    ip = models.TextField()
    port = models.IntegerField()
    port_iperf = models.IntegerField()
    time = models.DateTimeField()
