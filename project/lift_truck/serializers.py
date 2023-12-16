from rest_framework import serializers
from .models import Forklift, To, Claim


class ForkliftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forklift
        fields = ('__all__')


class ToSerializer(serializers.ModelSerializer):
    class Meta:
        model = To
        fields = ('__all__')


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = ('__all__')
