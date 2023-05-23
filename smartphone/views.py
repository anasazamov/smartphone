from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Phone


def to_dict(phone: Phone) -> dict:
    '''inctance of Phone convert to dict'''
    return {
        'id': phone.id,
        'name': phone.name,
        'color': phone.color,
        'description': phone.description,
        'ram': phone.ram,
        'memory': phone.memory,
        'brend': phone.brend,
        'price': phone.price,
        'url': phone.url,
    }


def get_phone(request: HttpRequest, id: int) -> JsonResponse:
    '''get phone by id'''
    try:
        phone = Phone.objects.get(id=id)
        return JsonResponse(to_dict(phone))

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'object does not exist!'})