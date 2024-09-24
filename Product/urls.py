from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('products/',views.allprod,name='products'),
    path('products.details/<int:id>/',views.productDetail,name='productdetail'),
    
]   
