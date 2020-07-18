from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Main_Report_Group(models.Model):
    rg_1_name = models.CharField(max_length=100,unique=True, verbose_name='Main Report Group')
    rg_1_name_cd = models.DateField(auto_now_add=True, verbose_name='Created Date')

class Rixos_Report_Group(models.Model):
    rg_2_name = models.CharField(max_length=100,unique=True, verbose_name='PL Report Group')
    rg_1_grp = models.ForeignKey(Main_Report_Group, on_delete=models.CASCADE, verbose_name='Main Report Group')
    rg_2_name_cd = models.DateField(auto_now_add=True, verbose_name='Created Date')

class USALI_Report_Group(models.Model):
    rg_3_name = models.CharField(max_length=100,unique=True, verbose_name='USALI Report Group')
    rg_1_grp = models.ForeignKey(Main_Report_Group, on_delete=models.CASCADE, verbose_name='Main Report Group')
    rg_3_name_cd = models.DateField(auto_now_add=True, verbose_name='Created Date')

class Account_list(models.Model):
    acc_code = models.CharField(max_length=20, verbose_name='Account Code', unique=True)
    acc_name = models.CharField(max_length=100, verbose_name='Account Name')
    rg_1 = models.ManyToManyField(Rixos_Report_Group)
    rg_2 = models.ManyToManyField(USALI_Report_Group)
    acc_cd = models.DateField(auto_now_add=True, verbose_name='Created Date')