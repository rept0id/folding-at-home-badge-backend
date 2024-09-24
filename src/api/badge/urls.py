from django.urls import path
from .views import badge_view

urlpatterns = [
    path('badge/<str:username>/', badge_view, name='badge_view'),
]