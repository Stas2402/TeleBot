import telebot
import requests

bot = telebot.TeleBot('1012392887:AAHoiinJ809WkYfhC3gMzsBmEXcS2Lrypss')
foods = set(['еда', "продукты", "жратва", 'хлеб', 'атб', 'варус', 'сильпо', 'магазин'])
alcohols = set(['пиво', 'вино', 'бухло', 'пивас', 'алкоголь', 'выпивка', 'сидр', 'ром'])
coffees = set(['кофе', 'чай'])
public_serv = set(['комуналка', 'свет', 'вода', 'газ', 'отопление', 'коммунальные услуги', 'жилье'])
transports = set(['трамвай', 'проезд', 'дорога', 'маршрутка'])
creditss = set(['кредит', 'долг'])
trips = set(['путешествие', 'поездка', 'отпуск'])


food = 0
alcohol = 0
coffee = 0
public_services = 0
transport = 0
credit = 0
trip = 0
budget = {
    'food': food,
    'alcohol': alcohol,
    'coffee': coffee,
    'public services': public_services,
    'transport': transport,
    'credit': credit,
    'trip': trip,
}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['current'])
def current_message(message):
    current = []
    for key in budget.keys():
        string = key + ' {}\n'.format(budget[key])
        current.append(string)
    reply = ''.join(current)
    bot.send_message(message.chat.id, reply)

@bot.message_handler(commands=['categories'])
def categories_message(message):
    categories = []
    for key in budget.keys():
        categories.append(key + '\n')
    reply = ''.join(categories)
    bot.send_message(message.chat.id, reply)

@bot.message_handler(content_types=['text'])
def added(message):
    what = message.text.split(' ')
    if len(what) <= 2:
        value = 0
        str = 0
        Fail = False
        for k in what:
            if k.isdigit():
                value = int(k)
            else:
                str = k.lower()
        if str in foods:
            budget['food'] += value
        elif str in alcohols:
            budget['alcohol'] += value
        elif str in coffees:
            budget['coffee'] += value
        elif str in public_serv:
            budget['public services'] += value
        elif str in transports:
            budget['transport'] += value
        elif str in creditss:
            budget['credit'] += value
        elif str in trips:
            budget['trip'] += value
        else:
            bot.send_message(message.chat.id, 'Не найдено похожей категории. Попробуй еще раз.')
            Fail = True
        if Fail == False:
            bot.send_message(message.chat.id, 'Окей, {} грн потрачено на {}'.format(value, str))



    print(message.text)
    print(budget)


bot.polling()
