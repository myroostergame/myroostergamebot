from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Start komutu için işleyici
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Open", web_app={"url": "https://musical-fenglisu-dbf730.netlify.app/"}),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🐔 Build your egg farm now!",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    BOT_TOKEN = "7641663892:AAFKMX2K9AQ0nPOJH-_b5v9azAE7KZ88tRc"

    # Bot uygulamasını oluştur
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Komut işleyicileri ekle
    app.add_handler(CommandHandler("start", start))

    # Botu başlat
    print("bot active...")
    app.run_polling()
