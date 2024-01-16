import json

from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from service_center.models import Clients, Orders, Staff, Categories
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def token_verify(request):
    return JsonResponse({"result": 'ok'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_clients(request):
    result = [{
        "id": i.pk,
        "full_name": i.get_client_fio(),
        "phone": i.phone_number,
    } for i in Clients.objects.all()]
    return JsonResponse({"result": sorted(result, key=lambda sort_by: sort_by['id'])})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_clients_for_adm(request):
    result = [{
        "id": i.pk,
        "last_name": i.last_name,
        "first_name": i.first_name,
        "father_name": i.father_name,
        "phone": i.phone_number,
    } for i in Clients.objects.all()]
    return JsonResponse({"result": sorted(result, key=lambda sort_by: sort_by['id'])})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_categories(request):
    result = [{
        "id": i.pk,
        "name": i.name,
    } for i in Categories.objects.all()]
    return JsonResponse({"result": sorted(result, key=lambda sort_by: sort_by['id'])})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_staff_data(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (данные_сотрудника): {data}')
    result = [{
        "id": i.pk,
        "full_name": i.get_staff_fio(),
        "phone": i.phone_number,
        "post": i.post
    } for i in Staff.objects.all().filter(pk=data)]
    return JsonResponse({"result": result})

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_staff(request):
    result = [{
        "id": i.pk,
        "full_name": i.get_staff_fio(),
        "post": i.post
    } for i in Staff.objects.all()]
    return JsonResponse({"result": sorted(result, key=lambda sort_by: sort_by['id'])})

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_orders_for_adm(request):
    result = [{
        "id": i.pk,
        "title": i.title,
        "description": i.description,
        "category": i.category_id,
        "status": i.status,
        "client": i.client_id,
        "staff_in": i.staff_in_id,
        "executor": i.executor_id,
        "staff_out": i.staff_out_id,
        "created_at": i.created_at,
        "repair_at": i.repair_at,
        "closed_at": i.closed_at
    } for i in Orders.objects.all()]
    return JsonResponse({"result": sorted(result, key=lambda sort_by: sort_by['id'])})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_orders(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (данные_заказов): {data}')
    result = [{
        "id": i.pk,
        "title": i.title,
        "status": i.status,
        "categoryTitle": i.category.name,
        "client_FN": i.client.get_client_fio(),
        "client_phone": i.client.phone_number,
    } for i in Orders.objects.all().filter(status=data['status']).select_related('category', 'client')]
    return JsonResponse({"result": sorted(result, key=lambda sort_by: sort_by['id'])})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_my_orders(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (данные_моих_заказов): {data}')
    result = [{
        "id": i.pk,
        "title": i.title,
        "status": i.status,
        "categoryTitle": i.category.name,
        "client_FN": i.client.get_client_fio(),
        "client_phone": i.client.phone_number,
    } for i in
        Orders.objects.all().filter(Q(executor_id=data['executor_id']) & Q(status=data['status'])).select_related(
            'category', 'client')]
    return JsonResponse({"result": sorted(result, key=lambda sort_by: sort_by['id'])})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_my_orders_count(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (данные_кол-во_моих_заказов): {data}')
    result = Orders.objects.aggregate(
        orders_in=Count('pk', filter=Q(staff_in=data['staff_id'])),
        orders_done=Count('pk', filter=Q(executor_id=data['staff_id'])),
        orders_out=Count('pk', filter=Q(staff_out=data['staff_id']))
    )
    print(result)
    return JsonResponse({"result": result})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_other_order_data(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (полные_данные_заказа): {data}')
    result = [{
        "id": i.pk,
        "client_id": i.client.pk,
        "category_id": i.category_id,
        "description": i.description,
        "staff_in_FN": i.staff_in.get_staff_fio(),
        "executor_FN": i.get_executor_fio(),
        "staff_out_FN": i.get_staff_out_fio(),
        "created_at": i.created_at,
        "repair_at": i.get_repair_date(),
        "closed_at": i.get_closed_date(),
    } for i in Orders.objects.all().filter(pk=data).select_related('staff_in', 'staff_out', 'executor',
                                                                   'client', 'category')]
    print(result[0]["id"])
    return JsonResponse({"result": sorted(result, key=lambda sort_by: sort_by['id'])})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def add_order(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (добавление_заказа): {data}')
    order = Orders(
        title=data['title'],
        description=data['description'],
        status=data['status'],
        category_id=data['category_id'],
        client_id=data['client_id'],
        staff_in_id=data['staff_in_id'],
        created_at=datetime.strptime(data['created_at'], "%d.%m.%Y")
    )
    order.save()
    return JsonResponse({"result": 'Заказ успешно сформирован!'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def add_order_adm(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (добавление_заказа-adm): {data}')
    order = Orders(
        title=data['title'],
        description=data['description'],
        status=data['status'],
        category_id=data['category_id'],
        client_id=data['client_id'],
        staff_in_id=data['staff_in'],
        executor_id=data['executor'],
        staff_out_id=data['staff_out'],
        created_at=datetime.strptime(data['created_at'], "%Y-%m-%d"),
        repair_at=datetime.strptime(data['repair_at'], "%Y-%m-%d"),
        closed_at=datetime.strptime(data['closed_at'], "%Y-%m-%d"),
    )
    order.save()
    return JsonResponse({"result": 'Заказ успешно добавлен!'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def add_client(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (добавление_клиента): {data}')
    client = Clients(
        last_name=data['last_name'],
        first_name=data['first_name'],
        father_name=data['father_name'],
        phone_number=data['phone_number']
    )
    client.save()
    return JsonResponse({"result": 'Клиент успешно добавлен!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def add_category(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (добавление_категории): {data}')
    category = Categories(
        name=data['name']
    )
    category.save()
    return JsonResponse({"result": 'Категория успешно добавлена!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def update_order(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (изменение_данных_заказа): {data}')
    order = Orders.objects.get(id=data['id'])
    order.title = data['title']
    order.description = data['description']
    order.category_id = data['category_id']
    order.client_id = data['client_id']
    order.save()
    return JsonResponse({"result": 'Данные заказа успешно изменены!'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def update_order_adm(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (изменение_данных_заказa-adm): {data}')
    order = Orders.objects.get(id=data['id'])
    order.title = data['title']
    order.status = data['status']
    order.description = data['description']
    order.category_id = data['category_id']
    order.staff_in_id = data['staff_in']
    order.executor_id = data['executor']
    order.staff_out_id = data['staff_out']
    order.client_id = data['client_id']
    order.created_at = data['created_at']
    order.repair_at = data['repair_at']
    order.closed_at = data['closed_at']
    order.save()
    return JsonResponse({"result": 'Данные заказа успешно изменены!'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def take_order(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (взятие_заказа): {data}')
    order = Orders.objects.get(id=data['id'])
    order.executor_id = data['executor_id']
    order.status = data['status']
    order.save()
    return JsonResponse({"result": 'Вы приняли заказ!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def order_done(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (взятие_заказа): {data}')
    order = Orders.objects.get(id=data['id'])
    order.repair_at = datetime.strptime(data['repair_at'], "%d.%m.%Y")
    order.status = data['status']
    order.save()
    return JsonResponse({"result": 'Заказ переведен в состояние готовности!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def order_out(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (взятие_заказа): {data}')
    order = Orders.objects.get(id=data['id'])
    order.closed_at = datetime.strptime(data['closed_at'], "%d.%m.%Y")
    order.staff_out_id = data['staff_out']
    order.status = data['status']
    order.save()
    return JsonResponse({"result": 'Заказ выдан клиенту!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def update_client(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (изменение_данных_клиента): {data}')
    client = Clients.objects.get(id=data['id'])
    client.last_name = data['last_name']
    client.first_name = data['first_name']
    client.father_name = data['father_name']
    client.phone_number = data['phone_number']
    client.save()
    return JsonResponse({"result": 'Данные клиента успешно изменены!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def update_category(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (изменение_данных_категории): {data}')
    category = Categories.objects.get(id=data['id'])
    category.name = data['name']
    category.save()
    return JsonResponse({"result": 'Данные категории успешно изменены!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def delete_order(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (удаление_заказа): {data}')
    order = Orders.objects.get(id=data['id'])
    order.delete()
    return JsonResponse({"result": 'Данные заказа успешно удалены!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def delete_client(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (удаление_клиента): {data}')
    client = Clients.objects.get(id=data['id'])
    client.delete()
    return JsonResponse({"result": 'Данные клиента успешно удалены!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def delete_category(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные (удаление_категории): {data}')
    category = Categories.objects.get(id=data['id'])
    category.delete()
    return JsonResponse({"result": 'Данные категории успешно удалены!'})
