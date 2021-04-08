from django.urls import path

from api.views import category_list, category_detail, category_product, product_list, product_detail

urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:new_id>/', category_detail),
    path('categories/<int:new_id>/products', category_product),

    path('products/', product_list),
    path('products/<int:pk>/', product_detail)
]