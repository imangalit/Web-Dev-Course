from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import JsonResponse
from api.models import Category
from api.models import Product

def category_list(request):
    categories = Category.objects.all()
    new_category_json = [c.to_json() for c in categories]
    return JsonResponse(new_category_json, safe=False)

def category_detail(request, new_id ):
    try:
        category = Category.objects.get(id=new_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())

def category_product(request, new_id):
    try:
        category = Category.objects.get(id=new_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.product_set.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)

def product_list(request):
    products = Product.objects.all()
    new_product_list = [p.to_json() for p in products]
    return JsonResponse(new_product_list, safe=False)

def product_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.to_json())
