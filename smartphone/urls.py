from django.urls import path
from .views import (
    phone,
)

urlpatterns = [
    path('smartphones/<int:id>', phone),
    path('smartphones/', phone),
]
