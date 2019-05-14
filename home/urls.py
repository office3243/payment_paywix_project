from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('payment/success', views.payment_success, name='payment_success'),
    path('payment/failure', views.payment_failure, name='payment_failure')

]
