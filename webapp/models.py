from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class GroupInfo(models.Model):
    uID = models.CharField(unique = True,max_length = 3, validators=[MinLengthValidator(3)])

class User(models.Model):
    uID = models.CharField(unique = True,max_length=3,validators=[MinLengthValidator(3)])
    Name = models.CharField(max_length = 50)
    Time = models.CharField(max_length = 19)

class User_Group(models.Model):
    uID = models.ForeignKey(User, on_delete = models.CASCADE)
    gID = models.ForeignKey(GroupInfo, on_delete = models.CASCADE)

class GroupProj(models.Model):
    gpID = models.CharField(unique = True, max_length = 3,validators=[MinLengthValidator(3)])
    Name = models.CharField(max_length = 20)
    CreatedBy = models.CharField(max_length = 3,validators=[MinLengthValidator(3)])
    #事件專案的人嗎
    gID = models.ForeignKey(GroupInfo, on_delete = models.CASCADE)

class PersonPorj(models.Model):
    Name = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20)
    Time = models.CharField(max_length = 19,default='2019-12-19-08-10-34')
    uID = models.ForeignKey(User, on_delete = models.CASCADE)

class Money(models.Model):
    pgCHOICES = [
        ('P', 'p'),
        ('G', 'g'),
    ]
    ioCHOICES = [
        ('I', 'I'),
        ('O', 'O'),
    ]
    PorG = models.CharField(max_length=1,choices=pgCHOICES,)
    pName = models.ForeignKey(PersonPorj, on_delete = models.CASCADE)
    uID = models.ForeignKey(User, on_delete = models.CASCADE,null=True,blank=True)#null=true
    gpID = models.ForeignKey(GroupInfo, on_delete = models.CASCADE,null=True,blank=True)#null=true
    time = models.CharField(max_length = 19,)#,default='2019-12-19-08-10-34')
    InorOut = models.CharField(max_length=1,choices=ioCHOICES,)
    ItemType = models.CharField(max_length=10,)
    ItemName = models.CharField(max_length=10,)
    value = models.IntegerField(default=0)
    

class MoneyOrLife(models.Model):
    Name = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20)
    moneyValue = models.IntegerField()
    # Dest_uID = models.ForeignKey(User, on_delete = models.CASCADE,unique=True)
    # Src_uID = models.ForeignKey(User, on_delete = models.CASCADE,unique=True)
    gpID = models.ForeignKey(GroupInfo, on_delete = models.CASCADE)

