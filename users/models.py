from django.db import models


class User(models.Model):
    title = models.CharField(max_length=20, blank=False, default='')
    firstName = models.CharField(max_length=90, blank=False, default='')
    surName = models.CharField(max_length=90, blank=False, default='')
    dob = models.CharField(max_length=90, blank=False, default='')
    mobile = models.IntegerField()
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    addressline1 = models.CharField(max_length=300, blank=False, default='')
    addressline2 = models.CharField(max_length=300, blank=True, default='')
    town = models.CharField(max_length=100, blank=False, default='')
    country = models.CharField(max_length=100, blank=False, default='')
    postcode = models.CharField(max_length=100, blank=False, default='')
    addDoctDetails = models.CharField(max_length=100, blank=True, default='')
    efirstName = models.CharField(max_length=300, blank=True, default='')
    esurName = models.CharField(max_length=300, blank=True, default='')
    emobile = models.CharField(max_length=300, blank=True, default='')
    isPatient = models.BooleanField(default=False)
    isDoctor = models.BooleanField(default=False)
    isStaff = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    activestatus = models.CharField(max_length=100, blank=True, default='YES')
    createdAt = models.DateTimeField(auto_now=False, auto_now_add=True)


class UserToken(models.Model):
    access_token = models.CharField(max_length=1024)
    refresh_token = models.CharField(max_length=1024)
    access_token_created_at = models.DateTimeField(auto_now_add=True)
    refresh_token_created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.access_token
