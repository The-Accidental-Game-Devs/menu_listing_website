from django.core.management.base import BaseCommand

from menu.models import Item


class Command(BaseCommand):
    help = 'Reformat item image file type for all items'

    def handle(self, *args, **kwargs):
        items = Item.objects.exclude(image=None)
        count = 0
        for item in items:
            item.reformat_image()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Reformated {count} images.'))
