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

    elif request.method == "PUT":
        try:
            phone = Phone.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        # get data from request body
        data_json = request.body.decode()
        data = json.loads(data_json)
        
        if data.get('name'):
            phone.name = data['name']
        if data.get('url'):
            phone.url = data['url']
        if data.get('color'):
            phone.color = data['color']
        if data.get('ram'):
            phone.ram = data['ram']
        if data.get('memory'):
            phone.memory = data['memory']
        if data.get('brend'):
            phone.brend = data['brend']
        if data.get('price'):
            phone.price = data['price']
        if data.get('description'):
            phone.description = data['description']

        phone.save()

        return JsonResponse(to_dict(phone))

    elif request.method == "DELETE":
        try:
            phone = Phone.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        phone.delete()

        return JsonResponse({'status': 'ok'})

    return JsonResponse({'status': 'method not allowed!'})



def get_by_ram(request: HttpRequest) -> JsonResponse:
    params = request.GET

    ram = int(params.get('ram', 0))
    if ram:
        phones = Phone.objects.filter(ram=ram).order_by("price").reverse()

        result = [to_dict(phone) for phone in phones]
        return JsonResponse(result, safe=False)


def get_by_price_in_range(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        params = request.GET

        min = float(params.get('min'))
        max = float(params.get('max'))
        
        result = []

        for smartphone in Phone.objects.all():
            if min <= smartphone.price and smartphone.price <= max:
                result.append(to_dict(smartphone))

        return JsonResponse(result, safe=False)

def get_by_name(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        params = request.GET

        name = (params.get('name',""))
        
        if name:
            result = []

            for smartphone in Phone.objects.filter(name__icontains=name):
                    result.append(to_dict(smartphone))
            if result:
                return JsonResponse(result, safe=False)
            return JsonResponse({"result":"Not found"})
        return JsonResponse({"error":"not name"})
