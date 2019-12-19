# from firstapp.models import *#UserStatus,UserInfo, AllMoneyInfo
# import requests
# import selenium
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import json, re, datetime, time

# from django.conf import settings
# from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
# from django.views.decorators.csrf import csrf_exempt
# # from home.models import App
# from linebot import LineBotApi, WebhookParser
# from linebot.exceptions import InvalidSignatureError, LineBotApiError
# from linebot.models import MessageEvent, TextSendMessage, PostbackEvent

# line = LineBotApi('k5bOp3T9Djg6kva7/uffZhDBCs8bOLHZZ+c7ujyyQNOXgW2BYmOaeSh9dm02GePq+gD1+nUKVeDNGWByoEhtXsc6KjcXK4Ho1VKNPIAQv22fuirxpUOKm0gUSbFKyRwMXt4/z4osUDN+NeLK7CH54gdB04t89/1O/w1cDnyilFU=')
# parser = WebhookParser('a0b0bd5107877891df3a337c5355bfc6')
   
              
# # print(111)
# global ans, firstbank, megabank, taiwanbank, cathaybank, esunbank

# # XXXbank.append({
# #     'type':貨幣名稱 'USA',
# #     'cashIN':float(), =現金 買入匯率(第一) /現金買匯(兆豐) /本行買入(台銀) /銀行買進(國泰) / 銀行買入(玉山)
# #     'cashOUT':float(),=現金 賣出匯率       /現金賣匯      /本行賣出      /銀行賣出      / 銀行賣出
# #     'spotIN':float()  =即期 即期買匯	
# #     'spotOUT':float(),=即期 
# # })
# global nameToName
# nameToName = [
#     {'name':'日圓','code':'JPY'},
#     {'name':'美元','code':'USD'},
#     {'name':'人民幣','code':'CNY'},
#     {'name':'歐元','code':'EUR'},
#     {'name':'港幣','code':'HKD'},
#     {'name':'英鎊','code':'GBP'},
#     {'name':'澳幣','code':'AUD'},
#     {'name':'加幣','code':'CAD'},
#     {'name':'新加坡幣','code':'SGD'},
#     {'name':'瑞士法郎','code':'CHF'},
#     {'name':'泰銖','code':'THB'},
#     {'name':'菲律賓比索','code':'PHP'},
#     {'name':'韓元','code':'KRW'}
# ]

# ###  ----比率網---- ###

# def money_bank(listTbody,money_type):  # 該項貨幣(1)查詢各銀行(n)匯率，已爬到內容(listTbody)作整理
#     cnt = 0
#     bank_all = listTbody.find_all('tr')
#     # print(bank_all)
#     for x in bank_all:
#         if cnt == 0:
#             cnt = cnt + 1
#             continue
#         else:
#             row = x.find_all('td')
#             bank = row[0].text.replace('\n','')
#             intType = []
#             for i in range(1,5):
#                 if row[i].text == '--':
#                     intType.append(0)
#                 else:
#                     intType.append(float(row[i].text))
#             date = datetime.datetime.now()
#             fee = row[6].text.replace(' ','')
#             ans.append({
#                 'type':money_type,
#                 'bank':bank,
#                 'cashIN':intType[0],
#                 'cashOUT':intType[1],
#                 'spotIN':intType[2],
#                 'spotOUT':intType[3],
#                 'fee':fee,
#                 'update':str(date.year) +'/'+ str(date.month) +'/'+ str(date.day) +' '+ row[5].text
#             })
#         # except:
#         #     continue
#     return

# def all_craw_moneyType():  #帶入要查詢的貨幣名稱 get JSON格式的ans
#     global ans
#     ans = []
#     money_type = 'X'
#     # print(123)
#     webHomePage = "https://www.findrate.tw"
#     res_homepage = requests.get(webHomePage)
#     res_homepage.encoding='utf8'
#     soup_homepage = BeautifulSoup((res_homepage.text),'lxml') 
#     listMoney_type = soup_homepage.select('.listbtns')
#     li_a = listMoney_type[0].select('a')

