from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from events.models import Event, EventType, Session, data_structure


class EventSerializer(serializers.ModelSerializer):
    """Serializer of Event"""
    session_id = serializers.UUIDField()

    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']

    def validate_data(self, value):
        """
        Check that value is a valid name.
        """
        data_structure(value, self.initial_data['name'], self.initial_data['category'])
        return value

    @transaction.atomic()
    def create(self, validated_data):
        """Override creation for create event type for allowing to define payload validation"""
        session_id = validated_data.pop('session_id')
        application = self.context['request'].user
        validated_data['session'], created = Session.objects.get_or_create(application=application, uuid=session_id)
        event = Event.objects.create(**validated_data)
        EventType.objects.get_or_create(category=validated_data['category'], name=validated_data['name'])
        return event
