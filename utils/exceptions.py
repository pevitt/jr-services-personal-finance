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

    U01 = dict(code="U01", message="User not found", status=status.HTTP_404_NOT_FOUND)

    U02 = dict(
        code="U02",
        message="Error while user creation",
        status=status.HTTP_400_BAD_REQUEST,
    )

    U03 = dict(
        code="U03", message="Invalid credentials", status=status.HTTP_401_UNAUTHORIZED
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
