from django.shortcuts import render , redirect
from django.views import  View
from django.core.mail import send_mail
from django.conf import settings


class Booking(View):
    def get(self , request):
        user_name = request.session.get('name')
        user_mail = request.session.get('email')
        data = {}
        data['name'] = user_name
        data['email'] = user_mail
        #print(data)
        return render(request, 'booking.html', data)

    def post(self, request):

        postData = request.POST
        first_name = postData.get('name')
        timing = postData.get('gridRadios')
        email = postData.get('email')
        user_name = request.session.get('name')

        print(user_name,timing,email)

        error_message = None
        success_message = 'Reservation Booked !'
        if (not first_name):
            error_message = "Please provide a name for reservation !"
        if (not email):
            error_message = "Please provide email for reservation !"

        data={}
        if error_message:
            data['name'] = user_name
            data['error'] = error_message
        else:
            data['name'] = user_name
            data['success'] = success_message
            '''
             send_mail(
                'Reservation Confirmed !',  # Subject
                'Hello ' + first_name + ' your reservation is confirmed this ' + timing,  # Message
                'shwetikt@gmail.com',  # From
                ['shwetikt@gmail.com']  # To
                )
            '''
        return render(request, 'booking.html', data)



