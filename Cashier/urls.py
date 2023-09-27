from .views import ProductView,TransactionView
from django.urls import path

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),
    path('pay/', TransactionView.as_view(), name='pay'),
]