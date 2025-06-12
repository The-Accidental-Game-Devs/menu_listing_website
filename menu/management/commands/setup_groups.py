from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Set up groups with default model permissions.'

    def handle(self, *args, **kwargs):
        group_permissions = {'Item Manager': ['add_item', 'change_item', 'delete_item'],
            'Category Manager': ['add_category', 'change_category', 'delete_category'], }

        for group_name, perm_codenames in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'Created group: {group_name}')

            for codename in perm_codenames:
                try:
                    permission = Permission.objects.get(codename=codename)
                    group.permissions.add(permission)
                    self.stdout.write(f'  ✓ Added permission: {codename}')
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'  ⚠ Missing permission: {codename}'))

        self.stdout.write(self.style.SUCCESS('Groups and default permissions setup complete.'))
