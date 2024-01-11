from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('get-staff-data', views.get_staff),
    path('get-token', obtain_auth_token, name='token'),
    path('get-clients', views.get_clients),
    path('get-clients-for-adm', views.get_clients_for_adm),
    path('get-orders', views.get_orders),
    path('get-my-orders', views.get_my_orders),
    path('get-my-orders-count', views.get_my_orders_count),
    path('get-categories', views.get_categories),
    path('get-order-other-data', views.get_other_order_data),

    path('add-order', views.add_order),
    path('add-client', views.add_client),

    path('update-order', views.update_order),
    path('update-client', views.update_client),
    path('take-order', views.take_order),
    path('order-done', views.order_done),
    path('order-out', views.order_out),

    path('delete-order', views.delete_order),
    path('delete-client', views.delete_client),

    path('token-verify', views.token_verify),
    re_path(r'^auth/', include('djoser.urls.base')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
