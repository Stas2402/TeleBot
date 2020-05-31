import telebot
import requests

bot = telebot.TeleBot('1012392887:AAHoiinJ809WkYfhC3gMzsBmEXcS2Lrypss')

foods = set(['еда', "продукты", "жратва", 'хлеб', 'атб', 'варус', 'сильпо', 'магазин'])
alcohols = set(['пиво', 'вино', 'бухло', 'пивас', 'алкоголь', 'выпивка', 'сидр', 'ром'])
coffees = set(['кофе', 'чай'])
public_serv = set(['комуналка', 'свет', 'вода', 'газ', 'отопление', 'коммунальные услуги', 'жилье', 'газ'])
transports = set(['трамвай', 'проезд', 'дорога', 'маршрутка'])
creditss = set(['кредит', 'долг'])
trips = set(['путешествие', 'поездка', 'отпуск'])
others = set(['другое', 'еще'])
food, alcohol, coffee, public_services, transport, credit, trip, other = 0, 0, 0, 0, 0, 0, 0, 0
budget = {
    'food': food,
    'alcohol': alcohol,
    'coffee': coffee,
    'public services': public_services,
    'transport': transport,
    'credit': credit,
    'trip': trip,
    'other': other,
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
    value = 0
    str = 0
    Fail = False
    if len(what) == 2:
        for k in what:
            try:
                value = int(k)
            except:
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
        elif str in others:
            budget['other'] += value
        else:
            bot.send_message(message.chat.id, 'Не найдено похожей категории. Попробуй еще раз.')
            Fail = True
        if Fail == False:
            if value > 0:
                bot.send_message(message.chat.id, 'Окей, {} грн потрачено на {}'.format(value, str))
            else:
                bot.send_message(message.chat.id, 'Окей, {} грн вычли из {}'.format(value, str))
    else:
        bot.send_message(message.chat.id, "Неверный формат. Используй, например, 'газ 500'")


    print(str)
    print(value)
    print(budget)

@bot.message_handler(commands=['previos'])
def previos(message):
    bot.send_message(message.chat.id, 'Нет данных о предидущем месяце')








bot.polling()
