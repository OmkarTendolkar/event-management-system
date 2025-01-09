from django.urls import path
from . import views

app_name = 'events_app'
urlpatterns = [
    path('', views.event_list, name='event_list'),
]
