from django.urls import path
from . import views


urlpatterns = [
    path(r'invoice/', views.Invoice_list, name='invoice'), #go to 8000/api/invoice
    path(r'invoice/<int:id>/', views.invoice_detail, name = 'invoice_detail'),
   
]
