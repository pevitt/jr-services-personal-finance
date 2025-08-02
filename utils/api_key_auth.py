from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework_api_key.models import APIKey
from rest_framework.exceptions import AuthenticationFailed


class CustomAPIKeyAuthentication(BaseAuthentication):
    """
    Custom API Key authentication that uses 'api-key' header
    """
    
    def authenticate(self, request):
        api_key = request.META.get('HTTP_API_KEY')
        if not api_key:
            return None
            
        try:
            api_key_obj = APIKey.objects.get_from_key(api_key)
            if api_key_obj.revoked:
                raise AuthenticationFailed('API Key has been revoked.')
            return (None, api_key_obj)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API Key.')


class HasValidAPIKey(BasePermission):
    """
    Custom permission that checks for valid 'api-key' header
    """
    
    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY')
        if not api_key:
            return False
            
        try:
            api_key_obj = APIKey.objects.get_from_key(api_key)
            return not api_key_obj.revoked
        except APIKey.DoesNotExist:
            return False