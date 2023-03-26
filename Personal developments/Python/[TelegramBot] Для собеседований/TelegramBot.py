 
from imghdr import tests
import telebot
from telebot import types # для указание типов
import config
import psycopg2 
import datetime
import time


conn = psycopg2.connect(dbname='TelegramBot',user='TgBot',password='qwerty',host='localhost')

kol = 0 
config.token = ""; #"Токен бота";
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    global kol 
    bot.send_message(message.chat.id, text="Запуск тестового бота")
    #kol = 1

@bot.message_handler(commands=['Add'])
def addZauvka(message):
    global kol
    kol = 1
    Zayvka(message)


SpisokDolznost = []
voprosvariantOtveta = []

Fam = ""
Name = ""
Otch = ""
DateDir = ""
Dolznost = 0
dolznoDolznostRodutelstID = -1
def Zayvka(message):
    global kol
    if (kol == 1):
        bot.send_message(message.chat.id,text="Введите Фамилию:")
         #Zayvka(message)
    elif (kol == 2):
        bot.send_message(message.chat.id,text="Введите Имя:")
         
        #Zayvka(message)
    elif (kol == 3):
        bot.send_message(message.chat.id,text="Введите Отчество:")
         
    elif (kol == 4):
        bot.send_message(message.chat.id,text="Введите Дату Рождения (формат: 2001-02-13):")


    elif (kol == 5):
        markup = types.InlineKeyboardMarkup()
        cursor = conn.cursor() 
        cursor.execute('SELECT * FROM "Dolznost"')
        global SpisokDolznost
        for row in cursor:
            markup.add(types.InlineKeyboardButton(text=str(row[1]),callback_data="Dolzn_"+str(row[0])))
            SpisokDolznost.append(row[1])
        bot.send_message(message.chat.id,text="Выберите желаемую должность:",reply_markup=markup)
    elif (kol == 6):

        global dolznoDolznostRodutelstID
        cursor = conn.cursor() #(1,1,'+Fam+','+Name+','+Otch+')
        cursor.execute('SELECT "id", "Opisanue" FROM "ParametrDolznost" Where "ParametrDolznost"."Rodutel" is null and "ParametrDolznost"."Dolznost" = '+Dolznost)
        for row in cursor:
            time.sleep(0.5)
            dolznoDolznostRodutelstID = row[0]
            bot.send_message(message.chat.id,text=str(row[1]))

        cursor.execute('SELECT "id","Opisanue","VariantOtveta" FROM "ParametrDolznost" Where "ParametrDolznost"."Rodutel" = '+str(dolznoDolznostRodutelstID)+' and "ParametrDolznost"."Dolznost" = '+Dolznost)        
        variantOtveta = ''
        idVariantOtvet = ''
        messageVarOtv = ''
        for row in cursor:
            messageVarOtv = row[1]
            variantOtveta = row[2]
            idVariantOtvet = row[0]
        
        markup = types.InlineKeyboardMarkup()
        global voprosvariantOtveta
        voprosvariantOtveta = variantOtveta.split('/')
        for i in range(len(voprosvariantOtveta)):
            markup.add(types.InlineKeyboardButton(text=str(voprosvariantOtveta[i]),callback_data="VarOtvet_"+str(idVariantOtvet)))
        time.sleep(1.0)
        bot.send_message(message.chat.id,text=messageVarOtv,reply_markup=markup)

    elif (kol == 7):
        bot.send_message(message.chat.id,text="Хороший выбор!\nСпасибо за тестирование!")
        kol = -1
        print(Fam+" "+Name+" "+Otch)
        AddZayvka()



    kol+=1

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global Dolznost
    # Если сообщение из чата с ботом
    if call.message:
        # - Выбранная должность
        if  call.data.find("Dolzn_") > -1:
            rasp = call.data.find("_")
            Dolznost = str(call.data)[rasp+1:]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы выбрали должность: ["+SpisokDolznost[int(Dolznost)-1]+"]")
            print(Dolznost)
            Zayvka(call.message)
        
        # - Выбранный вариант ответа на существующий вопрос
        if  call.data.find("VarOtvet_") > -1:
            buffer = call.data.find("_")
            IDVoprosKDolznostu = str(call.data)[buffer+1:]
            cursor = conn.cursor()
            cursor.execute('SELECT "SvyzanoePoleOtveta" FROM "ParametrDolznost" Where "ParametrDolznost"."Rodutel" = '+str(dolznoDolznostRodutelstID)+' and "ParametrDolznost"."Dolznost" = '+Dolznost+' and "ParametrDolznost"."id" ='+IDVoprosKDolznostu)        
            SvyzanoePoleOtveta = ""
            for row in cursor:
                SvyzanoePoleOtveta = row[0]

            if SvyzanoePoleOtveta == "zarplata":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы выбрали зарплату: ["+str(voprosvariantOtveta[int(IDVoprosKDolznostu)])+"]")

def AddZayvka():

    cursor = conn.cursor() #(1,1,'+Fam+','+Name+','+Otch+')
    cursor.execute('INSERT INTO "Zayvku"("DateBitr","Dolznost","Status","SotrF","SotrN","SotrO") VALUES (%s,%s,%s,%s,%s,%s)',
                   (DateDir,Dolznost,1,Fam,Name,Otch))
    conn.commit()
    #cursor.close()
    print("Заява добавлена в БД")


@bot.message_handler(content_types=['text'])
def func(message):
    global kol
    global Fam
    global Name
    global Otch
    global DateDir

    if (kol == 2):
        Fam = message.text 
    elif (kol == 3):
        Name = message.text  
    elif (kol == 4):
        Otch = message.text
    elif (kol == 5):
        DateDir = datetime.datetime.strptime(message.text,'%Y-%m-%d').strftime('%Y-%m-%d')
        
    if kol>=1 and message.text != "":
        Zayvka(message)
    
bot.polling(none_stop=True)