#     for href in li_a:
#         lihref = href.get('href')
#         regex = re.compile('\/(.+)\/')
#         match = regex.search(lihref)
#         if match.group(1) == money_type or money_type == 'X':
#             if href.text == '南非幣' or href.text == '印度披索' or href.text == '丹麥幣' or href.text == '墨西哥比索' or href.text == '土耳其里拉':
#                 continue
#             res_money = requests.get(webHomePage+lihref)
#             res_money.encoding='utf8'
#             soup_money = BeautifulSoup((res_money.text),'lxml')
#             moneyList = soup_money.select('tbody')
            
#             money_bank(moneyList[1],match.group(1))
#             # break

# # all_craw_moneyType()
# # for x in ans:
# #     print(x)


# ### ---第一銀行--- ### -----------------------------------------
# def NO1_craw_moneyType():
#     searchTYPE = 'X'
#     global firstbank
#     firstbank = []
#     webHomePage = "https://ibank.firstbank.com.tw/NetBank/7/0201.html?sh=none"
#     res_homepage = requests.get(webHomePage)
#     res_homepage.encoding='utf8'
#     soup_homepage = BeautifulSoup((res_homepage.text),'lxml') 

#     time_span = soup_homepage.select('.locator2')
#     regex = re.compile('(\d.+\d)')
#     match = regex.search(time_span[0].text)
#     NO1_time = match.group(1)
#     # print(NO1_time)

#     NO1_tbody = soup_homepage.select('.CnbTable_550')
#     NO1_list_tr = NO1_tbody[1].find_all('tr')
#     cnt = 0
#     for td in NO1_list_tr:
#         if cnt == 0:
#             cnt = cnt + 1
#             continue
#         NO1_list_td = td.find_all('td')
#         # print(NO1_list_td[0].text)
#         if NO1_list_td[0].text.find('large') != -1:
#             continue
#         regex = re.compile(r'\((.+)\)')
#         match = regex.search(NO1_list_td[0].text)
#         cash_spot = NO1_list_td[1].text
#         moneyIN = NO1_list_td[2].text.strip()
#         moneyOUT = NO1_list_td[3].text.strip()

#         try:
#             money_type = match.group(1)
#             if money_type == searchTYPE or searchTYPE == 'X':
#                 if cash_spot == 'Spot':
#                     firstbank.append({
#                         'type':money_type,
#                         'cashIN':0,
#                         'cashOUT':0,
#                         'spotIN':float(moneyIN),
#                         'spotOUT':float(moneyOUT)
#                     })
#                 else:
#                     for x in firstbank:
#                         if x['type'] == money_type:
#                             x['cashIN'] = float(moneyIN)
#                             x['cashOUT'] = float(moneyOUT)
#                 # if money_type == searchTYPE:
#                 #     break
#         except:
#             continue
                
# # NO1_craw_moneyType()
# # for x in firstbank:
# #     print(x)

# # "AAA(BBB)".split("(")[1].split(")")[0]


# ### ---兆豐銀行--- ###  -----------------------------------------------
# def mega_craw_moneyType():
#     searchTYPE = 'X'
#     global megabank
#     megabank = []
#     browser = webdriver.Chrome()
#     browser.get("https://wwwfile.megabank.com.tw/other/bulletin02_02.asp")
#     time.sleep(0.5)
#     soup_homepage = BeautifulSoup((browser.page_source),'lxml')
#     browser.close()

#     time_date = soup_homepage.select('#dataDate')
#     time_time = soup_homepage.select('#dataTime')
#     # print(time_date[0].text + ' ' + time_time[0].text)

#     mega_list_tbody = soup_homepage.select('#contentTbody')
#     mega_list_tr = mega_list_tbody[0].find_all('tr')
#     for i in mega_list_tr:
#         mega_list_td = i.find_all('td')

