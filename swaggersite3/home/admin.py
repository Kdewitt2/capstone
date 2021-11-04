from django.contrib import admin
from .models import Product, HomePost, Order, AboutPost, ContactInfo

admin.site.register(Product)
admin.site.register(HomePost)
admin.site.register(Order)
admin.site.register(AboutPost)
admin.site.register(ContactInfo)

