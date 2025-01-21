from django.urls import path, include
from . import views

# add urls for views
urlpatterns = [
    path('', views.index, name='payment_page'),
    path('create/', views.create_payment, name='create_payment'),    
    path('success/', views.payment_success, name='payment_success'),    
    ]