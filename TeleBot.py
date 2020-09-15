import telebot
import pickle

bot = telebot.TeleBot('1012392887:AAHoiinJ809WkYfhC3gMzsBmEXcS2Lrypss')

categories = [['food', 'еда', "продукты", "жратва", 'хлеб', 'атб', 'варус', 'сильпо', 'магазин'],
              ['alcohol', 'пиво', 'вино', 'бухло', 'пивас', 'алкоголь', 'выпивка', 'сидр', 'ром'],
              ['coffee', 'кофе', 'чай'],
              ['public services', 'комуналка', 'свет', 'вода', 'газ', 'отопление', 'коммунальные услуги', 'жилье',
               'газ'],
              ['transport', 'трамвай', 'проезд', 'дорога', 'маршрутка'],
              ['credit', 'кредит', 'долг'],
              ['trip', 'путешествие', 'поездка', 'отпуск'],
              ['other', 'другое', 'еще'],
              ]

def save_budget(content):
    with open('budget.txt', 'wb') as file:
        pickle.dump(content, file)

def load_budget():
    try:
        with open('budget.txt', 'rb') as file:
            budget = pickle.load(file)
            return budget
    except:
        pass


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['current'])
def current_message(message):
    budget = load_budget()
    current = []
    for key in budget.keys():
        string = key + ' {}\n'.format(budget[key])
        current.append(string)
    reply = ''.join(current)
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['categories'])
def categories_message(message):
    budget = load_budget()
    categories = []
    for key in budget.keys():
        categories.append(key + '\n')
    reply = ''.join(categories)
    bot.send_message(message.chat.id, reply)


def parse_added_message(message):
    what = message.text.split(' ')
    value = 0
    str = 0
    if len(what) == 2:
        for k in what:
            try:
                value = int(k)
            except:
                str = k.lower()
        return value, str


@bot.message_handler(content_types=['text'])
def added(message):
    counter_to_error = 0
    budget = load_budget()
    try:
        value, str = parse_added_message(message)
    except:
        bot.send_message(message.chat.id, "Неверный формат. Используй, например, 'газ 500'")
        return 0
    for cat in categories:
        if str in cat:
            budget['{}'.format(cat[0])] += value
            print(budget)
            if value > 0:
                bot.send_message(message.chat.id, 'Окей, {} грн --> {}'.format(value, str))
            elif value <= 0:
                bot.send_message(message.chat.id, 'Окей, {} грн <-- {}'.format(value * -1, str))
        else:
            counter_to_error += 1
    if counter_to_error == 8:
        bot.send_message(message.chat.id, "Такой категории не существует. Список доступных категорий /categories")
        return 0
    else:
        save_budget(budget)


@bot.message_handler(commands=['previos'])
def previos(message):
    bot.send_message(message.chat.id, 'Нет данных о предидущем месяце')


bot.polling()
