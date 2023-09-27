from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,

)
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User, Product, Transaction_items, Transaction
from .serializers import UserSerializer, ProductSerializer, PaymentSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.timezone import make_aware
from datetime import datetime

# Create your views here.


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TransactionView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request):
        serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            payment_items = serializer.validated_data['items']

            transaction = Transaction.objects.create(
                cashier=request.user,
                number_of_items=len(payment_items)
            )

            for payment_item in payment_items:
                product_id = payment_item['id']
                quantity = payment_item['qty']

                try:
                    product = Product.objects.get(id=product_id)
                except Product.DoesNotExist:
                    return Response(f"Product with ID {product_id} does not exist.", status=status.HTTP_404_NOT_FOUND)

                Transaction_items.objects.create(
                    item=product,
                    quantity=quantity,
                    transaction=transaction
                )

            return Response("Transaction created successfully.", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Transaction.objects.all()
        cashier_id = self.request.query_params.get('cashier')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if cashier_id:
            queryset = queryset.filter(cashier_id=cashier_id)

        if start_date and end_date:
            start_date = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
            end_date = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
            queryset = queryset.filter(
                transaction_time__gte=start_date, transaction_time__lte=end_date)

        return queryset
