from django.contrib import admin
from .models import *
import xadmin

# Register your models here.


class IT_assets_pc_admin(admin.ModelAdmin):
    list_display = (
        'User_Name_Pc',
        'User_Name_Pc_1',
        'User_Id',
        'Brand_Pc',
        'model_Pc',
        'Service_Tag',
        'Device_ID_Pc',
        'Pc_Type',
        'Equipment_Status_Pc',

    )
    search_fields = (
        'User_Id',
        'User_Name_Pc',
        'Service_Tag',
        'Equipment_Status_Pc'
    )

class Iphone_admin(admin.ModelAdmin):
    list_display = (
        "iphone_type",
        'ime_nunmber',
        'iphone_number',
        'location',
        'dep_iphone',
        'elm_iphone',
        'iphone_username',
        'zhuangtai_iphone',
    )
    search_fields = (
        'ime_nunmber',
        'iphone_number',
        'location',
        'dep_iphone',
        'elm_iphone',
        'iphone_username',
        'zhuangtai_iphone'


    )


class Collect_employee_information_PC_admin(admin.ModelAdmin):
    list_display = (
        'User_ID',
        'User_Englishname',
        'User_Chinesename',
        'Product_Name',
        'Amount',
        'Attribution_Dept',
        'Number_Pc',
        'Brand',
        'xinghao',
        'Service_Tag',
        'E_Service'
    )


admin.site.register(IT_assets_pc,IT_assets_pc_admin)
admin.site.register(Collect_employee_information_PC,Collect_employee_information_PC_admin)


admin.site.register(Iphone,Iphone_admin)




