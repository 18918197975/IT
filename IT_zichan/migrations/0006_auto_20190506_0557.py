# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-06 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_zichan', '0005_collect_employee_information_pc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iphone_type', models.CharField(blank=True, max_length=12, null=True, verbose_name='设备类型')),
                ('ime_nunmber', models.CharField(blank=True, max_length=24, null=True, verbose_name='IME号码')),
                ('iphone_number', models.CharField(blank=True, max_length=24, null=True, verbose_name='资产编号')),
                ('location', models.CharField(blank=True, max_length=24, null=True, verbose_name='设备所在地')),
                ('dep_iphone', models.CharField(blank=True, max_length=24, null=True, verbose_name='所属部门')),
                ('elm_iphone', models.CharField(blank=True, max_length=24, null=True, verbose_name='设备领用人')),
                ('iphone_username', models.CharField(blank=True, max_length=24, null=True, verbose_name='中文名称')),
                ('zhuangtai_iphone', models.CharField(blank=True, max_length=24, null=True, verbose_name='设备状态')),
            ],
        ),
        migrations.AlterModelOptions(
            name='collect_employee_information_pc',
            options={'verbose_name': '员工IT信息收集', 'verbose_name_plural': '员工IT信息收集'},
        ),
        migrations.AlterField(
            model_name='collect_employee_information_pc',
            name='User_ID',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='it_assets_pc',
            name='Base_Pc',
            field=models.CharField(blank=True, default='上海', max_length=32, null=True, verbose_name='设备存放地'),
        ),
    ]