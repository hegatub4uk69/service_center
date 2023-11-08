from django.db import models

class Orders(models.Model):
    CATEGORIES = [
        "Новый", "В работе", "Готов", "Выдан", "Отклонён"
    ]

    title = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Categories', null=True, blank=False, on_delete=models.SET_NULL)
    client = models.ForeignKey('Clients', null=True, blank=False, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=CATEGORIES, default="Новый")
    staff_in = models.ForeignKey('Staff', null=True, blank=False, on_delete=models.SET_NULL)
    executor_id = models.ForeignKey('Staff', null=True, blank=True, on_delete=models.SET_NULL)
    staff_out = models.ForeignKey('Staff', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateField()
    repair_at = models.DateField()
    closed_at = models.DateField()
class Clients(models.Model):
    last_name = models.CharField()
    first_name = models.CharField()
    father_name = models.CharField()
    phone_number = models.CharField()
class Categories(models.Model):
    name = models.CharField()
class Staff(models.Model):
    last_name = models.CharField()
    first_name = models.CharField()
    father_name = models.CharField()
    phone_number = models.CharField()
    account_id = models.ForeignKey('Accounts', null=True, blank=True, on_delete=models.SET_NULL)
class Accounts(models.Model):
    login = models.CharField()
    password = models.CharField()
class Accounts_Roles(models.Model):
    account_id = models.ForeignKey('Accounts', null=True, blank=True, on_delete=models.SET_NULL)
    role_id = models.ForeignKey('Roles', null=True, blank=True, on_delete=models.SET_NULL)
class Roles(models.Model):
    name = models.CharField()
