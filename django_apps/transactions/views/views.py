from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.exceptions import FinanceAPIException, ErrorCode
from utils.mixins import ResponseMixin
from rest_framework import serializers
from django_apps.transactions.models import Category, Transaction
from django_apps.transactions.services import CategoryService

# Create your views here.
class CategoryView(ResponseMixin, APIView):
    authentication_classes = []  # Sin autenticación
    permission_classes = [] 

    class CategoryInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ['name', 'type', 'description']
    
    class CategoryOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ['id', 'name', 'type', 'description']

    def post(self, request):
        in_serializer = self.CategoryInputSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)
        data = CategoryService.create(**in_serializer.validated_data)
        print(data)
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