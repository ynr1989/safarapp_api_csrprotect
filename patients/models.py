from django.db import models


class Patient(models.Model):
    patiantFirstName = models.CharField(max_length=90, blank=False, default='')
    patiantLastName = models.CharField(max_length=90, blank=False, default='')
    email = models.CharField(max_length=100, blank=False, default='')
    bloodGroup = models.CharField(max_length=30, blank=False, default='')
    weight = models.CharField(max_length=50, blank=False, default='')
    age = models.IntegerField(default=0)
    nhsnumber = models.IntegerField(default=0)
    insuranceid = models.CharField(max_length=90, blank=False, default='')
    pincode = models.CharField(max_length=70, blank=False, default='')
    fatherHusbandName = models.CharField(max_length=70, blank=False, default='')
    gender = models.CharField(max_length=70, blank=False, default='')
    address = models.CharField(max_length=70, blank=False, default='')
    activestatus = models.CharField(max_length=70, blank=False, default='')
    patiantImage = models.CharField(max_length=70, blank=False, default='')
    createdAt = models.DateTimeField(auto_now=False, auto_now_add=True)

