from django.urls import path, include
from . import views

# add urls for views
urlpatterns = [
    path('', views.index, name='payment_page'),    
]

    