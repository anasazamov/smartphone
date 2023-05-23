from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json

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


def phone(request: HttpRequest, id=None) -> JsonResponse:
    '''get phone by id'''
    if request.method == "GET":
        if id is not None:
            try:
                phone = Phone.objects.get(id=id)
                return JsonResponse(to_dict(phone))

            except ObjectDoesNotExist:
                return JsonResponse({'status': 'object does not exist!'})
        else:
            phones = Phone.objects.all()

            result = [to_dict(phone=phone) for phone in phones]
            return JsonResponse(result, safe=False)
    
    elif request.method == 'POST':
        # get data from request body
        data_json = request.body.decode()
        data = json.loads(data_json)

        if not data.get('name'):
            return JsonResponse({'status': 'name is required!'})
        elif not data.get('url'):
            return JsonResponse({'status': 'url is required!'})
        elif not data['url'].startswith('https://'):
            return JsonResponse({'status': 'url is invalid!'})
        elif not data.get('color'):
            return JsonResponse({'status': 'color is required!'})
        elif not data.get('ram'):
            return JsonResponse({'status': 'ram is required!'})
        elif not data.get('brend'):
            return JsonResponse({'status': 'brend is required!'})
        elif not data.get('price'):
            return JsonResponse({'status': 'price is required!'})
        elif not data.get('memory'):
            return JsonResponse({'status': 'memory is required!'})

        phone = Phone.objects.create(
            name=data['name'],
            description=data.get('description', ''),
            url=data['url'],
            color=data['color'],
            ram=data['ram'],
            memory=data['memory'],
            brend=data['brend'],
            price=data['price'],
        )
        phone.save()

        return JsonResponse(to_dict(phone))

    return JsonResponse({'status': 'method not allowed!'})
