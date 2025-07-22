import logging
import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

def send_daily_message(context):
    message = (
        "🚨 *CDS Daily Current Affairs Update* 🚨\n\n"
        "📰 Latest from @d71academy_current_affairs (Instagram)\n\n"
        "🔗 https://www.instagram.com/d71academy_current_affairs/\n\n"
        "🪖 Stay sharp. Jai Hind!"
    )
    context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=message,
        parse_mode='Markdown'
    )

def start(update, context):
    update.message.reply_text("✅ Bot is active. CDS Intel delivery running!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    scheduler = BackgroundScheduler()
    scheduler.add_job(send_daily_message, 'cron', hour=6, minute=0, args=[updater.job_queue])
    scheduler.start()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
