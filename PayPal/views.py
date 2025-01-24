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
    """A homepage view to input the user's details for the PayPal transaction.

    :param request: The HTTP request object containing information about the client's request.
    :type request: HttpRequest
    :return: Return the index template
    :rtype: HttpResponse
    """
    context = {'PAYPAL_CLIENT_ID': os.environ.get('PAYPAL_CLIENT_ID')}    
    return render(request, 'payment/index.html', context)
