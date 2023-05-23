from django.urls import path
from .views import (
    get_phone,
)

urlpatterns = [
    path('smartphones/<int:id>', get_phone)
]
