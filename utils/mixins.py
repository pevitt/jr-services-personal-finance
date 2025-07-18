from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
import time

class ResponseMixin:
    def dispatch(self, request, *args, **kwargs):
        self.start_time = time.time()
        return super().dispatch(request, *args, **kwargs)
    
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        
        if isinstance(response, Response):
            original_data = response.data
            response_time = round((time.time() - self.start_time) * 1000, 2)  # en milisegundos
            
            if response.status_code < 400:
                code = "SUCCESS"
                message = "Request processed successfully"
            else:
                code = "ERROR"
                message = self._get_error_message(response.status_code)

            response.data = {
                'timestamp': datetime.now().isoformat(),
                'response_time_ms': response_time,
                'code': code,
                'message': message,
                'response_data': original_data
            }

        return response
    
    def _get_error_message(self, status_code):
        return {
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_404_NOT_FOUND: "Not Found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal Server Error",
        }.get(status_code, "Unknown Error")