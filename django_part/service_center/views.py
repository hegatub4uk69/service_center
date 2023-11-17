"""
Используется для первого метода работы с данными.
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from service_center.models import Clients, Orders, Staff, Categories


@csrf_exempt
def get_clients(request):
    result = [{
        "pk": i.pk,
        "lastName": i.last_name,
        "firsName": i.first_name
    } for i in Clients.objects.all()]
    return JsonResponse({"result": result})


@csrf_exempt
def get_categories(request):
    result = [{
        "pk": i.pk,
        "name": i.name,
    } for i in Categories.objects.all()]
    return JsonResponse({"result": result})


@csrf_exempt
def get_staff(request):
    result = [{
        "pk": i.pk,
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
        "staff_out": i.staff_out_id,
        "title": i.title,
        "description": i.description,
        "status": i.status,
        "categoryTitle": i.category.name,
        "client_FN": i.client.get_client_fio(),
        "client_phone": i.client.phone_number,
        "staff_in_FN": i.staff_in.get_staff_fio(),
        "executor_FN": i.executor.get_staff_fio(),
    } for i in Orders.objects.all().select_related('category', 'staff_in', 'staff_out', 'executor', 'client')]
    return JsonResponse({"result": result})
