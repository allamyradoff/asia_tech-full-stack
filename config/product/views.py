from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def home(request):
    product = Product.objects.filter(is_active=True)
    category = Category.objects.all()
    context = {
        'product': product,
        'category':category,
    }
    return render (request, 'home.html', context)

def all_product(request):
    all_products = Product.objects.all()
    category = Category.objects.all()

    paginator = Paginator(all_products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)



    context = {
        'product' : paged_products,
        'category': category
    }

    return render(request, 'store.html', context)



def store(request, id):
    category = Category.objects.all()
    product = Product.objects.filter(category=id, is_active=True)

    paginator = Paginator(product, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'product':paged_products,
        'category':category,
    }
    return render(request, 'store.html', context)

def product_detail(request, category_id, id):
    product = Product.objects.get(id=id)
    print(product)

    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)
