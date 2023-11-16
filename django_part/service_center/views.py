"""
Используется для первого метода работы с данными.
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from service_center.models import Clients, Orders, Staff


@csrf_exempt
def get_clients(request):
    result = [{
        "pk": i.pk,
        "lastName": i.last_name,
        "firsName": i.first_name
    } for i in Clients.objects.all()]
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
        "pk": i.pk,
        "title": i.title,
        "description": i.description,
        "status": i.status,
        "categoryTitle": i.category.name,
        "clientLastName": i.client.last_name
    } for i in Orders.objects.all().select_related('category', 'staff_in', 'staff_out', 'executor', 'client')]
    return JsonResponse({"result": result})