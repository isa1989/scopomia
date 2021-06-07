from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField



class Settings(models.Model):
    #head 
    logo_header = models.FileField(null=True, blank=True, upload_to='settings')
    slider_title = models.CharField(max_length=255, blank=True,null=True)
    slider_content = models.TextField(blank=True,null=True)
    slider_image = models.FileField(blank=True,null=True, upload_to='settings')
    slider_title_1 = models.CharField(max_length=255, blank=True,null=True)
    slider_content_1 = models.TextField(blank=True,null=True)
    slider_image_1 = models.FileField(blank=True,null=True, upload_to='settings')
    slider_title_2 = models.CharField(max_length=255, blank=True,null=True)
    slider_content_2 = models.TextField(blank=True,null=True)
    slider_image_2 = models.FileField(blank=True,null=True, upload_to='settings')
    #footer meny
    footer_menu = models.CharField(max_length=255,blank=True,null=True)
    footer_partnyor = models.CharField(max_length=255,blank=True,null=True)
    footer_dizayn = models.CharField(max_length=255,blank=True,null=True)
    about_contact = models.CharField(max_length=255,blank=True,null=True)
    #sosial media 
    facebook_url = models.URLField(max_length=255,blank=True,null=True)
    instagram_url = models.URLField(max_length=255,blank=True,null=True)
    youtube_url = models.URLField(max_length=255,blank=True,null=True)
    #about
    about_title = models.CharField(max_length=100,blank=True,null=True)
    about_image = models.FileField(blank=True,null=True, upload_to='settings')
    #contact
    contact_us = models.CharField(max_length=255,blank=True,null=True)
    contact_address = models.CharField(max_length=255,blank=True,null=True)
    contact_number = models.CharField(max_length=100,blank=True,null=True)
    contact_email = models.CharField(max_length=150,blank=True,null=True)
    #partnyorlar
    partnyor_title = models.CharField(max_length=255,blank=True,null=True,default="Partnyorlar")
    #sifaris et
    order_number = models.CharField(max_length=255,blank=True,null=True)
    order_content = RichTextField()

   
    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'


class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=50, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_children(self):
        return Menu.objects.filter(parent=self)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyular'


class BrendCategory(models.Model):
    category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=255)
    other_title = models.TextField()
    price = models.FloatField()
    brendcategory = models.ForeignKey(BrendCategory,related_name="brend", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField()
    description = RichTextField()
    specification = RichTextField()
    discount_price = models.FloatField(blank=True, null=True)
  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:detail", kwargs={
            'slug': self.slug
        })


class ItemImage(models.Model):
    item = models.ForeignKey(Item, default=None,related_name="items", on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.item.title


class About(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Partnyor(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title


