from django.shortcuts import render
from Products.models import Product
def Product_list(request):
    all_products = Product.objects.all()
    data = {
        'Products': all_products,
        'title':"Daraz product page"
         
    }
    return render(request,"single_product.html",data)
       
        
 
