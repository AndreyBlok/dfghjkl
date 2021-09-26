import telebot
from telebot import types

bot = telebot.TeleBot('1983898484:AAFEAduhHYKhvNyIrv0jKmMCYigr8zBqqhY')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # приветствие началось
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "дарово чем те подсабить?")
    elif message.text == "Дарова":
        bot.send_message(message.from_user.id, "о прив чем помочь?")
    elif message.text == "привет":
        bot.send_message(message.from_user.id, "здарово го кс")
    elif message.text == "как дела":
        bot.send_message(message.from_user.id, "Было норм пока ты не спросили")
    elif message.text == "Как дела":
        bot.send_message(message.from_user.id, "Было норм пока ты не спросили")
    elif message.text == "Как дела?":
        bot.send_message(message.from_user.id, "Было норм пока ты не спросили")
    # приветствие закончилось
    # начало диалогов
    elif message.text.lower() == "го по пивку":
        bot.send_message(message.from_user.id, "я буду жигуль ")
    elif message.text.lower() == "Расскажи о себе":
        bot.send_message(message.from_user.id, "Меня зовут Gememinebot я нахожусь на постоянной разработке одним "
                                               "великим Человеком")
    # конец диалогов
    # начало основных действий

    elif message.text.lower() == "во что сыграть":

        bot.send_message(message.from_user.id, "не стоит играть в лигу лигенд и Volorant а то ты диградируешь Но "
                                               "зарубись в бесплатный шутер kS:go в нём ты не сможешь делать ничего "
                                               "кроме того как сливат")
    elif message.text.lower() == "А в гта не некак":
        bot.send_message(message.from_user.id, "Ну можно в Fallout 4 не начинай ато затянит и думать надо будет")
    elif message.text.lower() == "А в фар край (кривая локализация,да) ты играл? ":
        bot.send_message(message.from_user.id, "ну в пятёрку можешь сыграть но это будет сложно")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "можешь написать привет")
    else:
        bot.send_message(message.from_user.id, "напиши /help или проверь слово попробуй написать на с большой или "
                                               "малнькой буквы")


bot.polling(none_stop=True, interval=0)
