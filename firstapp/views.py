from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from firstapp.models import UserStatus, UserInfo, AllMoneyInfo

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,StickerSendMessage, 
    LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, PostbackAction,
    TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction,
     ConfirmTemplate,  PostbackEvent, CarouselTemplate, CarouselColumn, FollowEvent)
from urllib.parse import parse_qsl

line_bot_api = LineBotApi('k5bOp3T9Djg6kva7/uffZhDBCs8bOLHZZ+c7ujyyQNOXgW2BYmOaeSh9dm02GePq+gD1+nUKVeDNGWByoEhtXsc6KjcXK4Ho1VKNPIAQv22fuirxpUOKm0gUSbFKyRwMXt4/z4osUDN+NeLK7CH54gdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('a0b0bd5107877891df3a337c5355bfc6')

status = ['現金/現鈔', '日幣', '買入','臺灣銀行']
def sendQuickreply(event):
    #try:
        message = TextSendMessage(
            text = "請輸入想要的外幣種類\n(若無則請嘗試自行輸入)",
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/fQ7kKiA.png',
                        action = PostbackAction(label='日圓', text='日圓' ,data = 'action=money&id=JPY')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/pFFFD8Q.png',
                        action = PostbackAction(label='美元', text='美元',data = 'action=money&id=USD')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/vGwLo0l.png',
                        action = PostbackAction(label='人民幣', text='人民幣',data = 'action=money&id=CNY')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/5LO1Vqj.png',
                        action = PostbackAction(label='歐元', text='歐元' ,data = 'action=money&id=EUR')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/FUKAQgh.png',
                        action = PostbackAction(label='港幣', text='港幣',data = 'action=money&id=HKD')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/1YWgDmh.png',
                        action = PostbackAction(label='英鎊', text='英鎊',data = 'action=money&id=GBP')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/stkbCy8.png',
                        action = PostbackAction(label='澳幣', text='澳幣' ,data = 'action=money&id=AUD')
                    ),
          
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/G0ptHPN.png',
                        action = PostbackAction(label='加幣', text='加幣',data = 'action=money&id=CAD')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/fTQ4SeJ.png',
                        action = PostbackAction(label='新加坡幣', text='新加坡幣',data = 'action=money&id=SGD')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/62KIsYq.png',
                        action = PostbackAction(label='瑞士法郎', text='瑞士法郎' ,data = 'action=money&id=CHF')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/R5761OJ.png',
                        action = PostbackAction(label='韓元', text='韓元',data = 'action=money&id=KRW')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/UkwVSMJ.png',
                        action = PostbackAction(label='泰銖', text='泰銖',data = 'action=money&id=THB')
                    ),
                    QuickReplyButton(
                        image_url = 'https://i.imgur.com/iT4rtaq.png',
                        action = PostbackAction(label='菲律賓比索', text='菲律賓比索',data = 'action=money&id=PHP')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    #except:
        #line_bot_api.reply_message(event.reply_token,
        #TextMessage(text='發生錯誤!'))

def sendBuyORSell(event):
    try:
        message2 = TemplateSendMessage(
            alt_text = '確認買/賣類型',
            template = ConfirmTemplate(
                text='請選擇要買或賣該項貨幣',
                actions=[
                    MessageTemplateAction(
                        label='買入',
                        text = '@買入',
                    ),
                    MessageTemplateAction(
                        label='賣出',
                        text = '@賣出',
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message2)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextMessage(text='發生錯誤!'))

def sendBanksss(event):
    #try:
        #if status[0]=='現金/現鈔' :
        #    print('加上手續費')
        #    fee = '\n手續費 : $100/次'
        #else:
        #    fee = ''

        ##提取使用者訊息
        userID = event.source.user_id
        userStatus = UserStatus.objects.get(lineBotID=userID)
        print(userStatus)
        moneyORpass = userStatus.moneyORpass
        moneyType= userStatus.moneyType
        buyORsell = userStatus.buyORsell

        if moneyORpass =='現金/現鈔' and buyORsell == '買入':
            which = 'cashOUT'
        elif moneyORpass =='現金/現鈔' and buyORsell == '賣出':
            which = 'cashIN'
        elif moneyORpass =='即期/存摺' and buyORsell == '買入':
            which = 'spotOUT'
        elif moneyORpass =='即期/存摺' and buyORsell == '賣出':
            which = 'spotIN'
        print(which)

        MoneyInfo = AllMoneyInfo.objects.filter(moneyType = moneyType).order_by(which)[0:3]
        MoneyInfo2 = MoneyInfo.reverse()
        if which == 'cashOUT':
            test1 = MoneyInfo.values('cashOUT')
            print(test1)
            print(test1[0]['cashOUT'])
        elif which == 'spotOUT':
            test1 = MoneyInfo.values('spotOUT')
        elif which == 'cashIN':
            test1 = MoneyInfo.values('spotOUT')
        elif which == 'spotIN':
            test1 = MoneyInfo.values('spotOUT')

        test1Value = []
        for i in range(3):
            test1Value.append(test1[i][which])
        print(test1Value)

        CarouselColumns = []
        for i in range(3):
            print(i)
            print(MoneyInfo[i])
            CarouselColumns.append(
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item1.jpg',
                    title = MoneyInfo[i].bank,
                    text = userStatus.moneyType+'  (銀行)'+which+test1Value[i]+'\n' ,
                    actions = [
                        PostbackTemplateAction(
                            label='換算匯率',
                            data='action=換算匯率&bank='+MoneyInfo[i].bank,
                        ),
                        PostbackTemplateAction(
                            label='設定提醒',
                            data='action=設定提醒',
                        ),
                        URITemplateAction(
                            label='附近銀行',
                            uri='http://example.com/1'
                        ),     
                    ] 
                )
            )
        
        message3 = TemplateSendMessage(
            alt_text = '選擇指定銀行',
            template = CarouselTemplate(
                columns=CarouselColumns
                #[
                    # CarouselColumn(
                    #     thumbnail_image_url='https://example.com/item1.jpg',
                    #     title='臺灣銀行',
                    #     text=status[1]+'  '+status[0]+': 0.38 \n更新時間: 10:30'+fee,
                    #     actions=[
                    #         PostbackTemplateAction(
                    #             label='換算匯率',
                    #             data='action=換算匯率&bank=臺灣銀行',
                    #         ),                            
                    #         PostbackTemplateAction(
                    #             label='設定提醒',
                    #             data='action=設定提醒',
                    #         ),
                    #         URITemplateAction(
                    #             label='附近銀行',
                    #             uri='http://example.com/1'
                    #         )
                    #     ]
                    # ),
                    # CarouselColumn(
                    #     thumbnail_image_url='https://example.com/item2.jpg',
                    #     title='大力銀行',
                    #     text=status[1]+'\n'+status[0]+': 0.38 \n更新時間: 10:30',
                    #     actions=[
                    #         MessageTemplateAction(
                    #             label='message1',
                    #             text='message text1'
                    #         ),                            
                    #         PostbackTemplateAction(
                    #             label='postback1',
                    #             text='postback text1',
                    #             data='action=buy&itemid=1'
                    #         ),
                    #         URITemplateAction(
                    #             label='uri2',
                    #             uri='http://example.com/1'
                    #         )
                    #     ]
                    # )
                #]
            )
        )
        line_bot_api.reply_message(event.reply_token,message3)
    # except:
    #     line_bot_api.reply_message(event.reply_token,
    #     TextMessage(text='發生錯誤!'))

def sendChangedMoney(event):
    try:
        message4 = status[3]+'\n'+status[1]+event.message.text+'\n換匯後: $'
        line_bot_api.reply_message(event.reply_token,TextMessage(text=message4))
    except:
        line_bot_api.reply_message(event.reply_token,
        TextMessage(text='發生錯誤!'))

def sendConfrimAlert(event) :
    try:
        message4 = TemplateSendMessage(
            alt_text = '確認提醒設定',
            template = ConfirmTemplate(
                text='請確認是否將\n'+status[3]+' '+status[0]+' '+event.message.text+'\n設定提醒?',
                actions=[
                    PostbackTemplateAction(
                        label='是',
                        data = 'action=是',
                    ),
                    PostbackTemplateAction(
                        label='否',
                        data = 'action=否',
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message4)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextMessage(text='發生錯誤!'))
@csrf_exempt
def callback(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        # get X-Line-Signature header value
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        # get request body as text
        body = request.body.decode('utf-8')

        # handle webhook body
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            if isinstance(event, FollowEvent):
                print("in Follow")
                print(event.source.user_id)
                userStatus = UserStatus(lineBotID=event.source.user_id)
                userStatus.save()
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='Follow...')
                )
            # 文字訊息
            if isinstance(event, MessageEvent):                
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    print(mtext)
                    if mtext == '@幣別一覽':
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text='功能尚未完成\n敬請期待...')
                        )
                    if mtext == '@現金/現鈔' or mtext == '@即期/存摺':
                        status[0] = mtext
                        # userStatus = UserStatus.objects.get(lineBotID=event.source.user_id)
                        # userStatus.moneyORpass = mtext[1::]
                        # userStatus.save()
                        print(mtext[1::])
                        print('sendQuickreply')
                        sendQuickreply(event)             
                    # elif mtext[-1] == '幣' or mtext[-1] =='元':
                    #     #status[1] = mtext
                    #     print(status)
                    #     print('sendBuyORSell')
                    #     sendBuyORSell(event)
                    elif mtext == '@買入' or mtext == '@賣出':
                        #status[2] = mtext
                        #print(status)
                        userStatus = UserStatus.objects.get(lineBotID=event.source.user_id)
                        userStatus.buyORsell = mtext[1::]
                        userStatus.save()
                        print(mtext[1::])
                        print('sendBanksss')
                        sendBanksss(event)
                    elif mtext[0] == '$':
                        #print(status)
                        print('sendChangedMoney')
                        sendChangedMoney(event)
                    elif mtext[0] == '%':
                        print('sendConfrimAlert')
                        sendConfrimAlert(event)
            # postback訊息
            if isinstance(event, PostbackEvent):
                backdata = dict(parse_qsl(event.postback.data))
                print(backdata)
                if backdata.get('action') == '換算匯率':
                    print('換算匯率...')
                    userStatus = UserStatus.objects.get(lineBotID=event.source.user_id)
                    userStatus.bank = backdata.get('bank')
                    userStatus.save()
                    #status[3] = backdata.get('bank')
                    #status[4] = '換算匯率'
                    print(status)
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text='請輸入臺幣:\n範例輸入: $100')
                    )
                elif backdata.get('action') == '設定提醒':
                    print('設定提醒...')
                    #status[3] = backdata.get('bank')
                    userStatus = UserStatus.objects.get(lineBotID=event.source.user_id)
                    userStatus.bank = backdata.get('bank')
                    userStatus.save()
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text='請輸入提醒匯率值:\n範例輸入: %0.22')
                    )
                elif backdata.get('action') == '是':
                    print('匯率設定完成')
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='提醒設定END')
                )
                elif backdata.get('action') == '否':
                    print('重新設定匯率')
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='重新輸入提醒匯率值:\n範例輸入: %0.22')
                )                
                elif backdata.get('action') == 'money':
                    userStatus = UserStatus.objects.get(lineBotID=event.source.user_id)
                    userStatus.moneyType = backdata.get('id')
                    userStatus.save()
                    print('sendBuyORSell')
                    sendBuyORSell(event)

                # line_bot_api.reply_message(
                #     event.reply_token,
                #     TextSendMessage(text=event.message.text)
                # )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()