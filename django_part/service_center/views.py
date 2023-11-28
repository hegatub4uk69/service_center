"""
Используется для первого метода работы с данными.
"""
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from service_center.models import Clients, Orders, Staff, Categories


@csrf_exempt
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
    result = [{
        "id": i.pk,
        "client_id": i.client.pk,
        "staff_in_id": i.staff_in_id,
        "executor_id": i.executor_id,
        "category_id": i.category_id,
        "staff_out": i.staff_out_id,
        "title": i.title,
        "description": i.description,
        "status": i.status,
        "categoryTitle": i.category.name,
        "client_FN": i.client.get_client_fio(),
        "client_phone": i.client.phone_number,
        "staff_in_FN": i.staff_in.get_staff_fio(),
        "executor_FN": i.get_executor_fio(),
        "staff_out_FN": i.get_staff_out_fio(),
        "created_at": i.created_at,
        "repair_at": i.get_repair_date(),
        "closed_at": i.get_closed_date(),
    } for i in Orders.objects.all().select_related('category', 'staff_in', 'staff_out', 'executor', 'client')]
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
        order = Orders.objects.get(id = data['id'])
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


