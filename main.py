import telebot
import time
import threading
import os

# Твой токен
TOKEN = "8668177114:AAFll1Z4NJdccQcBpQoFePCRDSkqGv-L0i4"
bot = telebot.TeleBot(TOKEN)

def delete_later(chat_id, message_id, delay):
    time.sleep(delay)
    try:
        bot.delete_message(chat_id, message_id)
    except:
        pass

@bot.message_handler(commands=['all', 'start'])
def summon(message):
    user_text = message.text.replace('/all', '').replace('/start', '').strip()
    if not user_text:
        user_text = "✨ Дивы, внимание! Общий сбор! ✨"

    try:
        sent_msg = bot.send_message(message.chat.id, user_text)
        bot.pin_chat_message(message.chat.id, sent_msg.message_id, disable_notification=False)
        
        status_msg = bot.send_message(message.chat.id, "📢 Оповещение разослано! (Удалюсь через 15 сек)")

        # Таймеры на удаление
        threading.Thread(target=delete_later, args=(message.chat.id, sent_msg.message_id, 15)).start()
        threading.Thread(target=delete_later, args=(message.chat.id, status_msg.message_id, 15)).start()
        threading.Thread(target=delete_later, args=(message.chat.id, message.message_id, 15)).start()
    except:
        pass

if __name__ == "__main__":
    print("✅ Бот запущен автономно!")
    bot.infinity_polling()
  
