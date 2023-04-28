from django.shortcuts import render, redirect
from .forms import Customer_Form
from django.contrib import messages
from .models import Customer

# Create your views here.


# Index View
def index(request):
    return render(request, 'index.html')


# KYC register form
def register(request):
    form = Customer_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Form has been submitted Successfuly!")
            return redirect('register')
            # return redirect('registered_student')
        else:
            messages.error(request, "Customer details not saved successfulyy, Try again !!")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html') 

