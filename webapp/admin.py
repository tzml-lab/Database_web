from django.contrib import admin
from webapp.models import User, PersonPorj, Money, User_Group, GroupInfo, GroupProj, MoneyOrLife

# Register your models here.
admin.site.register(User)
admin.site.register(PersonPorj)
admin.site.register(Money)
admin.site.register(User_Group)
admin.site.register(GroupInfo)
admin.site.register(MoneyOrLife)
# admin.site.register()
#, GroupInfo, GroupProj, 