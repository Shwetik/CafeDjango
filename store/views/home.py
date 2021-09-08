from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import  View
from django.contrib import messages


class Index(View):

    def get(self, request):

        # Initializing Objects
        products = Product.get_all_products();
        categories = Category.get_all_categories();


        # Handle and filter category GET request
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();

        # Render index.html using database objects
        session_user = request.session.get('name')
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['name'] = session_user

        return render(request, 'index.html', data)

    def post(self, request):

        product = request.POST.get('product')
        #print(product)
        cart = request.session.get('cart')
        if cart:
            cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        #print(request.session['cart'])
        return redirect('homepage')



