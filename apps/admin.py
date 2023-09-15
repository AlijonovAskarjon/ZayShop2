from django.contrib import admin
from django.utils.html import format_html

from apps.models import Product, Category, User

admin.site.register(User)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    readonly_fields = ('slug',)

    @staticmethod
    def image_tag(obj: Category):
        return format_html(
            f'<img style=" opacity:1; border-radius: 15px; width:120px; height:80px;" src="{obj.image.url}" alt="{obj.name}">')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_image', 'price', 'short_desc', 'size', 'color', 'category', 'exists')
    exclude = ('slug', 'created_at')

    @admin.display(description='Image')
    def product_image(self, obj: Product):
        return format_html(
            f'<img style=" opacity:1; border-radius: 15px; width:120px; height:80px;" src="{obj.image.url}" alt="{obj.name}">'
        )
