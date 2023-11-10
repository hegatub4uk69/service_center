from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name

class Accounts(models.Model):
    login = models.CharField(max_length=45, null=False, blank=False)
    password = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.login

class Accounts_Roles(models.Model):
    account_id = models.ForeignKey(Accounts, related_name='Accounts_Roles_account_id', null=True, blank=True, on_delete=models.SET_NULL)
    role_id = models.ForeignKey(Roles, related_name='Accounts_Roles_role_id', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.account_id

class Staff(models.Model):
    last_name = models.CharField(max_length=25, null=False, blank=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    father_name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    account_id = models.ForeignKey(Accounts, related_name='Staff_account_id', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.phone_number

class Clients(models.Model):
    last_name = models.CharField(max_length=25, null=False, blank=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    father_name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    def __str__(self):
        return self.phone_number

class Categories(models.Model):
    name = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    NEW = 'N'
    WORK = 'W'
    DONE = 'D'
    GIVEN = 'G'
    DECLINE = 'DC'
    CATEGORIES = [
        (NEW, "Новый"), (WORK, "В работе"), (DONE, "Готов"), (GIVEN, "Выдан"), (DECLINE, "Отклонён")
    ]

    title = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, null=True, blank=False, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=CATEGORIES, default=NEW)
    client = models.ForeignKey(Clients, related_name='Orders_client_id', null=True, blank=False, on_delete=models.SET_NULL)
    staff_in = models.ForeignKey(Staff, related_name='Orders_staff_in_id', null=True, blank=False, on_delete=models.SET_NULL)
    executor_id = models.ForeignKey(Staff, related_name='Orders_executor_id', null=True, blank=True, on_delete=models.SET_NULL)
    staff_out = models.ForeignKey(Staff, related_name='Orders_staff_out_id', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    repair_at = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    closed_at = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title
