import logging
import time
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, JobQueue

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables to store users and groups
approved_users = set()
banned_users = set()
sudo_users = {1910728581}  # Replace with actual user IDs

# Define the bot's token
TOKEN = '6960093955:AAHyOitxsQynWsDG6h6PsTTSGIIlhQD-Uao'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_photo(photo='https://te.legra.ph/file/727e348dd9fe5fa820aed.jpg',
                                caption="I can protect your group from copyright strikes.",
                                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates", url="https://t.me/GAURAV_BOTS")]]))

def delete_edited_message(update: Update, context: CallbackContext) -> None:
    if update.message:
        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"You edited a message and it has been deleted.")

def auto_delete_media(update: Update, context: CallbackContext) -> None:
    if update.message:
        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

def gban(update: Update, context: CallbackContext) -> None:
    user_id = context.args[0]
    banned_users.add(user_id)
    update.message.reply_text(f"User {user_id} has been globally banned.")

def approve(update: Update, context: CallbackContext) -> None:
    user_id = context.args[0]
    approved_users.add(user_id)
    update.message.reply_text(f"User {user_id} has been approved.")

def unapprove(update: Update, context: CallbackContext) -> None:
    user_id = context.args[0]
    approved_users.discard(user_id)
    update.message.reply_text(f"User {user_id} has been unapproved.")

def broadcast(update: Update, context: CallbackContext) -> None:
    message = " ".join(context.args)
    # Here you would need to implement logic to send messages to all groups
    update.message.reply_text(f"Broadcasting: {message}")

def auto_delete_all_chats(context: CallbackContext) -> None:
    # Logic to delete all chats after 4 hours
    pass

def main() -> None:
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher
    
    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.edited, delete_edited_message))
    dispatcher.add_handler(MessageHandler(Filters.photo | Filters.video | Filters.document, auto_delete_media))
    dispatcher.add_handler(CommandHandler("gban", gban))
    dispatcher.add_handler(CommandHandler("at", approve))
    dispatcher.add_handler(CommandHandler("t", unapprove))
    dispatcher.add_handler(CommandHandler("broad", broadcast))

    # Job queue for auto-deleting all chats
    job_queue = updater.job_queue
    job_queue.run_repeating(auto_delete_all_chats, interval=14400)  # Every 4 hours

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
