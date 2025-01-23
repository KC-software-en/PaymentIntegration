# import paypalrestsdk for PayPal methods that create, process & manage payments
import paypalrestsdk

# import os to access environment variables
import os

# import load_dotenv to load environment variables from .env file
from dotenv import load_dotenv

##############################################################################################

# configure paypal sdk
def configure_paypal():
    """A function that configures the PayPal SDK with the client ID and client secret from environment variables.

    :return: Return the configured PayPal SDK.
    :rtype: paypalrestsdk.Api
    """
    # load environment variables from .env file
    # call load_dotenv method to read the .env file & make the content available to os.getenv
    load_dotenv()

    # get the client ID, client secret & PayPal mode from environment variables
    client_id = os.getenv('PAYPAL_CLIENT_ID')    
    client_secret = os.getenv('PAYPAL_CLIENT_SECRET')    
    paypal_mode = os.getenv('PAYPAL_MODE')    

    # configure the PayPal SDK with the client ID and client secret
    paypalrestsdk.configure({
        "mode": paypal_mode,  # sandbox or live 
        "client_id": client_id,
        "client_secret": client_secret
    })
    
