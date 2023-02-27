import telebot

from bot import checkQuestion
#bot = telebot.TeleBot("5912626227:AAFZK5IDJ3gqeTsj6p4LdAMpYA5F6JNtCr8")





"""



@bot.message_handler()
def get_user_text(message):
    if message.text.lower() == "bye":
        bot.send_message(message.chat.id, "bye")
        bot.stop_polling()
    else:
        answer = checkQuestion.check(message.text)  # метод передающий ответ в checkQuestion
        bot.send_message(message.chat.id, answer)

    bot.infinity_polling()

"""
