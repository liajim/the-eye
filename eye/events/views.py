from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    http_method_names = ['post', 'get']
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []
