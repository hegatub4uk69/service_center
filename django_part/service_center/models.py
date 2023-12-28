from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    last_name = models.CharField(max_length=25, null=False, blank=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    father_name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    account = models.ForeignKey(User, related_name='Staff_account_id', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.phone_number

    def get_staff_fio(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

class Clients(models.Model):
    last_name = models.CharField(max_length=25, null=False, blank=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    father_name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)

    def get_client_fio(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

    def __str__(self):
        return self.phone_number

class Categories(models.Model):
    name = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    NEW = 'Новый'
    WORK = 'В работе'
    DONE = 'Готов'
    GIVEN = 'Выдан'
    CATEGORIES = [
        (NEW, "Новый"), (WORK, "В работе"), (DONE, "Готов"), (GIVEN, "Выдан")
    ]

    title = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, null=True, blank=False, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=CATEGORIES, default=NEW)
    client = models.ForeignKey(Clients, related_name='Orders_client_id', null=True, blank=False, on_delete=models.CASCADE)
    staff_in = models.ForeignKey(Staff, related_name='Orders_staff_in_id', null=True, blank=False, on_delete=models.SET_NULL)
    executor = models.ForeignKey(Staff, related_name='Orders_executor_id', null=True, blank=True, on_delete=models.SET_NULL)
    staff_out = models.ForeignKey(Staff, related_name='Orders_staff_out_id', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    repair_at = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    closed_at = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_repair_date(self):
        if self.repair_at is not None:
            return self.repair_at
        else:
            return f'Отсутствует'
    def get_closed_date(self):
        if self.closed_at is not None:
            return self.closed_at
        else:
            return f'Отсутствует'

    def get_executor_fio(self):
        if self.executor is not None:
            return f'{self.executor.last_name} {self.executor.first_name} {self.executor.father_name}'
        else:
            return f'Не определён'

    def get_staff_out_fio(self):
        if self.staff_out is not None:
            return f'{self.staff_out.last_name} {self.staff_out.first_name} {self.staff_out.father_name}'
        else:
            return f'Не определён'