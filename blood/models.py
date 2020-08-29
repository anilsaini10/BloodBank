from django.db import models

# Create your models here.


class NeedBlood(models.Model):
    person_id = models.AutoField
    person_name  = models.CharField(max_length=50)
    person_email = models.CharField(max_length=50,default="")
    person_mobileNumber =models.IntegerField(default=0)
    person_age =models.IntegerField(default=0)
    person_reason = models.CharField(max_length = 300)
    person_address= models.CharField(max_length=200)
    person_gender= models.CharField(max_length=20)
    person_bloodGroup= models.CharField(max_length=20)
    # pub_date = models.DateField()

    def __str__(self):
        return self.person_name

class DonateBlood(models.Model):
    person_id = models.AutoField
    person_name  = models.CharField(max_length=50)
    person_email = models.CharField(max_length=50,default="")
    person_mobileNumber =models.IntegerField(default=0)
    person_age =models.IntegerField(default=0)

    person_address= models.CharField(max_length=200)
    person_gender= models.CharField(max_length=20)
    person_bloodGroup= models.CharField(max_length=20)
    # pub_date = models.DateField("")

    def __str__(self):
        return self.person_name



class GotBlood(models.Model):
    person_id = models.AutoField
    person_name  = models.CharField(max_length=50)
    person_email = models.CharField(max_length=50,default="")
    person_mobileNumber =models.IntegerField(default=0)
    person_age =models.IntegerField(default=0)
    person_reason = models.CharField(max_length = 300)
    person_address= models.CharField(max_length=200)
    person_gender= models.CharField(max_length=20)
    person_bloodGroup= models.CharField(max_length=20)
    # pub_date = models.DateField("")

    def __str__(self):
        return self.person_name