from django.core.management.base import BaseCommand

from menu.models import Category


class Command(BaseCommand):
    help = 'Regenerate thumbnails for all categories'

    def handle(self, *args, **kwargs):
        categories = Category.objects.exclude(image=None)
        count = 0
        for category in categories:
            category.generate_thumbnail()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Regenerated {count} thumbnails.'))
