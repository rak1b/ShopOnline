from django.contrib import admin

# Register your models here.
from ShopOne.models import  products,contact,checkout_info,shop_tracker
admin.site.register(contact)
@admin.register(products)
class productAdmin(admin.ModelAdmin):
	list_display = [
		'product_id',
		'product_name',
		'product_desc',
		'pub_date',
		'category',
		'price',
		'image'

	]

@admin.register(checkout_info)
class registerAdmin(admin.ModelAdmin):
	list_display = [
		'checkout_id',
		'checkout_name',
		'checkout_email',
		'checkout_phone',
		'checkout_address',
		'checkout_zip_code',
		'checkout_json',
	]

@admin.register(shop_tracker)
class mytrackerAdmin(admin.ModelAdmin):
	list_display = ['tracker_id','tracker_desc','tracker_date']
