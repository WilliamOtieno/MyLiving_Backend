from django.db import models
from uuid import uuid1


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Building(TimestampModel):
    uuid = models.UUIDField(default=uuid1, primary_key=True, db_index=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(null=True)
    tenant_number = models.PositiveIntegerField(default=0)
    location = models.TextField(null=True)
    gps_coordinates = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
