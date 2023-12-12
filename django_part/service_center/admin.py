from django.contrib import admin
# from .models import Roles, Accounts, Accounts_Roles, Staff, Clients, Categories, Orders
from .models import Staff, Clients, Categories, Orders

# @admin.register(Roles)
# class RolesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id',)
#     search_fields = ('id', 'name')
#     list_editable = ('name',)
#     list_filter = ('name',)
# @admin.register(Accounts)
# class AccountsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'login', 'password')
#     list_display_links = ('id',)
#     search_fields = ('id', 'login')
#     list_editable = ('login', 'password')
#     list_filter = ('login',)
# @admin.register(Accounts_Roles)
# class AccountsRolesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'account', 'role')
#     list_display_links = ('id',)
#     search_fields = ('id', 'account', 'role')
#     list_editable = ('account', 'role')
#     list_filter = ('account', 'role')
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'father_name', 'phone_number', 'account')
    list_display_links = ('id',)
    search_fields = ('id', 'last_name', 'first_name', 'father_name', 'phone_number')
    list_editable = ('last_name', 'first_name', 'father_name', 'phone_number', 'account')
    list_filter = ('last_name', 'first_name', 'father_name', 'phone_number')
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'father_name', 'phone_number')
    list_display_links = ('id',)
    search_fields = ('id', 'last_name', 'first_name', 'father_name', 'phone_number')
    list_editable = ('last_name', 'first_name', 'father_name', 'phone_number')
    list_filter = ('last_name', 'first_name', 'father_name', 'phone_number')
@admin.register(Categories)
class Categories(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('id', 'name')
    list_editable = ('name',)
    list_filter = ('name',)
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'status', 'client',
                    'staff_in', 'executor', 'staff_out', 'created_at', 'repair_at', 'closed_at')
    list_display_links = ('id',)
    search_fields = ('id', 'title', 'description', 'category', 'status', 'client',
                    'staff_in', 'executor', 'staff_out', 'created_at', 'repair_at', 'closed_at')
    list_editable = ('title', 'description', 'category', 'status', 'client',
                    'staff_in', 'executor', 'staff_out', 'created_at', 'repair_at', 'closed_at')
    list_filter = ('title', 'description', 'category', 'status', 'client',
                    'staff_in', 'executor', 'staff_out', 'created_at', 'repair_at', 'closed_at')
