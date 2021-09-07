from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View


class Login(View):
    def get(self , request):
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        #customer object
        customer = Customer.get_customer_by_email(email)


        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:

                # mapping customer session with customer id
                request.session['customer'] = customer.id
                request.session['name'] = customer.first_name
                request.session['email'] = customer.email

                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        #print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
