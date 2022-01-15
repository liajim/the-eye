import logging

from django.forms import model_to_dict
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """ Override exception handler for log validation errors"""

    if isinstance(exc, ValidationError):
        logger.exception(f'Event Validation Exception: {exc}, for payload: {context["request"].data}, '
                         f'application_id: {context["request"].user.id}, '
                         f'application_name:{context["request"].user.username}')

    return exception_handler(exc, context)