#         regex = re.compile(r'\[(.+)\]')
#         match = regex.search(mega_list_td[0].text)
#         money_type = match.group(1)
#         if searchTYPE == money_type or searchTYPE == 'X':
#             inputMoney = []
#             for i in range(1,5):
#                 if mega_list_td[i].text == '---':
#                     inputMoney.append(0)
#                 else:
#                     inputMoney.append(float(mega_list_td[i].text))

#             megabank.append({
#                 'type':money_type,
#                 'cashIN':inputMoney[1],
#                 'cashOUT':inputMoney[3],
#                 'spotIN':inputMoney[0],
#                 'spotOUT':inputMoney[2]
#             })
#             if searchTYPE == money_type:
#                 break
#         # break

# # mega_craw_moneyType()
# # for i in megabank:
# #     print(i)


# ### ---台灣銀行--- ### -------------------------------------
# def TW_craw_moneyType():
#     searchTYPE = 'X'
#     global taiwanbank
#     taiwanbank = []
#     webHomePage = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
#     res_homepage = requests.get(webHomePage)
#     res_homepage.encoding='utf8'
#     soup_homepage = BeautifulSoup((res_homepage.text),'lxml')

#     time_span = soup_homepage.select('.time')
#     TW_time = time_span[0].text
#     # print(TW_time)

#     TW_tbody = soup_homepage.select('tbody')
#     TW_list_tr = TW_tbody[0].find_all('tr')
#     for i in TW_list_tr:
#         TW_list_td = i.find_all('td')
#         regex = re.compile(r'\((.+)\)')
#         match = regex.search(TW_list_td[0].text)

#         if match.group(1) == searchTYPE or searchTYPE == 'X':
#             intType = []
#             for j in range(1,5):
#                 if TW_list_td[j].text == '-':
#                     intType.append(0)
#                 else:
#                     intType.append(float(TW_list_td[j].text))
            
#             taiwanbank.append({
#                 'type':match.group(1),
#                 'cashIN':intType[0],
#                 'cashOUT':intType[1],
#                 'spotIN':intType[2],
#                 'spotOUT':intType[3],
#             })
#             if match.group(1) == searchTYPE:
#                 break

# # TW_craw_moneyType()
# # for i in taiwanbank:
# #     print(i)


# ### ---國泰世華--- ###  -------------------------------
# def cathay_craw_moneyType():
#     searchTYPE = 'X'
#     global cathaybank
#     cathaybank = []
#     webHomePage = "https://www.cathaybk.com.tw/cathaybk/personal/deposit-exchange/rate/currency-billboard/"
#     res_homepage = requests.get(webHomePage)
#     res_homepage.encoding='utf8'
#     soup_homepage = BeautifulSoup((res_homepage.text),'lxml')

#     time_span = soup_homepage.select('.paragraph')
#     time_format = time_span[0].text.split('：')[1] 
#     time_format = time_format.replace('年','/')
#     time_format = time_format.replace('月','/')
#     time_format = time_format.replace('日',' ')
#     time_format = time_format.replace('時',':')
#     time_format = time_format.replace('分','')
#     # print(time_format)
#     cathay_list_tbody = soup_homepage.select('tbody')
#     # print(cathay_list_tbody)

#     cathay_list_tr = cathay_list_tbody[2].find_all('tr')
#     # print(cathay_list_tr)
#     # cathay_list_td = cathay_list_tr[0].find_all('td')
#     for i in cathay_list_tr:
#         cathay_list_td = i.find_all('td')
#         regex = re.compile(r'\((.+)\)')
#         match = regex.search(cathay_list_td[0].text)
#         moneyType = match.group(1)
#         if moneyType == searchTYPE or searchTYPE == 'X':
#             moneyIN = cathay_list_td[1].text
#             moneyOUT = cathay_list_td[2].text
#             if (cathay_list_td[0].text).find('Cash') != -1:  #有找到！表示是現金匯率
#                 for i in cathaybank:
#                     if i['type'] == moneyType:
#                         i['cashIN'] = float(moneyIN)
#                         i['cashOUT'] = float(moneyOUT)
#             else:
#                 cathaybank.append({
#                 'type':moneyType,
#                 'cashIN':0,
#                 'cashOUT':0,
#                 'spotIN':float(moneyIN),
#                 'spotOUT':float(moneyOUT),
#             })
#             # if moneyType == searchTYPE:
#             #     break
    
