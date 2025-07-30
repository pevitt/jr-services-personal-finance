from django.urls import converters
from utils.exceptions import FinanceAPIException, ErrorCode
import uuid

class CustomUUIDConverter:
    regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    def to_python(self, value):
        print(f"🎯 CustomUUIDConverter.to_python() llamado con: {value}")
        try:
            return uuid.UUID(value)
        except ValueError:
            print(f"❌ UUID inválido: {value}")
            raise FinanceAPIException(
                error_code=ErrorCode.B04.value
            )

    def to_url(self, value):
        return str(value)

# Registrar el converter
converters.register_converter(CustomUUIDConverter, 'custom_uuid')
print("✅ CustomUUIDConverter registrado como 'custom_uuid'")