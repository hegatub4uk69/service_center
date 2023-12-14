from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('token-verify', views.token_verify),
    path('get-token', obtain_auth_token, name='token'),
    path('get-clients', views.get_clients),
    path('get-orders', views.get_orders),
    path('get-categories', views.get_categories),
    path('add-order', views.add_order),
    path('update-order', views.update_order),
    path('delete-order', views.delete_order),
    path('get-order-other-data', views.get_other_order_data),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
