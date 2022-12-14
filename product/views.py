from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct


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

    orderproduct = OrderProduct.objects.filter(user=request.user, product_id=product.id).exists()

    reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'product': product,
        'orderproduct':orderproduct,
        'reviews': reviews

    }

    return render(request, 'product_detail.html', context)


def search(request):
    category = Category.objects.all()



    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.filter(name__icontains=keyword)
            product_count = product.count()
    
    context = {
        'product':product,
        'product_count': product_count,
        'category':category,

    }
    return render(request, 'store.html', context)



def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            review = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, "?????????????? ???? ??????????, ?????? ?????????? ????????????????")
            return redirect(url)


        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data= ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()

                messages.success(request, '?????????????? ???? ?????? ??????????')
                return redirect(url)
