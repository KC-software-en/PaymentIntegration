import paypalrestsdk

# import os to access environment variables
import os

#####################################################################################

# configure paypal sdk
def configure_paypal():
    """A function that configures the PayPal SDK with the client ID and client secret from environment variables.

    :return: Return the configured PayPal SDK.
    :rtype: paypalrestsdk.Api
    """
    # get the client ID and client secret from environment variables
    client_id = os.environ.get('PAYPAL_CLIENT_ID')
    client_secret = os.environ.get('PAYPAL_CLIENT_SECRET')

    # configure the PayPal SDK with the client ID and client secret
    paypalrestsdk.configure({
        "mode": "sandbox",  # sandbox or live
        "client_id": client_id,
        "client_secret": client_secret
    })

    # return the configured PayPal SDK
    return paypalrestsdk.Api
