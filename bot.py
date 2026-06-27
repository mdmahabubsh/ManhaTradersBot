import os
from openai import OpenAI
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌿 মানহা ট্রেডার্সে স্বাগতম!\n\n"
        "✅ খাঁটি সরিষার তেল\n"
        "✅ উন্নত মানের চাল\n\n"
        "📦 পণ্য দেখতে /products লিখুন\n"
        "📞 যোগাযোগ করতে /contact লিখুন"
    )


# /products
async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 আমাদের পণ্যসমূহ:\n\n"
        "🌿 খাঁটি সরিষার তেল\n"
        "💰 ১ লিটার - ৩৬০ টাকা\n"
        "💰 ২ লিটার - ৭২০ টাকা\n\n"
        "🍚 মিনিকেট চাল\n"
        "💰 ৫০ কেজি - ৩৭১০ টাকা\n\n"
        "🍚 কাটারি চাল\n"
        "💰 ৫০ কেজি - ৩৩৫০ টাকা"
    )


# /contact
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 যোগাযোগ:\n\n"
        "🏪 মানহা ট্রেডার্স\n"
        "📱 01908274008\n"
        "📧 mahabubmd96@gmail.com"
    )


# সাধারণ চ্যাট
# সাধারণ চ্যাট
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "তুমি মানহা ট্রেডার্সের একজন কাস্টমার সাপোর্ট প্রতিনিধি। "
                        "তুমি বাংলা ভাষায় উত্তর দেবে। "
                        "মানহা ট্রেডার্স চাল, সরিষার তেল ও খাদ্যপণ্য বিক্রি করে।"
                    ),
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
        )

        await update.message.reply_text(
            response.choices[0].message.content
        )

    except Exception as e:
        await update.message.reply_text(
            f"❌ Error: {str(e)}"
        )


# Main
def main():
    app = Application.builder().token(
        TELEGRAM_BOT_TOKEN
    ).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("products", products))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            chat
        )
    )

    print("✅ Manha Traders Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
