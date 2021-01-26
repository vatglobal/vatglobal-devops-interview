

# serializers.py
from rest_framework.serializers import ModelSerializer

from .models import Event

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'name',
            'description',
            'time'
        )
