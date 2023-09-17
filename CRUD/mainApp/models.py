from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    emp_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=20)
    Salary = models.IntegerField()