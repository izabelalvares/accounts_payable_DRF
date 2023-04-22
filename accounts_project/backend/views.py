from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Invoice
from .serializers import InvoiceSerializer


@api_view(['GET'])

def Invoice_list(request):
    
    if request.method == 'GET':
        invoice = Invoice.objects.all()
        serializer = InvoiceSerializer(invoice, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])

def invoice_detail(request, id):
    if request.method == 'GET':
        data = Invoice.objects.get(id = id)
        serializer = InvoiceSerializer(data)
        return Response(serializer.data)

