from django.contrib import admin

# Register your models here.
from firstapp.models import UserStatus, UserInfo, AllMoneyInfo

admin.site.register(UserStatus)
admin.site.register(UserInfo)
admin.site.register(AllMoneyInfo)