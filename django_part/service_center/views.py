import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from service_center.models import Clients, Orders, Staff, Categories
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def get_clients(request):
    result = [{
        "id": i.pk,
        "full_name": i.get_client_fio(),
        "phone": i.phone_number,
    } for i in Clients.objects.all()]
    return JsonResponse({"result": result})


@csrf_exempt
def get_categories(request):
    result = [{
        "id": i.pk,
        "name": i.name,
    } for i in Categories.objects.all()]
    return JsonResponse({"result": result})


@csrf_exempt
def get_staff(request):
    result = [{
        "id": i.pk,
        "last_name": i.last_name,
        "first_name": i.first_name,
        "father_name": i.father_name,
        "phone": i.phone_number,
        "account_login": i.account.login
    } for i in Staff.objects.all().select_related('account')]
    return JsonResponse({"result": result})


@csrf_exempt
def get_orders(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные: {data}')
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
def get_other_order_data(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные: {data}')
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
def add_order(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные: {data}')
    if request.method == "POST":
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
    return JsonResponse({"result": 'Данные сохранены'})


@csrf_exempt
def update_order(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные: {data}')
    if request.method == "POST":
        order = Orders.objects.get(id=data['id'])
        order.title = data['title']
        order.description = data['description']
        order.category_id = data['category_id']
        order.client_id = data['client_id']
        order.save()
    return JsonResponse({"result": 'Данные изменены'})


@csrf_exempt
def delete_order(request):
    data = json.loads(request.body.decode())
    print(f'Пришедшие данные: {data}')
    if request.method == "POST":
        order = Orders.objects.get(id=data['id'])
        order.delete()
    return JsonResponse({"result": 'Данные удалены'})
