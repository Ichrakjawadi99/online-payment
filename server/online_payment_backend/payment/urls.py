# payment/urls.py
from django.urls import path
from .views import SignUpView, SignInView, ProcessPaymentView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('process-payment/', ProcessPaymentView.as_view(), name='process-payment'),
]
