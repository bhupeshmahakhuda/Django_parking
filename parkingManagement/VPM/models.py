from django.db import models

class Category(models.Model):
    categoryName=models.CharField(max_length=20)

    def __str__(self):
        return self.categoryName

class Vehicle(models.Model):
    parkingNumber=models.CharField(max_length=20,null=True)
    vehicleComapny=models.CharField(max_length=20,null=True)
    regNo=models.CharField(max_length=20,null=True)
    ownerName=models.CharField(max_length=20,null=True)
    ownerContact=models.CharField(max_length=20,null=True)
    inTime=models.CharField(max_length=20,null=True)
    outTime=models.CharField(max_length=20,null=True)
    parkingCharge=models.CharField(max_length=20,null=True)
    remark=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,null=True)
    pdate=models.DateField(auto_now_add=True)

    category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.parkingNumber

