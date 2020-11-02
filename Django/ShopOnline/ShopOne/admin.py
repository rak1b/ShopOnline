from django.contrib import admin

# Register your models here.
from ShopOne.models import  products,contact,checkout_info
admin.site.register(products)
admin.site.register(contact)
admin.site.register(checkout_info)
