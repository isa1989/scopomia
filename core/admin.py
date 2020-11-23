from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


# class SettingsAdmin(TranslationAdmin):
#     pass
#     fieldsets = (
#         ('Home Page Settings', {
#             'classes': ('collapse',),
#             'fields': ('logo_header',)
#         }),
# #         # ('Footer Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('footer_title', 'footer_links', 'footer_home_link', 'footer_home_url', 'footer_whatwedo_link',
        #                'footer_whatwedo_url', 'footer_manifesto_link', 'footer_manifesto_url', 'footer_joinus_link',
        #                'footer_joinus_url', 'footer_contact_us', 'footer_contact_us_adress', 'footer_tel_text',
        #                'footer_email', 'facebook', 'linkedin', 'copyright'),
        # }),
        # ('Social Networks Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('facebook', 'facebook_target', 'instagram', 'instagram_target', 'linkedin', 'linkedin_target',
        #                'twitter', 'twitter_target', 'mail', 'mail_target',),
        # }),
        # ('Logo Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('logo_header', 'logo_home', 'logo_footer', 'logo_header_url', 'logo_home_url', 'logo_footer_url'),
        # }),
        # ('What we do Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('index_title',),
        # }),
        # ('Manifesto Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('index_title_manifesto',),
        # }),
        # ('Workshops Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('index_title_workshop',),
        # }),
        # ('Join us Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('joinus_title',),
        # }),


        # ('Cases Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('cases_title', 'cases_banking', 'cases_bold_title_banking', 'cases_plane_title_banking',
        #                'cases_bold_content_banking', 'cases_plane_content_banking',
        #                'cases_insurance', 'cases_bold_title_insurance', 'cases_plane_title_insurance',
        #                'cases_bold_content_insurance', 'cases_plane_content_insurance',
        #                'cases_telecom', 'cases_bold_title_telecom', 'cases_plane_title_telecom',
        #                'cases_bold_content_telecom', 'cases_plane_content_telecom',
        #                'cases_startup', 'cases_bold_title_startup', 'cases_plane_title_startup',
        #                'cases_bold_content_startup', 'cases_plane_content_startup'
        #                ),
        # }),
        # ('404 Not Found Settings', {
        #     'classes': ('collapse',),
        #     'fields': ('not_found_title', 'not_found_opps', 'not_found_name', 'not_found_content',
        #                'not_found_url', 'not_found_path',),
        # }),

    # )
# @admin.register(ItemImage)
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
# admin.site.register(Category)
admin.site.register(ItemImage)
# admin.site.register(OrderItem)
# admin.site.register(Order)
admin.site.register(About)
admin.site.register(Partnyor)
admin.site.register(BrendCategory)
