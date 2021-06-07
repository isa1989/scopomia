from django.shortcuts import render
from django.views import generic
from .models import *
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404,HttpResponseNotFound
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


class ScopomiaHomeView(generic.TemplateView):
    template_name = 'home.html'


class ScopomiaBaseIndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_models'] = Menu.objects.all()
        context['partnyor_models'] = Partnyor.objects.all()

        return context
        
class ItemView(ListView):
    template_name = "product.html"
    model = Item
   
    def get(self, request, *args, **kwargs):
        menu_request = request.GET.get("menu")
        category_request = request.GET.get("category")
        if menu_request:
            
            if menu_request == "Stihl" or menu_request == "Other":
                # breakpoint()
                category = BrendCategory.objects.filter(category__name=menu_request)
                items = Item.objects.filter(brendcategory__category__name=menu_request)
                page = request.GET.get('page', 1)
                paginator = Paginator(items, 1)
                try:
                    items = paginator.page(page)
                except PageNotAnInteger:
                    return render(request, template_name='error.html')
                except EmptyPage:
                    return render(request, template_name='error.html')
            else:
                return render(request,template_name="error.html")
            return render(request,
                    template_name='product.html',
                    context = {"menu_request":menu_request,
                        "category":category,
                        "items":items,
                     })  
        if category_request: 
            try:
                category_request = int(category_request)
                category = BrendCategory.objects.filter(id = category_request)
                parent_category = BrendCategory.objects.filter(category_id = category_request)
                items = Item.objects.filter(brendcategory__id = category_request)
                page = request.GET.get('page', 1)
                paginator = Paginator(items, 1)
                try:
                    items = paginator.page(page)
                except PageNotAnInteger:
                    return render(request, template_name='error.html')
                except EmptyPage:
                    return render(request, template_name='error.html')
            except ValueError:
                return render(request,template_name="error.html") 
            return render(request,
                        template_name='product.html',
                        context = {"menu_request":menu_request,
                            "category":category,
                            "parent_category":parent_category, 
                            "items":items,
                            })

        else:
            return render(request,template_name="error.html") 
           
    
class DetailItemView(DetailView):
    template_name = "detail.html"
    model = Item 
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['photos'] = ItemImage.objects.filter(item__title=context['object'].title)
        context['last_items'] = Item.objects.filter().order_by('-id')[:10]
        
        return context

        




class AboutView(ListView):
    template_name = 'about.html'
    model = About

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['whatwedo_models'] = WhatWeDo.objects.all()

    #     return context



class ScopomiaContactusView(generic.TemplateView):
    template_name = 'contact.html'
    

# def error_404(request, exception):
#     context = RequestContext(request)
#     err_code = 404
#     response = render_to_response('index.html', {"code": err_code}, context)
#     response.status_code = 404
#     return response

class ScopomiaCheckoutView(generic.TemplateView):
    template_name = "confirmation.html"


def error_404(request):
    breakpoint()
#     data = {}
#     return render(request, 'error.html', data)


from django.shortcuts import render_to_response
from django.template import RequestContext

def handler404(request, exception, template_name="error.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response