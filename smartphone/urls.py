from django.urls import path
from .views import (
    get_phone,
    get_all_phone,
)

urlpatterns = [
    path('smartphones/<int:id>', get_phone),
    path('smartphones/', get_all_phone)
]
