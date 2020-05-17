from django.urls import path
from .views import Produtos_list, Produtos_new, Produtos_update, Produtos_delete

urlpatterns = [
    path('', Produtos_list, name='produtos_list'),
    path('new/', Produtos_new, name='produtos_new'),
    path('update/<int:id>', Produtos_update, name='produtos_update'),
    path('delete/<int:id>', Produtos_delete, name='produtos_delete'),
]
