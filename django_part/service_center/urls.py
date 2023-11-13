from .api import RolesViewSet, AccountsViewSet, AccountsRolesViewSet, StaffViewSet, ClientsViewSet, CategoriesViewSet, OrdersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('roles', RolesViewSet, 'roles')
router.register('accounts', AccountsViewSet, 'accounts')
router.register('accounts_roles', AccountsRolesViewSet, 'accounts_roles')
router.register('staff', StaffViewSet, 'staff')
router.register('clients', ClientsViewSet, 'clients')
router.register('categories', CategoriesViewSet, 'categories')
router.register('orders', OrdersViewSet, 'orders')

urlpatterns = router.urls