# # cathay_craw_moneyType()
# # for i in cathaybank:
# #     print(i)

# ### ---玉山銀行--- ### ---------------------------------
# def esun_craw_moneyType():
#     # print('esun')
#     searchTYPE = 'X'
#     global esunbank
#     esunbank = []
#     webHomePage = "https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates"
#     res_homepage = requests.get(webHomePage)
#     res_homepage.encoding='utf8'
#     soup_homepage = BeautifulSoup((res_homepage.text),'lxml')

#     time_span = soup_homepage.select('#LbQuoteTime')
#     time_format = time_span[0].text
#     time_format = time_format.replace('年','/')
#     time_format = time_format.replace('月','/')
#     time_format = time_format.replace('日','')
#     # print(time_format)

#     esun_list = soup_homepage.select('.tableContent-light')
#     for i in esun_list:
#         esun_list_td = i.find_all('td')
#         regex = re.compile(r'\((.+)\)')
#         match = regex.search(esun_list_td[0].text)
#         moneyType = match.group(1)

#         if moneyType == searchTYPE or searchTYPE == 'X':
#             inputMoney = []
#             for j in range(1,7):
#                 if j == 3 or j == 4:
#                     continue
#                 if esun_list_td[j].text == '':
#                     inputMoney.append(0)
#                 else:
#                     inputMoney.append(float(esun_list_td[j].text))
            
#             esunbank.append({
#                 'type':moneyType,
#                 'cashIN':inputMoney[2],  
#                 'cashOUT':inputMoney[3],
#                 'spotIN':inputMoney[0],
#                 'spotOUT':inputMoney[1],
#             })
#             if moneyType == searchTYPE:
#                 break
#         # break
#     # for i in esunbank:
#     #     print(i)

# # esun_craw_moneyType()


# ### JSON格式
# # data_json = json.dumps(ans)
# # print(data_json)

# # ans_unJSON = json.loads(data_json)
# # print(ans_unJSON)
# # for i in ans_unJSON:
# #     print(i)
#     # if i['bank'] == '第一銀行\n':
#         # print(i['即期賣出'])


# def main():
#     global ans, firstbank, megabank, taiwanbank, cathaybank, esunbank
#     print('main')
#     all_craw_moneyType()
#     print('all')
#     NO1_craw_moneyType()
#     print('NO1')
#     # print(firstbank)
#     mega_craw_moneyType()
#     print('mega')
#     # print(megabank)
#     TW_craw_moneyType()
#     print('TW')
#     # print(taiwanbank)
#     cathay_craw_moneyType()
#     print('cathay')
#     # print(cathaybank)
#     esun_craw_moneyType()
#     print('esun')
#     # print(esunbank)
#     ### 新增資料庫
#     for i in ans:
#         # print('db')
#         new_obj = AllMoneyInfo.objects.filter(moneyType=i['type'],bank=i['bank']).last()
#         # print(new_obj)
#         if new_obj == None:
#             new_obj = AllMoneyInfo(
#                         moneyType=i['type'],
#                         cashIN=i['cashIN'],
#                         cashOUT=i['cashOUT'],
#                         spotIN=i['spotIN'],
#                         spotOUT=i['spotOUT'],
#                         bank=i['bank'],
#                         fee=i['fee'],
#                         updateTime=i['update']
#                     )
#         else:
#             new_obj.cashIN = i['cashIN']
#             new_obj.cashOUT = i['cashOUT']
#             new_obj.spotIN = i['spotIN']
#             new_obj.spotOUT=i['spotOUT']
#             new_obj.fee = i['fee']
#             new_obj.updateTime=i['update']

