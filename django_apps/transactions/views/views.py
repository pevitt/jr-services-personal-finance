from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.exceptions import FinanceAPIException, ErrorCode
from rest_framework import serializers
from django_apps.transactions.models import Category, Transaction
from django_apps.transactions.services import CategoryService

# Create your views here.
class CategoryView(APIView):
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