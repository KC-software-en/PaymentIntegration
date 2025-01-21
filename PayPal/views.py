from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .utils import configure_paypal
import paypalrestsdk

###############################################################################

# configure paypal sdk
configure_paypal()

# Create your views here.
# create a view for the index template
def index(request):
    return render(request, 'payment/index.html')

# create a view for the payment
def create_payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')

        # create a payment
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal",
                "payer_info": {
                    "email": email
                }
            },
            # generate complete absolute URLs including domain - needed for when Paypal redirects after successful payment
            "redirect_urls": {
                "return_url": request.build_absolute_uri("/payment/success/"),
                "cancel_url": request.build_absolute_uri("/payment/cancel/"),
            },
            "transactions": [{
                "amount": {
                    "total": amount,
                    "currency": "USD"
                },
                "description": "Payment for " + name
            }]            
        })

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":                    
                    return JsonResponse({"approval_url": link.href})
                else:
                    return JsonResponse({"error": payment.error})
                
            return JsonResponse({"error": "Unknown error occurred"})
        
# success view
def payment_success(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'payment/success.html', {"payment": payment})
    else:
        return render(request, 'payment/cancel.html')        

'''
# create an order
def create_order(request):
    
            headers = {
                'Content-Type': 'application/json',
                'PayPal-Request-Id': '7b92603e-77ed-4896-8e78-5dea2050476a',
                'Authorization': 'Bearer """ ENTER TOKEN """',
            }
    
            data = '{ "intent": "CAPTURE", "purchase_units": [ { "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b", "amount": { "currency_code": "USD", "value": "100.00" } } ], "payment_source": { "paypal": { "experience_context": { "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED", "brand_name": "EXAMPLE INC", "locale": "en-US", "landing_page": "LOGIN", "shipping_preference": "SET_PROVIDED_ADDRESS", "user_action": "PAY_NOW", "return_url": "https://example.com/returnUrl", "cancel_url": "https://example.com/cancelUrl" } } } }'
    
            response = requests.post('https://api-m.sandbox.paypal.com/v2/checkout/orders', headers=headers, data=data)


        # confirm order
        headers = {
            'Authorization': 'Bearer """ ENTER TOKEN """',
        }

        data = '{ "payment_source": { "paypal": { "name": { "given_name": "John", "surname": "Doe" }, "email_address": "customer@example.com", "experience_context": { "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED", "brand_name": "EXAMPLE INC", "locale": "en-US", "landing_page": "LOGIN", "shipping_preference": "SET_PROVIDED_ADDRESS", "user_action": "PAY_NOW", "return_url": "https://example.com/returnUrl", "cancel_url": "https://example.com/cancelUrl" } } } }'

        response = requests.post('https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/confirm-payment-source', headers=headers, data=data)

# set up token
headers = {
    'Authorization': 'Bearer """ ENTER TOKEN """',
    'Content-Type': 'application/json',
    'PayPal-Request-ID': 'b5efbe82-bbad-4bb0-aeeb-bfef5b442e49',
}

data = '{ "payment_source": { "card": { "number": "4111111111111111", "expiry": "2027-02", "name": "John Doe", "billing_address": { "address_line_1": "2211 N First Street", "address_line_2": "17.3.160", "admin_area_1": "CA", "admin_area_2": "San Jose", "postal_code": "95131", "country_code": "US" }, "experience_context": { "brand_name": "YourBrandName", "locale": "en-US", "return_url": "https://example.com/returnUrl", "cancel_url": "https://example.com/cancelUrl" } } } }'

response = requests.post('https://api-m.sandbox.paypal.com/v3/vault/setup-tokens', headers=headers, data=data)

# show order details
    headers = {
            'Authorization': 'Bearer """ ENTER TOKEN """',
        }

        response = requests.get('https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T', headers=headers)
'''
