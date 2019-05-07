

from django.db import models


# Create your models here.
class IT_assets_pc(models.Model):
    Pc_Type = models.CharField(max_length=32, null=True, verbose_name="类型")
    Device_ID_Pc = models.CharField(max_length=32, null=True, verbose_name='设备编号')
    Base_Pc = models.CharField(max_length=32, default='上海', blank=True, null=True, verbose_name='设备存放地')
    Date_of_Purchase = models.DateTimeField(verbose_name="购买时间")
    Value_Pc = models.CharField(max_length=12 , null=True , verbose_name='原值')
    Brand_Pc = models.CharField(max_length=32, blank=True, null=True, default= 'Dell' , verbose_name='品牌')
    model_Pc = models.CharField(max_length=32 , blank=True, null=True, default= "E7470", verbose_name='型号')
    Service_Tag = models.CharField(max_length=32, blank=True, null=True, verbose_name="服务编号")
    Equipment_Status_Pc = models.CharField(max_length=32, blank=True, null=True, verbose_name='设备状态')
    User_Name_Pc = models.CharField(max_length=32, null=True, verbose_name='中文姓名')
    User_Name_Pc_1 = models.CharField(max_length=24, null=True, verbose_name='英文名')
    User_Id = models.CharField(max_length=12, null=True, blank=True, verbose_name='员工号')

    class Meta:
        verbose_name = 'IT 电脑资产'
        verbose_name_plural = 'IT 电脑资产'


class Collect_employee_information_PC(models.Model):
    User_ID = models.AutoField(primary_key=True,verbose_name='序号')
    User_Englishname = models.CharField(max_length=32,null=True,blank=True,verbose_name='英文名')
    User_Chinesename = models.CharField(max_length=32,null=True,blank=True,verbose_name='中文名')
    Product_Name = models.CharField(max_length=32,null=True, blank=True ,default='Desktop',verbose_name='产品名称')
    Amount = models.CharField(
        max_length=32,null=True,blank=True, default='1',verbose_name='数量')
    Attribution_Dept = models.CharField(max_length=32 , null=True, blank=True,verbose_name='归属部门')
    Number_Pc = models.CharField(max_length=32, blank=True, null=True, verbose_name="机器编号")
    Brand = models.CharField(max_length=32, blank=True ,null=True , verbose_name='品牌')
    xinghao = models.CharField(max_length=32,default='Latitude 7470',blank=True , null=True ,verbose_name='型号')
    Service_Tag = models.CharField(max_length=32 , blank=False , null=False ,verbose_name='服务编号')
    E_Service = models.CharField(max_length=32, blank=False,null=False, verbose_name='快速服务代码')

    class Meta:
        verbose_name = '员工IT信息收集'
        verbose_name_plural = '员工IT信息收集'




class Iphone(models.Model):

    iphone_type = models.CharField(max_length=12, blank=True, null=True, verbose_name='设备类型')
    ime_nunmber = models.CharField(max_length=24, blank=True, null=True, verbose_name='IME号码')
    iphone_number = models.CharField(max_length=24, blank=True, null=True, verbose_name='资产编号')
    location = models.CharField(max_length=24, blank=True, null=True, verbose_name='设备所在地')
    dep_iphone = models.CharField(max_length=24, blank=True, null=True, verbose_name='所属部门')
    elm_iphone = models.CharField(max_length=24, blank=True, null=True, verbose_name='设备领用人')
    iphone_username = models.CharField(max_length=24, blank=True, null=True, verbose_name='中文名称')
    zhuangtai_iphone = models.CharField(max_length=24, blank=True, null=True, verbose_name='设备状态')


    class Meta:
        verbose_name = '手机领用库存表'
        verbose_name_plural = '手机领用库存表'











