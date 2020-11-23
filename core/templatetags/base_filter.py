from ..models import Settings, Menu
from django import template

register = template.Library()


@register.simple_tag
def get_menus():
    return Menu.objects.filter(status=True)


# @register.simple_tag
# def get_modal_menus():
#     return ModalMenu.objects.filter(status=True)


@register.simple_tag
def get_settings():
    return Settings.objects.last()


# @register.simple_tag
# def cart_item_count():
#     qs = Order.objects.filter(ordered=False)
#     if qs.exists():
#         return qs[0].items.count()
#     return 0
