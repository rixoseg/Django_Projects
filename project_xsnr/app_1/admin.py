from django.contrib import admin
from .models import Main_Report_Group
from .models import Rixos_Report_Group
from .models import USALI_Report_Group
from .models import Account_list

# Register your models here.
@admin.register(Main_Report_Group)
class Main_Report_GroupAdmin(admin.ModelAdmin):
    list_display = ['rg_1_name']
    search_fields = ['rg_1_name']
class Meta:
    model = Main_Report_Group

@admin.register(Rixos_Report_Group)
class Rixos_Report_GroupAdmin(admin.ModelAdmin):
    list_display = ['rg_2_name']
    search_fields = ['rg_2_name']
class Meta:
    model = Rixos_Report_Group

@admin.register(USALI_Report_Group)
class USALI_Report_GroupAdmin(admin.ModelAdmin):
    list_display = ['rg_3_name']
    search_fields = ['rg_3_name']
class Meta:
    model = USALI_Report_Group

@admin.register(Account_list)
class Rixos_Report_GroupAdmin(admin.ModelAdmin):
    list_display = ['acc_code']
    search_fields = ['acc_name']
class Meta:
    model = Account_list