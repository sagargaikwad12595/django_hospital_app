from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(max_length=30)
    gender = models.CharField(max_length=30)


    class Meta:
        db_table = 'patient'
