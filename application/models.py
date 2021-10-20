# Here we are importing django models for creating models.
from django.db import models



# Employee (fields: id,firstname,lastname,image,email, joindate, salary)
class Employee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    image = models.ImageField()
    email = models.CharField(max_length=50)
    salary = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Employee"
