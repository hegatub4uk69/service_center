from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('get-staff-data', views.get_staff),
    path('get-token', obtain_auth_token, name='token'),
    path('get-clients', views.get_clients),
    path('get-orders', views.get_orders),
    path('get-categories', views.get_categories),
    path('get-order-other-data', views.get_other_order_data),

    path('add-order', views.add_order),
    path('add-client', views.add_client),

    path('update-order', views.update_order),
    path('update-client', views.update_client),

    path('delete-order', views.delete_order),
    path('delete-client', views.delete_client),

    path('token-verify', views.token_verify),
    re_path(r'^auth/', include('djoser.urls.base')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
