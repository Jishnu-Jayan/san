from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class properties(models.Model):
    name = models.CharField(max_length=225)
    details = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None)

    def __str__(self):
        return self.name



class contacts(models.Model):
    enquiry_name = models.CharField(max_length=250)
    enquiry_email = models.EmailField(max_length=250)
    enquiry_subject = models.CharField(max_length=50)
    enquiry_phone = models.CharField(max_length=11)
    enquiry_message = models.TextField()


    def __str__(self):
        return self.enquiry_name +"     "+ self.enquiry_email + "    "+ self.enquiry_phone