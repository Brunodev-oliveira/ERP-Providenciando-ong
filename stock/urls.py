from django.urls import path
from .views import supplier_list, supplier_details, stock_entry,supplier_form,supplier_edit




app_name = 'stock'


urlpatterns = [
    path('list/',supplier_list, name='Fornecedores'),
    path('<int:pk>/',supplier_details,name='detalhes_Fornecedores'),   
    path('append/',stock_entry, name='entradas'),
    path('register/',supplier_form, name='form_fornecedor'),
    path('<int:pk>/edit/', supplier_edit, name='editar_fornecedor'),  

]
