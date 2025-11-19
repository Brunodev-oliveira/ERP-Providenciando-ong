from django.urls import path
from donations.views import donation_list, donation_details, donation_register, unique_donation_register

app_name = 'donations'

urlpatterns = [
    path('', donation_list, name='Doação'),
    path('<int:pk>/', donation_details, name='detalhes_doação'),
    path('register/', donation_register, name='registrar_doaçoẽs'),
    path('register/<int:pk>/',unique_donation_register, name='doação_unitaria'),


   

]