#         new_obj.save()

#     allcheck = []
#     allcheck.append(firstbank)
#     allcheck.append(megabank)
#     allcheck.append(taiwanbank)
#     allcheck.append(cathaybank)
#     allcheck.append(esunbank)
#     # print(allcheck)
#     # print(len(allcheck))
#     for x in range(0,5):
#         bank = ''
#         ##第一銀行
#         for i in allcheck[x]:
#             # print(i)
#             if x == 0:
#                 bank = '第一銀行'
#             elif x == 1:
#                 bank = '兆豐銀行'
#             elif x == 2:
#                 bank = '臺灣銀行'
#             elif x == 3:
#                 bank = '國泰世華'
#             elif x == 4:
#                 bank = '玉山銀行'

#             new_obj = AllMoneyInfo.objects.filter(moneyType=i['type'],bank=bank).last()
#             if new_obj == None:
#                 print(i['type'] + '：None')
#                 continue
#             print(new_obj)
#             print(new_obj.moneyType + new_obj.bank)
#             # inputType = []
#             if i['cashIN'] != 0:
#                 new_obj.cashIN = i['cashIN']
#             if i['cashOUT'] != 0:
#                 new_obj.cashOUT = i['cashOUT']
#             if i['spotIN'] != 0:
#                 new_obj.spotIN = i['spotIN']
#             if i['spotOUT'] != 0:
#                 new_obj.spotOUT=i['spotOUT']
#             new_obj.save()

#     # try:
#     userInfo_List_IN = UserInfo.objects.filter(INorOUT='IN')
#     # print(userInfo_List)
#     # print(userInfo_List[0])
#     for k in userInfo_List_IN:
#         bank = k.bank
#         moneyType = k.moneyType
#         now = AllMoneyInfo.objects.filter(bank=bank,moneyType=moneyType).last()
#         if now != None:
#             for i in nameToName:
#                 if i['code'] == moneyType:
#                     moneyType = i['name']
#             # print(now.spotOUT)
#             # print(k.lowerBound)
#             if float(k.lowerBound) > float(now.spotOUT): #我買進要最低 也就是銀行賣出
#                 textNote = '匯率提醒！！！\n' + bank + '的' + moneyType + '目前是：'+ now.spotOUT + '\n已經低於 ' + k.lowerBound + '了！'
#                 line.push_message(k.lineBotID,TextSendMessage(text=textNote))
#                 print('提醒使用者IN')
#                 k.delete()

#     userInfo_List_OUT = UserInfo.objects.filter(INorOUT='OUT')
#     for k in userInfo_List_OUT:
#         bank = k.bank
#         moneyType = k.moneyType
#         now = AllMoneyInfo.objects.filter(bank=bank,moneyType=moneyType).last()
#         if now != None:            
#             for i in nameToName:
#                 if i['code'] == moneyType:
#                     moneyType = i['name']
#             if float(k.lowerBound) < float(now.spotOUT): #我買進要最低 也就是銀行賣出
#                 textNote = '匯率提醒！！！\n' + bank + '的' + moneyType + '目前是：'+ now.spotOUT + '\n已經高於 ' + k.lowerBound + '了！'
#                 line.push_message(k.lineBotID,TextSendMessage(text=textNote))
#                 print('提醒使用者OUT')
#                 k.delete()
#     # print('0000000000')         
#     # test = AllMoneyInfo.objects.filter(moneyType='JPY')
#     # print(len(test))
#     # test_sort = test.order_by('cashIN')
#     # which = 'cashIN'
#     # print(test_sort)
#     # for x in test_sort:
#     #     print(x)
#     #     print(x.bank)


# main()



