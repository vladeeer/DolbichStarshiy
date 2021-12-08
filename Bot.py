import time

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import Const as keys
import Func as F

print("Bot strarted...")

def log_message(name, text):
    dp.bot.send_message(chat_id=-530324262, text=(name + ": " + text + "\n"))

def start_command(update, context):
    log_message(update.message.from_user.first_name + " " + ("" if update.message.from_user.last_name is None else str(update.message.from_user.last_name)) + " [" + str(update.message.from_user.id) + "]: ", "Joined chat with Abdula")
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
        if ((update.message.from_user.id == int(keys.ADMIN)) and (text[0]=="/")):
            print("admin")
        else:
            resp = F.message_responses(text, update.message.from_user.first_name)
            for i in resp:
                if (i == ""):
                    continue
                dp.bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
                log_message("Bot", i)
                time.sleep(len(i)/7)
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
