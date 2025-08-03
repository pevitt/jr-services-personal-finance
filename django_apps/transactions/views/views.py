from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.exceptions import FinanceAPIException, ErrorCode
from utils.mixins import ResponseMixin
from rest_framework import serializers
from django_apps.transactions.models import Category, Transaction
from django_apps.transactions.services import CategoryService
from django_apps.transactions.serializers import TransactionInputSerializer, TransactionOutputSerializer, TransactionUpdateSerializer
from django_apps.transactions.services import TransactionService
from utils.pagination import CustomPagination
from utils.decorators import validate_uuid_param

# Create your views here.
class CategoryView(ResponseMixin, APIView):
    http_method_names = ['post', 'get']
    authentication_classes = []  # Sin autenticación
    permission_classes = [] 

    class CategoryInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ['name', 'type', 'description']
        
        def validate(self, attrs):
            name = attrs.get('name')
            category_type = attrs.get('type')
            if CategoryService.get_by_filters(name=name, type=category_type).first():
                raise FinanceAPIException(
                    error_code=ErrorCode.C04.value
                )
            
            return attrs
    
    class CategoryOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ['id', 'name', 'type', 'description']

    def post(self, request):
        in_serializer = self.CategoryInputSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)
        data = CategoryService.create(**in_serializer.validated_data)
        try:
            out_serializer = self.CategoryOutputSerializer(data)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.C00.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_201_CREATED
        )
    
    def get(self, request):

        category_type = request.query_params.get('category_type')
        name = request.query_params.get('name')
        description = request.query_params.get('description')
        filters = {}
        if category_type:
            filters['category_type'] = category_type
        if name:
            filters['name'] = name
        if description:
            filters['description'] = description
        categories = CategoryService.get_by_filters(**filters)

        try:
            out_serializer = self.CategoryOutputSerializer(categories, many=True)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.C02.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_200_OK
        )
    
class CategoryDetailView(ResponseMixin, APIView):
    http_method_names = ['get', 'put']
    authentication_classes = []  # Sin autenticación
    permission_classes = [] 

    class CategoryDetailOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ['id', 'name', 'type', 'description']

    class CategoryUpdateInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ['name', 'type', 'description']
            extra_kwargs = {
                'name': {'required': False},
                'type': {'required': False},
                'description': {'required': False}
            }

    @validate_uuid_param('category_id')
    def get(self, request, category_id):
        category = CategoryService.get_by_id(category_id)
        if not category:
            raise FinanceAPIException(
                error_code=ErrorCode.C01.value
            )
        try:
            out_serializer = self.CategoryDetailOutputSerializer(category)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.C02.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_200_OK
        )
    
    @validate_uuid_param('category_id')
    def put(self, request, category_id):
        category = CategoryService.get_by_id(category_id)
        if not category:
            raise FinanceAPIException(
                error_code=ErrorCode.C03.value
            )
        update_serializer = self.CategoryUpdateInputSerializer(
            instance=category,
            data=request.data,
            partial=True
        )
        update_serializer.is_valid(raise_exception=True)
        data = CategoryService.update(category_id, **update_serializer.validated_data)
        try:
            out_serializer = self.CategoryDetailOutputSerializer(data)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.C02.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_200_OK
        )

class TransactionView(ResponseMixin, APIView):
    http_method_names = ['post', 'get']
    pagination_class = CustomPagination
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        in_serializer = TransactionInputSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)
        try:
            transaction = TransactionService.create(**in_serializer.validated_data)
            out_serializer = TransactionOutputSerializer(transaction)
        except FinanceAPIException as e:
            raise e
        except Exception as e:  
            raise FinanceAPIException(error_code=ErrorCode.T00.value)
        return Response(out_serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        try:
            balance_id = request.query_params.get('balance_id')
            description = request.query_params.get('description')
            category_id = request.query_params.get('category_id')
            filters = {}
            if balance_id:
                filters['balance_id'] = balance_id
            if description:
                filters['description'] = description
            if category_id:
                filters['category_id'] = category_id
            
            print(filters)

            transactions = TransactionService.get_by_filters(**filters)
            paginator = self.pagination_class()
            paginated_data = paginator.paginate_queryset(transactions, request)
            out_serializer = TransactionOutputSerializer(paginated_data, many=True)
        except Exception:
            raise FinanceAPIException(error_code=ErrorCode.B02.value)
        return paginator.get_paginated_response(out_serializer.data)

class TransactionDetailView(ResponseMixin, APIView):
    http_method_names = ['get', 'put']
    authentication_classes = []
    permission_classes = []

    @validate_uuid_param('transaction_id')
    def get(self, request, transaction_id):
        transaction = TransactionService.get_by_id(transaction_id)
        if not transaction or not transaction.is_active:
            raise FinanceAPIException(error_code=ErrorCode.B01.value)
        try:
            out_serializer = TransactionOutputSerializer(transaction)
        except Exception:
            raise FinanceAPIException(error_code=ErrorCode.B02.value)
        return Response(out_serializer.data, status=status.HTTP_200_OK)

    @validate_uuid_param('transaction_id')
    def put(self, request, transaction_id):
        transaction = TransactionService.get_by_id(transaction_id)
        if not transaction or not transaction.is_active:
            raise FinanceAPIException(error_code=ErrorCode.B01.value)
        update_serializer = TransactionUpdateSerializer(
            instance=transaction,
            data=request.data,
            partial=True
        )
        update_serializer.is_valid(raise_exception=True)
        try:
            updated = TransactionService.update(transaction_id, **update_serializer.validated_data)
            out_serializer = TransactionOutputSerializer(updated)
        except Exception:
            raise FinanceAPIException(error_code=ErrorCode.B03.value)
        return Response(out_serializer.data, status=status.HTTP_200_OK)

    @validate_uuid_param('balance_id')
    def delete(self, request, transaction_id):
        transaction = TransactionService.get_by_id(transaction_id)
        if not transaction or not transaction.is_active:
            raise FinanceAPIException(error_code=ErrorCode.T02.value)
        try:
            transaction.delete()  # Soft delete
        except Exception:
            raise FinanceAPIException(error_code=ErrorCode.B03.value)
        return Response({"message": "Transaction deleted (soft delete)"}, status=status.HTTP_204_NO_CONTENT)