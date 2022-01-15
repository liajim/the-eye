import logging

from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from events.serializers import EventSerializer
from eye.celery import app

logger = logging.getLogger(__name__)


class Generic:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


@app.task
def save_event(data, user_id):
    """Save event using serializer"""
    user = User.objects.get(pk=user_id)
    serializer = EventSerializer(data=data, context={'request': Generic(user=user)})
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
    except ValidationError as exc:
        logger.exception(f'Event Validation Exception: {exc}, for payload: {data}, '
                         f'application_id: {user.id}, '
                         f'application_name:{user.username}')
