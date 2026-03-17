from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
import os

TOKEN = os.environ['TOKEN']

CREDITS_GRADES = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "CGPA Calculator Bot\n\n"
        "Type /cgpa to calculate your CGPA."
    )

async def cgpa_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Please enter your grades separated by spaces.\n"
        "Example (Only Grades): 3.50 4.00 3.75\n"
        "Example (Credit & Grade): 3 3.50 4 4.00"
    )
    return CREDITS_GRADES

async def calculate_cgpa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.text.strip().split()
    try:
        total_points = 0
        total_credit = 0
        if len(data) % 2 == 0:
            for i in range(0, len(data), 2):
                credit = float(data[i])
                grade = float(data[i+1])
                total_points += credit * grade
                total_credit += credit
        else:
            for val in data:
                grade = float(val)
                total_points += 3.0 * grade
                total_credit += 3.0
        if total_credit == 0:
            await update.message.reply_text("Input cannot be zero.")
            return CREDITS_GRADES
        cgpa = total_points / total_credit
        await update.message.reply_text(f"Your CGPA = {round(cgpa, 2)}\n\nTo calculate again, type /cgpa")
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("Invalid input! Please enter numbers only.")
        return CREDITS_GRADES

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CGPA calculation cancelled.")
    return ConversationHandler.END

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("cgpa", cgpa_command)],
        states={CREDITS_GRADES: [MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_cgpa)]},
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.run_polling()
