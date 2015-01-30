from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class AllotmentType(models.Model):
    name = models.CharField(max_length=30)
    default_hours = models.DecimalField(max_digits=10, decimal_places=3,
                                        null=True, blank=True)
    max_hours = models.DecimalField(max_digits=10, decimal_places=3,
                                    null=True, blank=True)
    default_expiry_period = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)


class Allotment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.ForeignKey(AllotmentType)
    hours = models.DecimalField(max_digits=10, decimal_places=3)
    expiry = models.DateField(null=True, blank=True)
    action_log = GenericRelation('ActionRecord',
                                 related_query_name='allotment_log_records')

    def __str__(self):
        return "{} - {}".format(self.user, self.type.name)


class RequestState(models.Model):
    name = models.CharField(max_length=30)
    forward_state = models.ForeignKey('RequestState', null=True, blank=True,
                                      related_name='request_forward_state')
    reverse_state = models.ForeignKey('RequestState', null=True, blank=True,
                                      related_name='request_reverse_state')

    def __str__(self):
        return "{}".format(self.name)


class Request(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.ForeignKey(AllotmentType)
    start = models.DateTimeField()
    end = models.DateTimeField()
    hours = models.DecimalField(max_digits=10, decimal_places=3)
    notes = models.TextField(null=True, blank=True)
    state = models.ForeignKey(RequestState)
    action_log = GenericRelation('ActionRecord',
                                 related_query_name='request_log_records')

    def __str__(self):
        return "{} - {}: {} - {}".format(self.user, self.type.name,
                                         self.start, self.end)


class ActionRecord(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    action = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "{}: {}".format(self.date, self.user)


class AllotmentTypeOverride(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.ForeignKey(AllotmentType)
    default_hours = models.DecimalField(max_digits=10, decimal_places=3,
                                        null=True, blank=True)
    max_hours = models.DecimalField(max_digits=10, decimal_places=3,
                                    null=True, blank=True)
    default_expiry_period = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.user, self.type.name)

