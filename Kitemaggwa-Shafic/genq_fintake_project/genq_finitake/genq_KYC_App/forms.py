from django import forms
from .models import Customer


# The purpose of this class is to define a standardized way for users to submit information 
# based on the fields specified in the model. 
# This can be used to easily create forms for user input in a web application, 
# and to validate and process the data submitted by the user.
class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'gender', 'country','district','town','zipcode',
                  'phonenumber1','phonenumber2','email']