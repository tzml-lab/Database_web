from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
from webapp.models import User, PersonPorj, Money
from django.views.decorators.csrf import csrf_exempt

def addMoneyPage(request):
    # groupID = groupID
    # userID = request.GET['uid']
    # try:
    #     time = request.GET['time']
    # except:
    #     time = 'None'
    # print(User.objects.filter(uID=userID))

    # if len(User.objects.filter(uID=userID)) > 0:
    #     user = User.objects.get(uID=userID)

    #     if len(Money.objects.filter(uID=user)) > 0:
    #         dataInfo = Money.objects.filter(uID=user, time=time)[0]
    #         # print(dataInfo.time.strptime())
    #         InorOut = dataInfo.InorOut
    #         ItemType = dataInfo.ItemType
    #         ItemName = dataInfo.ItemName
    #         howmuch = dataInfo.value
    #         pName = dataInfo.pName.Name

    userID = request.GET['uid']
    print(User.objects.filter(uID=userID))
    if len(User.objects.filter(uID=userID)) > 0:
        user = User.objects.get(uID=userID)
        time = 'None'
        if len(Money.objects.filter(uID=user)) > 0:
            try:
                time = request.GET['time']
                dataInfo = Money.objects.filter(uID=user, time=time)[0]
                InorOut = dataInfo.InorOut
                ItemType = dataInfo.ItemType
                ItemName = dataInfo.ItemName
                howmuch = dataInfo.value
                pName = dataInfo.pName.Name
            except:
                time = 'None'
                dataInfo = Money.objects.filter(uID=user)[0]
            # print(dataInfo.time.strptime())



    print(request.GET)
    return render(request,"addMoney.html",locals())


def postNewMoney(request):
    if request.method == 'POST':
        print(request.body)
        return HttpResponse("succeess")
    else:
        return HttpResponse("succeess")

# 使用者查詢各帳介面
def helloWeb(request,userID):
    
    user = User.objects.get(uID = userID)
    personPorjs = user.personporj_set.all().order_by('Time')
    #print (type(personPorjs[0].Name))

    out_moneys = personPorjs[0].money_set.all().filter(InorOut = "O")
    in_moneys = personPorjs[0].money_set.all().filter(InorOut = "I")
    new_personPorj = personPorjs[0].Name
    return render(request,"page.html",locals())

#API們!!!!!!!!!!!!!!!!!!!!!!!!!!!
@csrf_exempt
def delMoney(request):
    if request.method=="POST":
        print(request.POST)
        print(json.dumps(request.POST))
        moneyInfo = json.loads(json.dumps(request.POST))
        #刪除money in 資料庫
        # print(moneyInfo['userID']+'  '+moneyInfo['moneyPK'])
        user = User.objects.get(uID = moneyInfo['userID'])
        money = user.money_set.all().filter(time = moneyInfo['moneyPK'])
        print(money)
        money.delete()
        print(user.money_set.all())
        #print(money)
        return HttpResponse("收到deleteMoney")

# 人的所有錢
def ApiMoney(request,uID):
    try:
        List = []
        targets = Money.objects.filter(uID__uID = uID)
        for target in targets:
            Dirct = {'PorG':target.PorG,
                    'pName':target.pName.Name,
                    'time':target.time,
                    'InorOut':target.InorOut,
                    'ItemType':target.ItemType,
                    'ItemName':target.ItemName,
                    'value':target.value}
            List.append(Dirct)
        return HttpResponse(json.dumps(List), content_type='application/json')
    except:
        return HttpResponse('error')

# 人的所有專案
def ApiPersonalProject(request,uID):
    List = []
    targets = PersonPorj.objects.filter(uID__uID = uID)
    print(targets)
    for target in targets:
        List.append(target.Name)
        return HttpResponse(json.dumps(List), content_type='application/json')

# 專案裡的所有錢
def ApiPprojMoney(request,uID):
    # pName=?
    List = []
    qu = request.GET
    print(qu)
    try:
        targets = Money.objects.filter(uID__uID = uID,pName__Name=qu['pName'])
        for target in targets:
            Dirct = {'PorG':target.PorG,
                    'pName':target.pName.Name,
                    'time':target.time,
                    'InorOut':target.InorOut,
                    'ItemType':target.ItemType,
                    'ItemName':target.ItemName,
                    'value':target.value}
            List.append(Dirct)
        return HttpResponse(json.dumps(List), content_type='application/json')
    except:
        return HttpResponse('error')

# 新增使用者
def newUser(request):
    print('post')
    request.encoding='utf-8'
    key = request.POST
    print(key)
    # try:
    datetimeNow = datetime.datetime.now()
    time = datetimeNow.strftime("%Y-%m-%d-%H-%M-%S")
    newU = User.objects.create(uID = key['uID'], Name = key['Name'],Time=time)
    date = datetime.date.today()
    name = str(date.year) + '年' + str(date.month) + '月'
    PersonPorj.objects.create(Name = name, type = 'type', uID = newU, Time=time)
    return HttpResponse('success')
    # except:
    #     return HttpResponse('error')

# 新增記帳
def newMoney(request):
    print('post')
    request.encoding='utf-8'
    #key = request.POST
    key= request.POST
    #key = serializers.serialize("json", keyJson)
    print(key)
    datetimeNow = datetime.datetime.now()
    time = datetimeNow.strftime("%Y-%m-%d-%H-%M-%S")
    if key['addORedit']=='add':
        try:
            new = Money.objects.create(PorG = key['PorG'][0],
                                    pName = PersonPorj.objects.get(Name__exact=key['pName'], uID__uID=key['uID']),
                                    time = time,
                                    InorOut = key['InorOut'],
                                    ItemType = key['ItemType'],
                                    ItemName = key['ItemName'],
                                    value = key['value'])
            if(new.PorG == 'P'):
                new.uID = User.objects.filter(uID__exact = key['uID'])[0]
                new.save()
            return HttpResponse('success')
        except:
            print('ex')
            return HttpResponse('error')
    else :
        user = User.objects.get(uID = key['uID'])
        money = user.money_set.all().get(time = key['time'])
        money.InorOut = key['InorOut']
        money.ItemType = key['ItemType']
        money.ItemName = key['ItemName']
        money.value = key['value']
        money.save()
        
        personPorjs = user.personporj_set.all().order_by('Time')
        out_moneys = personPorjs[0].money_set.all().filter(InorOut = "O")
        in_moneys = personPorjs[0].money_set.all().filter(InorOut = "I")
        new_personPorj = personPorjs[0].Name
        
        return render(request,"page.html",locals())

            
    


