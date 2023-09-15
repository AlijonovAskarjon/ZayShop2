from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, SET_NULL
from django.db.models import Model, CharField, TextChoices, TextField, BigIntegerField, ForeignKey, DateTimeField, \
    SlugField
from django.utils.text import slugify
from django_resized import ResizedImageField


class Category(Model):
    name = CharField(max_length=20)
    image = ResizedImageField(crop=['middle', 'center'], upload_to='product.image.url')
    slug = SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(Model):
    class ColorChoice(TextChoices):
        RED = 'Red', 'Red'
        WHITE = 'White', 'White'
        YELLOW = 'Yellow', 'Yellow'
        BLACK = 'Black', 'Black'
        gray = 'Gray', 'Gray'

    name = CharField(max_length=20)
    image = ResizedImageField(crop=['middle', 'center'], upload_to='product/images')
    price = CharField(max_length=20)
    description = TextField(default='Iltimos, tovarni sotib oling')  # noqa
    created_at = DateTimeField(auto_now=True)
    views_count = BigIntegerField(blank=True, null=True)
    size = TextField(max_length=15, blank=True, null=True)
    color = CharField(max_length=15, choices=ColorChoice.choices, blank=True, null=True,
                      help_text="Ranglardan birini tanlang!")  # noqa
    category = ForeignKey(Category, on_delete=SET_NULL, blank=True, null=True)
    slug = SlugField(max_length=255, null=True, blank=True)
    exists = BooleanField(default=True)
    brand = CharField(max_length=30)

    @property
    def short_desc(self):
        return self.description[:30] + '...'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class User(AbstractUser):
    phone_number = CharField(max_length=15)
    image = ResizedImageField(crop=['center', 'middle'], size=[400, 300], upload_to='user/images/%m')
