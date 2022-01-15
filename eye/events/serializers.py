from django.db import transaction
from rest_framework import serializers

from events.models import Event, EventType


class EventSerializer(serializers.ModelSerializer):
    """Serializer of Event"""

    class Meta:
        model = Event
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):
        """Override creation for create event type for allowing to define payload validation"""
        event = super().create(validated_data)
        EventType.objects.update_or_create(category=event.category, name=event.name)
        return event
