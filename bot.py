
import os
from openai import OpenAI
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# আপনার API Key এখানে দিন
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
client = OpenAI(api_key=OPENAI_API_KEY)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌿 মানহা ট্রেডার্সে স্বাগতম!\n\n"
        "✅ খাঁটি সরিষার তেল\n"
        "✅ উন্নত মানের চাল\n\n"
        "📦 পণ্য দেখতে /products লিখুন"
    )

# /products
async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 আমাদের পণ্যসমূহ:\n\n"
        "🌿 খাঁটি সরিষার তেল\n"
        "💰 ১ লিটার - ৩৬০ টাকা\n"
        "💰 ২ লিটার - ৭২০ টাকা\n\n"
        "🌾 মিনিকেট চাল\n"
        "🌾 নাজিরশাইল চাল\n"
        "🌾 আতপ চাল\n\n"
        "🛒 অর্ডার করতে /contact লিখুন"
    )

# /contact
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 যোগাযোগ:\n"
        "মোবাইল: 01752157086\n"
        "🌐 https://manhatreaders.zatiqeasy.com"
    )

# AI উত্তর
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
তুমি Manha Traders-এর AI Assistant।
তুমি মানুষের মতো বাংলায় উত্তর দিবে।
দোকানের পণ্য:
- খাঁটি সরিষার তেল
- মিনিকেট চাল
- নাজিরশাইল চাল
- আতপ চাল
ফোন: 01752157086
ওয়েবসাইট: https://manhatreaders.zatiqeasy.com
"""
            },
            {"role": "user", "content": user_message}
        ]
    )

    await update.message.reply_text(
        response.choices[0].message.content
    )

# Bot চালু
app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("products", products))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot started...")
app.run_polling()
