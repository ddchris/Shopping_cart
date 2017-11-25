# -*- coding: utf-8 -*-

from django.contrib import admin
from myapp.models import ProductModel,UserModel 

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_price','p_imgs','p_desc','p_onsale','p_newproduct')

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id','user_account','user_password','user_gender','user_email')

admin.site.register(ProductModel,ProductModelAdmin)

admin.site.register(UserModel,UserModelAdmin)