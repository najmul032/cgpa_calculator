
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

TOKEN = "8630576455:AAHPiPb4gAz9ay0I3aDKiFsXizG2PcgwcqA"

CREDITS_GRADES = 1  # Conversation state

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "CGPA Calculator Bot\n\n"
        "Type /cgpa to calculate your CGPA."
    )

async def cgpa_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Please enter your credits and grades separated by spaces.\n"
        "Example: 3 3.75 4 3.50 3 4.00"
    )
    return CREDITS_GRADES

async def calculate_cgpa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.text.strip().split()

    if len(data) % 2 != 0:
        await update.message.reply_text("Please provide credit and grade in pairs!")
        return CREDITS_GRADES

    try:
        total_points = 0
        total_credit = 0
        for i in range(0, len(data), 2):
            credit = float(data[i])
            grade = float(data[i+1])
            total_points += credit * grade
            total_credit += credit

        if total_credit == 0:
            await update.message.reply_text("Total credit cannot be zero.")
            return CREDITS_GRADES

        cgpa = total_points / total_credit
        await update.message.reply_text(f"Your CGPA = {round(cgpa, 2)}")
        return ConversationHandler.END

    except ValueError:
        await update.message.reply_text("Invalid input! Please enter numbers like: 3 3.75 4 3.50")
        return CREDITS_GRADES

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CGPA calculation cancelled.")
    return ConversationHandler.END

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("cgpa", cgpa_command)],
        states={
            CREDITS_GRADES: [MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_cgpa)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)

    print("Bot is running...")
    app.run_polling()