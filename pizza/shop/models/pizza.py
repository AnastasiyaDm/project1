from django.db import models

# Create your models here.
from decimal import Decimal
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from slugify import slugify
from django.urls import reverse

class Pizza(models.Model):

    types = (
        ('cheese', 'Quattro Formaggi'),
        ('chicken', 'Quattro Stagioni'),
        ('mushroom', 'Funghi'),
        ('seafood', 'Frutti di Mare'),
        ('assorti', 'Assorti'),
        ('fruits', 'Fruits'),
        ('beef', 'Boscaiola'),
        ('hawaii', 'Hawaii'),
        ('green', 'Braccio di Ferro'),
        ('mozarella', 'Crudo'),
        ('vegetables', 'Vegetariana'),
        ('sausages', 'Bavaria')
    )

    name_slug = models.CharField(max_length=150, default='',null=True, blank=True)
    name = models.CharField(max_length=30)
    type = models.CharField(verbose_name='Пицца', max_length=15, choices=types, default='cheese')
    cost = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    image = ImageField(upload_to='pizza_img')

    @property
    def det_thumb_url(self):
        try:
            return get_thumbnail(self.image.path, '50x50', crop='center', quality=99).url
        except:
            return ''

    @property
    def thumb(self):
        try:
            return mark_safe('<img src="/media/%s" />' % get_thumbnail(self.image.path, '50x50', crop='center', quality=99))
        except:
            return ''

    def __str__(self):
        return '%s (%s)' % (self.name,self.type)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'name': self.name_slug})

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Pizza, self).save(*args, **kwargs)
