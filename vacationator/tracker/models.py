from django.db import models


# TODO: make these configurable
ALLOTMENT_TYPES = (
    ('vacation', 'Vacation'),
)


class Allotment(models.Model):
    type = models.CharField(max_length=30, choices=ALLOTMENT_TYPES)
    hours = models.DecimalField(max_digits=10, decimal_places=3)



