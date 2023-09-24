from django.shortcuts import render
from .scripts.customer_data import CustomerData  # getting data from form(contact html page) to  app
from django.core.mail import EmailMessage # uses smtplib under the hood makes it easy to send mail for any app
from .models import Customer  # stor# ing data in sqlite db

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        customer_data = CustomerData(request.POST)
        if customer_data.is_valid():
                # Process the form data
                name = customer_data.cleaned_data['name']
                email = customer_data.cleaned_data['email']
                message = customer_data.cleaned_data['message']

                Customer.objects.create(customer_name=name, customer_email=email, customer_msg=message)
                message_body = f"\nBooking Details: \n name: {name} \n msg: {message}\n"

                email_msg = EmailMessage("Hotel INH | Booking Confirmed, Thanks", message_body, to=[email])
                email_msg.send()
                return render(request, "thank.html")
    return render(request, "contact.html")


def thank(request):
    return render(request, "thank.html")
