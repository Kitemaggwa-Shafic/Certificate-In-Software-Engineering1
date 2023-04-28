from django.db import models

# Create your models here.


# register client model
class Customer(models.Model):
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    dob = models.DateField(auto_now=True)
    gender = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    district = models.CharField(max_length=55)
    town = models.CharField(max_length=55)
    zipcode = models.CharField(max_length=55)
    phonenumber1 = models.CharField(max_length=55)
    phonenumber2 = models.CharField(max_length=55)
    email = models.CharField(max_length=55)

    def __str__(self):
        return self.firstname