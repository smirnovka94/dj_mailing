from django.core.management.base import BaseCommand

from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        user = User.objects.create(
        # name='kirill',
        email='kirill@sky.pro',
        first_name = 'Admin',
        is_superuser = True,
        is_staff = True,
        is_active = True
        )

        user.set_password("qwerty88")
        user.save()



