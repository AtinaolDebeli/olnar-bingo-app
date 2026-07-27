from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if user.id not in users:
        users[user.id] = {
            "username": user.username,
            "balance": 0
        }

    await update.message.reply_text(
        f"🎉 Welcome to Olnar Bingo!\n\n"
        f"Hello {user.first_name}\n"
        f"Your account has been created.\n"
        f"Balance: 0 ETB\n\n"
        f"Use /help to see available commands."
    )

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    balance = users.get(user.id, {}).get("balance", 0)

    await update.message.reply_text(
        f"💰 Wallet Balance\n\n{balance} ETB"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start\n"
        "/wallet\n"
        "/games\n"
        "/join\n"
        "/deposit\n"
        "/withdraw"
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("wallet", wallet))
app.add_handler(CommandHandler("help", help_command))

print("Olnar Bingo Bot started...")

app.run_polling()
