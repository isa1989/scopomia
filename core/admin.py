from django.contrib import admin
from .models import *


class ItemImageAdmin(admin.StackedInline):
    model = ItemImage

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageAdmin]

    class Meta:
       model = Item

       
# Register your models here.
admin.site.register(Settings)
admin.site.register(Menu)
admin.site.register(ItemImage)
admin.site.register(About)
admin.site.register(Partnyor)
admin.site.register(BrendCategory)
