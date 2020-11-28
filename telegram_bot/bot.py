import telebot


bot = telebot.TeleBot("1346023285:AAE1T7QZEwrBR1J8F1Fm8vZapjJsPzq2Wwc") # bot token


@bot.message_handler(commands=["start"])
def welc(message):
	user_id = message.from_user.id

	bot.send_message(user_id, f"Salom men {bot.get_me().first_name} man")


@bot.message_handler(content_types=["text"])
def echo(message):
	user_id = message.from_user.id
	
	bot.send_message(user_id, message.text)


if __name__ == '__main__':
	bot.polling(none_stop=True)