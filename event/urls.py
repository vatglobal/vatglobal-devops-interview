# urls.py
from django.conf.urls import include, re_path, url
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventDjangoQViewSet
from event import views
from django.urls import path

router = DefaultRouter()
router.register(f"event", EventViewSet, basename='event')

urlpatterns = [
    re_path('^', include(router.urls)),
    url(r'^djangoq', EventDjangoQViewSet.as_view(), name='djangoq'),
    path('<str:pk>/', views.get_event, name='djangoq'),
]
