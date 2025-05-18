from django_apps.authentication import selectors as auth_selectors
from django_apps.authentication.models import CustomUser


def create_user(
    *,
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    nickname: str,
    document_type: str,
    document_number: str
) -> CustomUser:
    """
    Create a new user.
    """
    user = auth_selectors.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        nickname=nickname,
        document_type=document_type,
        document_number=document_number,
    )

    return user
