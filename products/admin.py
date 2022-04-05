from django.contrib import admin

from products.models import ComfyProducts, ComfySale, Dimension, ItemSizeColor, ProductImages, ShippingInfo

# Register your models here.
admin.site.register(ComfyProducts)
admin.site.register(ComfySale)
admin.site.register(Dimension)
admin.site.register(ShippingInfo)
admin.site.register(ProductImages)
admin.site.register(ItemSizeColor)