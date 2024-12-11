from django.db import models

# Create your models here.
class studytable(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=100)
    Email=models.EmailField()
    Mob=models.IntegerField()
    Qualification=models.CharField(max_length=100)
    Dob=models.DateField()
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Image=models.FileField()

    def __str__(self):
        return self.Firstname

class PageVisit(models.Model):
    count = models.IntegerField(default=0)