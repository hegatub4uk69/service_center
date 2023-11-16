"""
Используется для второго метода работы с данными.
"""
from .models import Roles, Accounts, Accounts_Roles, Staff, Clients, Categories, Orders
from .serializers import RolesSerializer, AccountsSerializer, AccountsRolesSerializer, StaffSerializer, ClientsSerializer, CategoriesSerializer, OrdersSerializer
from rest_framework import viewsets, permissions

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    permission_classes = [ permissions.AllowAny ]
    serializer_class = RolesSerializer

class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    permission_classes = [ permissions.AllowAny ]
    serializer_class = AccountsSerializer

class AccountsRolesViewSet(viewsets.ModelViewSet):
    queryset = Accounts_Roles.objects.all()
    permission_classes = [ permissions.AllowAny ]
    serializer_class = AccountsRolesSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    permission_classes = [ permissions.AllowAny ]
    serializer_class = StaffSerializer

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    permission_classes = [ permissions.AllowAny ]
    serializer_class = ClientsSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    permission_classes = [ permissions.AllowAny ]
    serializer_class = CategoriesSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    permission_classes = [ permissions.AllowAny ]
    serializer_class = OrdersSerializer