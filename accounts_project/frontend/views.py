from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
apiEndpoint = 'http://127.0.0.1:8000/api/invoice/'

apiEndpoint2 = 'http://127.0.0.1:8000/api/invoice/'

def home(request):
    invoice = requests.get(apiEndpoint).json()
    context = {'invoice':invoice,

               }

    return render(request, 'home.html', context)


def select_invoice(request, id):
    
    invoice = requests.get(apiEndpoint + str(id)).json()
    context = {'invoice': invoice,}
    
    return render(request, 'invoice_info.html', context)

