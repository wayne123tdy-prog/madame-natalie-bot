import telebot
from telebot import types

TOKEN = '8124000308:AAG1xDqEO1N093tc_0OfRelaUl-cnK0-aY0'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Цены 💰")
    btn2 = types.KeyboardButton("Адрес 📍")
    btn3 = types.KeyboardButton("Уход 🧴")
    btn4 = types.KeyboardButton("Записаться 📅")
    btn5 = types.KeyboardButton("Доп. информация ℹ️") 
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я бот-помощник студии кератина. Выбери нужный раздел ниже 👇", reply_markup=markup)

@bot.message_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    # 1. НАЖАЛИ НА КНОПКУ "ЦЕНЫ" -> Показываем выбор процедур
    if message.text == "Цены 💰":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_keratin = types.KeyboardButton("Кератин ✨")
        btn_botox = types.KeyboardButton("Ботокс 💧")
        btn_repair = types.KeyboardButton("Восстановление 🌿")
        btn_back = types.KeyboardButton("⬅️ Назад в меню")
        
        markup.add(btn_keratin, btn_botox)
        markup.add(btn_repair, btn_back)
        
        bot.send_message(message.chat.id, "Какая процедура вас интересует? 🤔", reply_markup=markup)

    # ================= КЕРАТИН =================
    elif message.text == "Кератин ✨":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Кератин 40-45 см"), types.KeyboardButton("Кератин 50-55 см"))
        markup.add(types.KeyboardButton("Кератин 60-65 см"), types.KeyboardButton("Кератин 70-75 см"))
        markup.add(types.KeyboardButton("Кератин 80-85 см"), types.KeyboardButton("⬅️ Назад в меню"))
        bot.send_message(message.chat.id, "Выбери длину волос для Кератина:", reply_markup=markup)

    # Цены на Кератин (твои старые цены)
    elif message.text == "Кератин 40-45 см":
        bot.send_message(message.chat.id, "💰 Стоимость Кератина (40-45 см): **2500 грн**")
    elif message.text == "Кератин 50-55 см":
        bot.send_message(message.chat.id, "💰 Стоимость Кератина (50-55 см): **3000 грн**")
    elif message.text == "Кератин 60-65 см":
        bot.send_message(message.chat.id, "💰 Стоимость Кератина (60-65 см): **3500 грн**")
    elif message.text == "Кератин 70-75 см":
        bot.send_message(message.chat.id, "💰 Стоимость Кератина (70-75 см): **4000 грн**")
    elif message.text == "Кератин 80-85 см":
        bot.send_message(message.chat.id, "💰 Стоимость Кератина (80-85 см): **4500 грн**")

    # ================= БОТОКС =================
    elif message.text == "Ботокс 💧":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Ботокс 40-45 см"), types.KeyboardButton("Ботокс 50-55 см"))
        markup.add(types.KeyboardButton("Ботокс 60-65 см"), types.KeyboardButton("Ботокс 70-75 см"))
        markup.add(types.KeyboardButton("Ботокс 80-85 см"), types.KeyboardButton("⬅️ Назад в меню"))
        bot.send_message(message.chat.id, "Выбери длину волос для Ботокса:", reply_markup=markup)

    # Цены на Ботокс (я поставил примерные, поменяй как скажет мама!)
    elif message.text == "Ботокс 40-45 см":
        bot.send_message(message.chat.id, "💰 Стоимость Ботокса (40-45 см): **2000 грн**")
    elif message.text == "Ботокс 50-55 см":
        bot.send_message(message.chat.id, "💰 Стоимость Ботокса (50-55 см): **2400 грн**")
    elif message.text == "Ботокс 60-65 см":
        bot.send_message(message.chat.id, "💰 Стоимость Ботокса (60-65 см): **2800 грн**")
    elif message.text == "Ботокс 70-75 см":
        bot.send_message(message.chat.id, "💰 Стоимость Ботокса (70-75 см): **3200 грн**")
    elif message.text == "Ботокс 80-85 см":
        bot.send_message(message.chat.id, "💰 Стоимость Ботокса (80-85 см): **3600 грн**")

    # ================= ВОССТАНОВЛЕНИЕ =================
    elif message.text == "Восстановление 🌿":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Восстановление 40-45 см"), types.KeyboardButton("Восстановление 50-55 см"))
        markup.add(types.KeyboardButton("Восстановление 60-65 см"), types.KeyboardButton("Восстановление 70-75 см"))
        markup.add(types.KeyboardButton("Восстановление 80-85 см"), types.KeyboardButton("⬅️ Назад в меню"))
        bot.send_message(message.chat.id, "Выбери длину волос для Восстановления:", reply_markup=markup)

    # Цены на Восстановление (тоже примерные, измени под себя)
    elif message.text == "Восстановление 40-45 см":
        bot.send_message(message.chat.id, "💰 Стоимость Восстановления (40-45 см): **600 грн**")
    elif message.text == "Восстановление 50-55 см":
        bot.send_message(message.chat.id, "💰 Стоимость Восстановления (50-55 см): **900 грн**")
    elif message.text == "Восстановление 60-65 см":
        bot.send_message(message.chat.id, "💰 Стоимость Восстановления (60-65 см): **1200 грн**")
    elif message.text == "Восстановление 70-75 см":
        bot.send_message(message.chat.id, "💰 Стоимость Восстановления (70-75 см): **1500 грн**")
    elif message.text == "Восстановление 80-85 см":
        bot.send_message(message.chat.id, "💰 Стоимость Восстановления (80-85 см): **1800 грн**")

    # ================= ОСТАЛЬНЫЕ КНОПКИ ГЛАВНОГО МЕНЮ =================
    elif message.text == "⬅️ Назад в меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Цены 💰")
        btn2 = types.KeyboardButton("Адрес 📍")
        btn3 = types.KeyboardButton("Уход 🧴")
        btn4 = types.KeyboardButton("Записаться 📅")
        btn5 = types.KeyboardButton("Доп. информация ℹ️")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню 👇", reply_markup=markup)

    elif message.text == "Адрес 📍":
        bot.send_message(message.chat.id, "📍 Студия Кератина, ул. Пашутинская, 57А  🏢  Красота ваших волос начинается здесь! 💫.")
        
    elif message.text == "Уход 🧴":
        bot.send_message(message.chat.id, "Памятка: Не мыть голову первые 24 часа, использовать только безсульфатный шампунь!")
        
    elif message.text == "Записаться 📅":
        bot.send_message(message.chat.id, "Чтобы записаться, напиши мне в личку.")
        
    elif message.text == "Доп. информация ℹ️":
        info_text = (
            "ℹ️ **Дополнительная информация:**\n\n"
            "1. Если вы не знаете, какая процедура вам больше подойдет, "
            "вы можете прийти ко мне на **бесплатную диагностику**! "
            "Я посмотрю на состояние волос и подберу идеальный уход. ✨"
        )
        bot.send_message(message.chat.id, info_text, parse_mode="Markdown")

print("Бот успешно запущен на компьютере!")
bot.infinity_polling()
