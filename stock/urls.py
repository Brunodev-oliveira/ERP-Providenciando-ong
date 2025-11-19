from django.urls import path
from .views import supplier_list, supplier_details, stock_entry,supplier_form,supplier_edit, stock_entry_form,supplier_delete

#  NÃO APAGAR FIX PARA: BRUNO 
# from .views import supplier_list, supplier_details, stock_entry, supplier_delete




app_name = 'stock'


urlpatterns = [
    # path('list/',supplier_list, name='Fornecedores'),
    # path('<int:pk>/',supplier_details,name='detalhes_Fornecedores'),   
    # path('append/<int:stock_id>/',stock_entry, name='entradas'),
    # path('register/',supplier_form, name='form_fornecedor'),
    # path('<int:pk>/edit/', supplier_edit, name='editar_fornecedor'), 



    #  NÃO APAGAR FIX PARA: BRUNO 
    # path('<int:pk>/',supplier_details,name='detalhes_Fornecedores'), 
    # path('delete/<int:pk>/',supplier_delete,name='deletar_Fornecedores'),  
    # path('append/',stock_entry, name='entradas'),   


    path('suppliers/list/',supplier_list, name='fornecedores'),
    path('suppliers/<int:pk>/',supplier_details, name='detalhes_fornecedores'),   
    path('suppliers/register/',supplier_form, name='form_fornecedor'),
    path('suppliers/<int:pk>/edit/',supplier_edit, name='editar_fornecedor'),
    path('suppliers/delete/<int:pk>/',supplier_delete,name='deletar_Fornecedores'),  

    
    # URLs de entradas
    path('entries/append/<int:stock_id>/',stock_entry, name='aplicar_entradas'),
    path('entries/', stock_entry_form, name='entradas'),
    
]
