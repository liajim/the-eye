from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(CreateModelMixin, GenericViewSet):
    http_method_names = ['post']
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []
