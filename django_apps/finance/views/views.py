from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.exceptions import FinanceAPIException, ErrorCode
from utils.mixins import ResponseMixin
from rest_framework import serializers
from django_apps.finance.models import Balance, Budget
from django_apps.finance.services import BalanceService, BudgetService

# Create your views here.
class BalanceView(ResponseMixin, APIView):
    authentication_classes = []  # Sin autenticación por ahora
    permission_classes = [] 

    class BalanceInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Balance
            fields = ['user', 'available_balance']
    
    class BalanceOutputSerializer(serializers.ModelSerializer):
        user = serializers.StringRelatedField()
        
        class Meta:
            model = Balance
            fields = ['id', 'user', 'available_balance', 'created_at', 'updated_at']

    def post(self, request):
        
        in_serializer = self.BalanceInputSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)
        
        data = BalanceService.create(**in_serializer.validated_data)
        try:
            out_serializer = self.BalanceOutputSerializer(data)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.B00.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_201_CREATED
        )
    
    
class BalanceDetailView(ResponseMixin, APIView):
    authentication_classes = []  # Sin autenticación por ahora
    permission_classes = [] 

    class BalanceDetailOutputSerializer(serializers.ModelSerializer):
        user = serializers.StringRelatedField()
        
        class Meta:
            model = Balance
            fields = ['id', 'user', 'available_balance', 'created_at', 'updated_at']

    class BalanceUpdateInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Balance
            fields = ['available_balance']
            extra_kwargs = {
                'available_balance': {'required': False}
            }

    def get(self, request, balance_id):
        
        balance = BalanceService.get_by_id(balance_id)
        if not balance:
            raise FinanceAPIException(
                error_code=ErrorCode.B01.value
            )
        try:
            out_serializer = self.BalanceDetailOutputSerializer(balance)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.B02.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def put(self, request, balance_id):
        
        balance = BalanceService.get_by_id(balance_id)
        if not balance:
            raise FinanceAPIException(
                error_code=ErrorCode.B01.value
            )
        update_serializer = self.BalanceUpdateInputSerializer(
            instance=balance,
            data=request.data,
            partial=True
        )
        update_serializer.is_valid(raise_exception=True)
        data = BalanceService.update(balance_id, **update_serializer.validated_data)
        try:
            out_serializer = self.BalanceDetailOutputSerializer(data)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.B03.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_200_OK
        )


class BudgetView(ResponseMixin, APIView):
    authentication_classes = []  # Sin autenticación por ahora
    permission_classes = [] 

    class BudgetInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Budget
            fields = ['user', 'monthly_income', 'monthly_expenses', 'actual_savings']
    
    class BudgetOutputSerializer(serializers.ModelSerializer):
        user = serializers.StringRelatedField()
        
        class Meta:
            model = Budget
            fields = ['id', 'user', 'monthly_income', 'monthly_expenses', 'suggested_savings', 'actual_savings', 'created_at', 'updated_at']

    def post(self, request):
        in_serializer = self.BudgetInputSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)
        
        data = BudgetService.create(**in_serializer.validated_data)
        try:
            out_serializer = self.BudgetOutputSerializer(data)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.B00.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_201_CREATED
        )
    
    
class BudgetDetailView(ResponseMixin, APIView):
    authentication_classes = []  # Sin autenticación por ahora
    permission_classes = [] 

    class BudgetDetailOutputSerializer(serializers.ModelSerializer):
        user = serializers.StringRelatedField()
        
        class Meta:
            model = Budget
            fields = ['id', 'user', 'monthly_income', 'monthly_expenses', 'suggested_savings', 'actual_savings', 'created_at', 'updated_at']

    class BudgetUpdateInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Budget
            fields = ['monthly_income', 'monthly_expenses', 'actual_savings']
            extra_kwargs = {
                'monthly_income': {'required': False},
                'monthly_expenses': {'required': False},
                'actual_savings': {'required': False}
            }

    def get(self, request, budget_id):
        budget = BudgetService.get_by_id(budget_id)
        if not budget:
            raise FinanceAPIException(
                error_code=ErrorCode.B01.value
            )
        try:
            out_serializer = self.BudgetDetailOutputSerializer(budget)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.B02.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def put(self, request, budget_id):
        budget = BudgetService.get_by_id(budget_id)
        if not budget:
            raise FinanceAPIException(
                error_code=ErrorCode.B01.value
            )
        update_serializer = self.BudgetUpdateInputSerializer(
            instance=budget,
            data=request.data,
            partial=True
        )
        update_serializer.is_valid(raise_exception=True)
        data = BudgetService.update(budget_id, **update_serializer.validated_data)
        try:
            out_serializer = self.BudgetDetailOutputSerializer(data)
        except Exception as e:
            raise FinanceAPIException(
                error_code=ErrorCode.B03.value
            )
        return Response(
            data=out_serializer.data, 
            status=status.HTTP_200_OK
        )
