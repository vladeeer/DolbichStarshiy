import time

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import Const as keys
import Func as F

print("Bot strarted...")

def typing(update, n):
    for i in range(0, int(2*n)):
        dp.bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
        time.sleep(0.5)

def log_message(name, text):
    for log_chat in keys.LOG_CHATS:
        dp.bot.send_message(chat_id=log_chat, text=(name + ": " + text + "\n"))

def start_command(update, context):
    log_message(update.message.from_user.first_name + " " + ("" if update.message.from_user.last_name is None else str(update.message.from_user.last_name)) + " [" + str(update.message.from_user.id) + "]: ", "Joined chat with Abdula")
    if (("лег" in update.message.from_user.first_name) or ("лад" in update.message.from_user.first_name)):
        log_message("Bot", "С нг крч")      
        time.sleep(6)
        typing(update, 4)
        update.message.reply_text("Э ну привет")
        time.sleep(2)
        typing(update, 1)
        time.sleep(7)
        typing(update, 20)
        update.message.reply_text("Вопщим сидел я аднажды в талете и думал о сваиом будущим но какда настала время вытерать нис я пасматрел на абрывак сральнай ленты у миня в руке")
        time.sleep(2)
        typing(update, 10)
        update.message.reply_text("Я понял што этат абрывак был неабычный он был асобеный")
        time.sleep(3)
        typing(update, 1)
        time.sleep(10)
        typing(update, 10)
        update.message.reply_text("Я вдрук пачуствавал што имена этат абрывак должын стать падаркам тибе на новий год")
        time.sleep(2)
        typing(update, 12)
        update.message.reply_text("На абрыфке я написал сваио имя и атправил ево к тибе")
        time.sleep(5)
        typing(update, 25)
        update.message.reply_text("И вот типерь када ты написал мине я хачу пасдравит тибя с самым пркирасным празником в гаду новым годам!!")
        time.sleep(3)
        typing(update, 9)
        update.message.reply_text("Пуст новый гот станит лутше чем паследний")
        time.sleep(1)
        typing(update, 4)
        update.message.reply_text("Щасливее висилее ярчи")
        time.sleep(2)
        typing(update, 13)
        update.message.reply_text("Здаровия тибе дастатка улыбак удачи и самих лутшых дыней!")
        time.sleep(1)
        typing(update, 5)
        update.message.reply_text("С новым годам!!!")
    else:
        log_message("Bot", "Ээйа")
        update.message.reply_text("Ээйа")

def help_command(update, context):
    log_message(update.message.from_user.first_name, "/help")
    log_message("Bot", "Абаедежся")
    update.message.reply_text("Абаедежся")

def handle_message(update, context):
    if (update.message != None):
        text=str(update.message.text).lower()
        log_message(update.message.from_user.first_name, update.message.text)
        if ((update.message.from_user.id in keys.ADMINS) and (text[0]=="/")):
            print("Admin: " + text)
            log_message("[Admin]",text)
        else:
            resp = F.message_responses(text, update.message.from_user.first_name)
            for i in resp:
                if (i == ""):
                    continue
                typing(update, float(len(i))/7.0)
                log_message("Bot", i)
                update.message.reply_text(i)
    
    elif (update.edited_message != None):
        resp = F.message_edited()
        for i in resp:
            if (i == ""):
                    continue
            dp.bot.send_chat_action(chat_id=update.edited_message.chat_id, action="typing")
            log_message("Bot", i)
            time.sleep(len(i)/7)
            update.edited_message.reply_text(i)

def error(update, context):
    error_text = f"Update {update} causes error {context.error}"
    print(error_text)
    log_message("[Server]", error_text)

def main():
    updater = Updater(keys.KEY, use_context=True)
    global dp 
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
