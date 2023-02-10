from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class Users(AbstractUser):
    USER_TYPE=(
        ('SA',"Super admin"),
        ('A',"Admin"),
        ('U',"user")
    )

    options=models.CharField(max_length=2,choices=USER_TYPE,default='U')

class Vehicle(models.Model):

    alphanum=RegexValidator(r'^[0-9a-zA-Z]*$','Only use alphanumeric characters')

    
    VEHICLE_TYPE_CHOICES = [
        ('Two', 'Two wheeler'),
        ('Three', 'Three wheeler'),
        ('Four', 'Four wheeler'),
    ]
    vehicle_number = models.CharField(max_length=20,validators=[alphanum])
    vehicle_type = models.CharField(max_length=5, choices=VEHICLE_TYPE_CHOICES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.CharField(max_length=200)
    user=models.ForeignKey(Users,on_delete=models.CASCADE)



