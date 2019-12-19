import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import json, re, datetime, time

ans = []
firstbank = []
megabank = []
taiwanbank = []
cathaybank = []
esunbank = []

# XXXbank.append({
#     'type':貨幣名稱 'USA',
#     'cashIN':float(), =現金 買入匯率(第一) /現金買匯(兆豐) /本行買入(台銀) /銀行買進(國泰) / 銀行買入(玉山)
#     'cashOUT':float(),=現金 賣出匯率       /現金賣匯      /本行賣出      /銀行賣出      / 銀行賣出
#     'spotIN':float()  =即期 即期買匯    
#     'spotOUT':float(),=即期 
# })

###  ----比率網---- ###

def money_bank(listTbody,money_type):  # 該項貨幣(1)查詢各銀行(n)匯率，已爬到內容(listTbody)作整理
    cnt = 0
    bank_all = listTbody.find_all('tr')
    # print(bank_all)
    for x in bank_all:
        if cnt == 0:
            cnt = cnt + 1
            continue
        else:
            row = x.find_all('td')
            bank = row[0].text.replace('\n','')
            intType = []
            for i in range(1,5):
                if row[i].text == '--':
                    intType.append(0)
                else:
                    intType.append(float(row[i].text))
            date = datetime.datetime.now()
            fee = row[6].text.replace(' ','')
            ans.append({
                'type':money_type,
                'bank':bank,
                'cashIN':intType[0],
                'cashOUT':intType[1],
                'spotIN':intType[2],
                'spotOUT':intType[3],
                'fee':fee,
                'update':str(date.year) +'/'+ str(date.month) +'/'+ str(date.day) +' '+ row[5].text
            })
        # except:
        #     continue
    return
def all_craw_moneyType(money_type):  #帶入要查詢的貨幣名稱 get JSON格式的ans
    webHomePage = "https://www.findrate.tw"
    res_homepage = requests.get(webHomePage)
    res_homepage.encoding='utf8'
    soup_homepage = BeautifulSoup((res_homepage.text),'lxml') 
    listMoney_type = soup_homepage.select('.listbtns')
    li_a = listMoney_type[0].select('a')

    for href in li_a:
        lihref = href.get('href')
        regex = re.compile('\/(.+)\/')
        match = regex.search(lihref)
        if match.group(1) == money_type:
            # if href.text == '南非幣' or href.text == '印度披索' or href.text == '丹麥幣' or href.text == '墨西哥比索' or href.text == '土耳其里拉':
            #     continue
            res_money = requests.get(webHomePage+lihref)
            res_money.encoding='utf8'
            soup_money = BeautifulSoup((res_money.text),'lxml')
            moneyList = soup_money.select('tbody')
            
            money_bank(moneyList[1],match.group(1))
            break

all_craw_moneyType('JPY')
for x in ans:
    print(x)