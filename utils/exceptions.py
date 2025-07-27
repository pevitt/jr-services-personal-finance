from enum import Enum

from rest_framework import status
from rest_framework.exceptions import APIException


class ErrorCode(Enum):
    """
    Enum for error codes.
    """

    U00 = dict(
        code="U00",
        message="An error occurred",
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

    U01 = dict(
        code="U01", 
        message="User not found", 
        status=status.HTTP_404_NOT_FOUND
    )

    U02 = dict(
        code="U02",
        message="Error while user creation",
        status=status.HTTP_400_BAD_REQUEST,
    )

    U03 = dict(
        code="U03", message="Invalid credentials", status=status.HTTP_401_UNAUTHORIZED
    )

    C00 = dict(
        code="C00",
        message="Error while creating category",
        status=status.HTTP_400_BAD_REQUEST,
    )

    C01 = dict(
        code="C01",
        message="Category already exists",
        status=status.HTTP_400_BAD_REQUEST,
    )

    C02 = dict(
        code="C02",
        message="Error while getting categories",
        status=status.HTTP_400_BAD_REQUEST,
    )

    C03 = dict(
        code="C03",
        message="Category not found",
        status=status.HTTP_400_BAD_REQUEST,
    )

    C04 = dict(
        code="C04",
        message="Category and type already exists",
        status=status.HTTP_400_BAD_REQUEST,
    )

    B00 = dict(
        code="B00",
        message="Error while creating balance",
        status=status.HTTP_400_BAD_REQUEST,
    )

    B01 = dict(
        code="B01",
        message="Balance not found",
        status=status.HTTP_404_NOT_FOUND,
    )

    B02 = dict(
        code="B02",
        message="Error while getting balances",
        status=status.HTTP_400_BAD_REQUEST,
    )

    B03 = dict(
        code="B03",
        message="Error while updating balance",
        status=status.HTTP_400_BAD_REQUEST,
    )

    T00 = dict(
        code="T00",
        message="Error while creating transaction",
        status=status.HTTP_400_BAD_REQUEST,
    )
    
    T01 = dict(
        code="T01",
        message="Transaction already exists",
        status=status.HTTP_400_BAD_REQUEST,
    )
    

    @classmethod
    def get_by_message(cls, message: str):
        try:
            return next(item for item in cls if item["message"] == message)
        except (StopIteration, Exception):
            return cls.U00

    @classmethod
    def get_by_code(cls, code: str):
        try:
            return next(item for item in cls if item["code"] == code)
        except (StopIteration, Exception):
            return cls.U00


class FinanceAPIException(APIException):
    """
    Custom API exception for finance module.
    """

    def __init__(self, error_code: ErrorCode, message: str = None, code: str = None):
        error = error_code
        if message:
            error = ErrorCode.get_by_message(message)

        data = error
        self.status_code = data["status"]

        super().__init__(detail=data["message"])
