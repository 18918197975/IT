# Generated by Django 2.1.3 on 2018-12-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_zichan', '0003_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterModelOptions(
            name='it_assets_pc',
            options={'verbose_name': 'IT 电脑资产', 'verbose_name_plural': 'IT 电脑资产'},
        ),
        migrations.AlterField(
            model_name='it_assets_pc',
            name='Base_Pc',
            field=models.CharField(blank=True, default='shanghai', max_length=32, null=True, verbose_name='设备存放地'),
        ),
        migrations.AlterField(
            model_name='it_assets_pc',
            name='Brand_Pc',
            field=models.CharField(blank=True, default='Dell', max_length=32, null=True, verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='it_assets_pc',
            name='Equipment_Status_Pc',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='设备状态'),
        ),
        migrations.AlterField(
            model_name='it_assets_pc',
            name='Service_Tag',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='服务编号'),
        ),
        migrations.AlterField(
            model_name='it_assets_pc',
            name='User_Id',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='员工号'),
        ),
        migrations.AlterField(
            model_name='it_assets_pc',
            name='model_Pc',
            field=models.CharField(blank=True, default='E7470', max_length=32, null=True, verbose_name='型号'),
        ),
    ]
