# views.py
from django_q.tasks import async_task, result

from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer
from rest_framework.views import APIView
from .func import create_event_schedule
from utils.func_to_ref import func_ref_to_import

class EventViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = EventSerializer
      queryset = Event.objects.all()

class EventDjangoQViewSet(APIView):
    def post(self, request, *args, **kw):
        async_task(func_ref_to_import(create_event_schedule))
        return Response({"result": "Async event"})