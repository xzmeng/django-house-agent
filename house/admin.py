from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(RentInfo)
admin.site.register(SaleInfo)
admin.site.register(RentContract)
admin.site.register(SaleContract)
admin.site.register(RentCommission)
admin.site.register(SaleCommission)

