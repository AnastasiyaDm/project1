from django.core.management.base import BaseCommand
from django.utils import timezone


from shop.models import Pizza
from django.core.files import File
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Start')
        Pizza.objects.all().delete()
        image_path = settings.BASE_DIR+'/data'
        for i in Pizza.types:
            img = '%s/%s.jpeg' % (image_path,i[0])
            p = Pizza()
            p.type = i[0]
            p.name = '%s pizza' % i[1]
            p.cost = 10
            p.save()
            p.image.save('%s.jpeg' % p.id,File(open(img, 'rb')))
            print('Creating %s' % i[0])
        print('Done')
