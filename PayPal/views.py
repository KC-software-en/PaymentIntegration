# display templates with render
from django.shortcuts import render

# import PayPal setup 
from .utils import configure_paypal

# access .env variables with os import
import os

###############################################################################

# configure paypal sdk
configure_paypal()

# create a view for the index template
def index(request):
    context = {'PAYPAL_CLIENT_ID': os.getenv('PAYPAL_CLIENT_ID')}    
    return render(request, 'payment/index.html', context)
