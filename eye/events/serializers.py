from django.db import transaction
from rest_framework import serializers

from events.models import Event, EventType, Session


class EventSerializer(serializers.ModelSerializer):
    """Serializer of Event"""
    session_id = serializers.UUIDField()

    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']

    @transaction.atomic()
    def create(self, validated_data):
        """Override creation for create event type for allowing to define payload validation"""
        session_id = validated_data.pop('session_id')
        application = self.context['request'].user
        validated_data['session'], _ = Session.objects.get_or_create(application=application, uuid=session_id)
        event = Event.objects.create(**validated_data)
        EventType.objects.update_or_create(category=event.category, name=event.name)
        return event
