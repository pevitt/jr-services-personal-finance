from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey


class Command(BaseCommand):
    help = 'Show the current API key'

    def handle(self, *args, **options):
        try:
            # Get the first (and should be only) API key
            api_key = APIKey.objects.first()
            
            if api_key:
                self.stdout.write(
                    self.style.SUCCESS(f'API Key found:')
                )
                self.stdout.write(f'Name: {api_key.name}')
                self.stdout.write(f'Created: {api_key.created}')
                self.stdout.write(f'Prefix: {api_key.prefix}')
                self.stdout.write(
                    self.style.WARNING(
                        'Note: The full API key is not stored for security reasons. '
                        'You need to save it when it was first created.'
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR('No API key found. Create one first with: python manage.py create_api_key <name>')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 