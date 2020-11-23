from modeltranslation.translator import translator, TranslationOptions
from .models import *


class MenuTranslationOption(TranslationOptions):
    fields = ('name',)


class SettingsTranslationOption(TranslationOptions):
    fields = ('slider_title', 'slider_content', 'slider_title_1', 'slider_content_1',
              'slider_title_2', 'slider_content_2', 'footer_menu', 'footer_partnyor', 'footer_dizayn',
              'about_contact', 'about_title', 'contact_us', 'contact_address', 'partnyor_title',"order_number","order_content",)

class ItemTranslationOption(TranslationOptions):
    fields = ('title',"other_title","description","specification")

class BrendCategoryTranslationOption(TranslationOptions):
    fields = ('name',)

class AboutTranslationOption(TranslationOptions):
    fields = ('title',"content",)

class PartnyorTranslationOption(TranslationOptions):
    fields = ('title',"content",)


translator.register(Menu, MenuTranslationOption)
translator.register(Settings, SettingsTranslationOption)
translator.register(Item, ItemTranslationOption)
translator.register(BrendCategory, BrendCategoryTranslationOption)
translator.register(About, AboutTranslationOption)
translator.register(Partnyor, PartnyorTranslationOption)

# translator.register(Settings, SettingsTranslationOption)
