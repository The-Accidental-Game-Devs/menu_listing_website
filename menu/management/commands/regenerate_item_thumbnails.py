from django.core.management.base import BaseCommand

from menu.models import Item


class Command(BaseCommand):
    help = 'Regenerate thumbnails for all items'

    def handle(self, *args, **kwargs):
        items = Item.objects.exclude(image=None)
        count = 0
        for item in items:
            item.generate_thumbnail()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Regenerated {count} thumbnails.'))
