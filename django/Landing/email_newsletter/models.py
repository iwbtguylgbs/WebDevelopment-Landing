from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
#pip install django-phonenumber-field[phonenumberslite]
#person = models.PeopleList.objects.get(id = 25)
#phoneNumber = person.number.as_e164

class PeopleList(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number = PhoneNumberField()
    mail = models.EmailField()


