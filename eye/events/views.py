from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from events.models import Event
from events.serializers import EventSerializer
from events.tasks import save_event


class EventViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    http_method_names = ['post', 'get']
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []

    def create(self, request, **kwargs):
        """Override create for doing async"""
        save_event.delay(request.data, request.user.id)
        return Response(status=status.HTTP_200_OK, data={"message": "Processed"})
