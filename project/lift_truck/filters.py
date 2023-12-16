from django_filters import FilterSet
from .models import Forklift, To, Claim


class ForkliftFilter(FilterSet):
    class Meta:
        model = Forklift
        fields = {
            'machine_serial_number': ['icontains'],
            'model_equipment__title': ['icontains'],
            'engine_model__title': ['icontains'],
            'transmission_model__title': ['icontains'],
            'drive_axle_model__title': ['icontains'],
            'controlled_bridge_model__title': ['icontains'],
        }


class ToFilter(FilterSet):
    class Meta:
        model = To
        fields = {
            'type__title': ['icontains'],
            'car__machine_serial_number': ['icontains'],
            'service_company__title': ['icontains'],
        }


class ClaimFilter(FilterSet):
    class Meta:
        model = Claim
        fields = {
            'car__machine_serial_number': ['icontains'],
            'order_note__title': ['icontains'],
            'recovery_method__title': ['icontains'],
            'service_company__title': ['icontains'],
        }
