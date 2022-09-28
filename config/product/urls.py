from django.urls import path
from .views import *
from django.conf import settings


urlpatterns = [
  path('', home, name="home"),
  path('store/', all_product, name="store"),
  path('<int:id>/', store, name="store"),
  path('<int:id>/<int:category_id>/', product_detail, name="product_detail"),
]