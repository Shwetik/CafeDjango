from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        #print(request.session.get('cart'))
        if not request.session.get('cart'):
            user_name = request.session.get('name')
            return render(request, 'cart.html', {'name': user_name} )
        else:
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            user_name = request.session.get('name')
            data = {}
            data['name'] = user_name
            data['products'] = products

            return render(request, 'cart.html', data)

    def post(self, request):
        # product is the product id selected to add in wishlist
        product = request.POST.get('product')
        #print(product)
        cart = request.session.get('cart')
        #print(cart)
        remove = request.POST.get('remove')
        if cart:
             if remove:
                cart.pop(product)

        request.session['cart'] = cart
        #print(request.session['cart'])
        return redirect('cart')
