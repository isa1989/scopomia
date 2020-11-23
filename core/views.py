from django.shortcuts import render
from django.views import generic
from .models import *
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.template import RequestContext







class ScopomiaHomeView(generic.TemplateView):
    template_name = 'home.html'


class ScopomiaBaseIndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_models'] = Menu.objects.all()
        context['partnyor_models'] = Partnyor.objects.all()

        return context
        

class ItemView(View):
    template_name = "product.html"
    model = Item
    paginate_by = 25
    # list=Item.objects.all()

    def get(self, request, *args, **kwargs):
        menu_request = request.GET.get("menu")
        category_request = request.GET.get("category")      
        if menu_request:
            if menu_request == "Emiliano" or menu_request == "Adawall":            
                category = BrendCategory.objects.filter(category__name=menu_request)
                items = Item.objects.filter(brendcategory__category__name=menu_request)
        elif category_request:
            category_request = int(category_request)
            category = BrendCategory.objects.filter(id= category_request)
            items = Item.objects.filter(brendcategory__id= category_request)
        return render(request,
                    template_name='product.html',
                    context = {"category":category, 
                    "items":items,
                     "menu_request":menu_request})
            
    
class DetailItemView(DetailView):
    template_name = "detail.html"
    model = Item 
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['photos'] = ItemImage.objects.filter(item__title=context['object'].title)
        context['last_items'] = Item.objects.filter().order_by('-id')[:10]
        
        return context

# class OrderSummaryView(View):
#     def get(self, *args, **kwargs):
#         try:
#             order = Order.objects.get()
#             context = {
#                 'object': order
#             }
#             return render(self.request, 'order_summary.html', context)
#         except ObjectDoesNotExist:
#             messages.warning(self.request, "You do not have an active order")
#             return redirect("/")

# def add_to_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_item, created = OrderItem.objects.get_or_create(
#         item=item,
#         # user=request.user,
#         ordered=False
#     )
#     order_qs = Order.objects.filter(ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             # messages.info(request, "This item quantity was updated.")
#             return redirect("core:order-summary")
#         else:
#             order.items.add(order_item)
#             # messages.info(request, "This item was added to your cart.")
#             return redirect("core:product")
#     else:
#         ordered_date = timezone.now()
#         order = Order.objects.create(ordered_date=ordered_date)
#         order.items.add(order_item)
#         # messages.info(request, "This item was added to your cart.")
#         return redirect("core:product")


# def remove_from_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_qs = Order.objects.filter(
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 ordered=False
#             )[0]
#             order.items.remove(order_item)
#             order_item.delete()
#             # messages.info(request, "This item was removed from your cart.")
#             return redirect("core:product")
#         else:
#             # messages.info(request, "This item was not in your cart")
#             return redirect("core:product")
#     else:
#         # messages.info(request, "You do not have an active order")
#         return redirect("core:product", slug=slug)


# def remove_single_item_from_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_qs = Order.objects.filter()


#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,

#             )[0]
#             if order_item.quantity > 1:
#                 order_item.quantity -= 1
#                 order_item.save()
#             else:
#                 order.items.remove(order_item)
#             # messages.info(request, "This item quantity was updated.")
#             return redirect("core:order-summary")
#         else:
#             # messages.info(request, "This item was not in your cart")
#             return redirect("core:product", slug=slug)
#     else:
#         # messages.info(request, "You do not have an active order")
#         return redirect("core:product", slug=slug)

class AboutView(ListView):
    template_name = 'about.html'
    model = About

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['whatwedo_models'] = WhatWeDo.objects.all()

    #     return context



class ScopomiaContactusView(generic.TemplateView):
    template_name = 'contact.html'
    

def error_404(request, exception):
    context = RequestContext(request)
    err_code = 404
    response = render_to_response('404a.html', {"code": err_code}, context)
    response.status_code = 404
    return response

class ScopomiaCheckoutView(generic.TemplateView):
    template_name = "confirmation.html"


