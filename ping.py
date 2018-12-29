import os
from datetime import datetime
import telebot
from telebot import apihelper
now = datetime.now()
now2=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
apihelper.proxy = {'https':'http://142.93.120.75:3128'}
hostname = {'10.140.4.11':'F411','10.140.4.12':'F412','10.140.4.14':'F414','10.140.4.15':'F415','10.140.4.16':'F416','10.140.4.17':'F417'}
channel = "614864940"
token = '768435358:AAG-7UW0z6sT20M4hRyDyd8QgzT1v44zx5s'
def res(dom):
    response = os.system('ping ' + dom)
    return (response)
bot = telebot.TeleBot(token)
for domain in hostname:
    if res(domain) == 0:
      print(hostname[domain] + ' is up!')
    else:
      print(hostname[domain] + ' is down!')
      bot.send_message(channel, hostname[domain] + ' is down!')
bot.send_message(channel, 'Проверка закончена '+now2 + '')
#bot.polling(none_stop=True, interval=0)
