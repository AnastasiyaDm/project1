from django.core.management.base import BaseCommand
from django.utils import timezone

from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Start...')
        for i in range(10):
            u = User()
            u.is_superuser = True
            u.is_active = True
            u.is_staff = True
            u.set_password('123')
            u.username = 'admin%s' % i
            u.save()
            print('Creating %s' % i)
        print('Done')
