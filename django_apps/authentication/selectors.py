from django_apps.authentication.models import CustomUser


def get_user_by_email(email: str) -> CustomUser:
    """
    Get a user by email.
    """
    return CustomUser.objects.get(email=email)


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

    return CustomUser.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        nickname=nickname,
        document_type=document_type,
        document_number=document_number,
    )
