from django.urls import path
from .views import dropdown_view

urlpatterns = [
    path('dropdown/', dropdown_view, name='dropdown'),
]
