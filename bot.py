import telebot

token = '2038991391:AAEvyEAIf39s0iz4aoeM_36qh_FKdpGZSbA'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    #if "liuda" in message.text:

    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)