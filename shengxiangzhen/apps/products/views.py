# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

def main(request):
    products = Product.objects.all();
    for i in range(0,len(products)):
        products[i].productImage = str(products[i].productImage).split('/')[-1]
    rc = RequestContext(request,{'products':products})
    return render_to_response('index.html',context_instance=rc);
    
def contact(request):
    rc = RequestContext(request, {'prob':'1'},)
    return render_to_response('contact.html', context_instance=rc)

def brandintro(request):
    rc = RequestContext(request, {'prob':'1'},)
    return render_to_response('brandintro.html', context_instance=rc)
