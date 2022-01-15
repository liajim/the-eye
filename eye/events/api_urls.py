from django.urls import path, include
from rest_framework import routers

from events.views import EventViewSet

eventRouter = routers.DefaultRouter()
eventRouter.register(r'', EventViewSet)

urlpatterns = [
    path('event/', include(eventRouter.urls)),
]