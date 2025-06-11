from django.core.management.base import BaseCommand

from menu.models import Category


class Command(BaseCommand):
    help = 'Reformat category image file type for all Cctegories'

    def handle(self, *args, **kwargs):
        categories = Category.objects.exclude(image=None)
        count = 0
        for category in categories:
            category.reformat_image()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Reformated {count} images.'))
