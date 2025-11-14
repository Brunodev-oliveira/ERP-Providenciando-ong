from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier


def supplier_list (request):
    suppliers = Supplier.objects.all()

    return render(request, 'suppliers-list.html', {'suppliers' : suppliers} )



def supplier_details(request, pk):

    supplier = get_object_or_404(Supplier, pk = pk)

    return render(request, 'suppliers-details.html', { 'supplier': supplier })



def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier,pk = pk)

    if request.method == 'POST':
        supplier.delete()
        
        redirect('Fornecedores')




def stock_entry(request):
    return render(request,'stock-entry.html')


