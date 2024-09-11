# inventory/urls.py
from django.http import HttpResponseRedirect
from django.urls import path
from .views import InventoryListCreate, InventoryRetrieveUpdateDestroy

urlpatterns = [
    path('inventory/', InventoryListCreate.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryRetrieveUpdateDestroy.as_view(), name='inventory-detail'),
     path('', lambda request: HttpResponseRedirect('/inventory/'))
]
