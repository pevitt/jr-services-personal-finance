from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_apps.authentication import services as auth_services
from django_apps.authentication.models import CustomUser
from utils.exceptions import ErrorCode, FinanceAPIException


# Create your views here.
class SignUpView(APIView):
    """
    View for signing up a new user.
    """

    class SignUpSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = [
                "first_name",
                "last_name",
                "email",
                "password",
                "nickname",
                "document_type",
                "document_number",
            ]

            def validate_email(self, value):
                if CustomUser.objects.filter(email=value).exists():
                    raise FinanceAPIException(ErrorCode.U02)
                return value
    class SignUpOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = [
                "id",
                "first_name",
                "last_name",
                "email",
                "nickname",
                "document_type",
                "document_number"
            ]

    def post(self, request):
        in_serializer = self.SignUpSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)
        try:
            user = auth_services.create_user(**in_serializer.validated_data)
        except:
            raise FinanceAPIException(ErrorCode.U02)
        
        out_serializer = self.SignUpOutputSerializer(user)

        return Response(out_serializer.data, status=status.HTTP_201_CREATED)
