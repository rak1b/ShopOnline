from django import template
from ShopOne.models import products,contact

register = template.Library()

@register.simple_tag
def product_return_by_id(id):
    return products.objects.filter(product_id=id)

@register.simple_tag
def product_name():
    return 'Rakib'

    