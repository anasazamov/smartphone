from django.urls import path
from .views import (
    phone,
    get_by_ram,
)

urlpatterns = [
    path('smartphones/<int:id>', phone),
    path('smartphones/', phone),
    path('get-by-ram/', get_by_ram),
]
