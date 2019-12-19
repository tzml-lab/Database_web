from django.db import models

# Create your models here.

class UserStatus(models.Model):
    lineBotID = models.TextField()
    moneyORpass = models.TextField(default='現金/現鈔')   #即期/存摺
    moneyType = models.CharField(max_length=3,default='JPY')
    buyORsell = models.TextField(default='買入')  #賣出
    bank = models.CharField(max_length=10,default='臺灣銀行')
    
    def _str_(self):
        return "UserStatus"
    class Meta:
        db_table = "UserStatus"

class UserInfo(models.Model):
    lineBotID = models.TextField()
    moneyType = models.CharField(max_length=3)
    INorOUT = models.CharField(max_length=3)  #IN/OUT
    bank = models.CharField(max_length=10)
    lowerBound = models.TextField()
    def _str_(self):
        return "UserInfo"
    class Meta:
        db_table = "UserInfo"

class AllMoneyInfo(models.Model):
    moneyType = models.CharField(max_length=3)
    cashIN = models.TextField(default='0')
    cashOUT = models.TextField(default='0')
    spotIN = models.TextField(default='0')
    spotOUT = models.TextField(default='0')
    bank = models.CharField(max_length=6)
    fee = models.TextField(default='無')
    updateTime = models.TextField()
    def _str_(self):
        return "AllMoneyInfo"
    class Meta:
        db_table = "AllMoneyInfo"