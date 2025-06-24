from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey


class Command(BaseCommand):
    help = 'Create new API key'

    def handle(self, *args, **options):
        api_key, key = APIKey.objects.create_key(name="Global API Key")
        self.stdout.write(f"API Key created: {key}")

        self.stdout.write(
            self.style.SUCCESS(
                'API Key created successfully. '
                'Note: The full API key is not stored for security reasons. '
                'You need to save it when it was first created.'
            )
        )
