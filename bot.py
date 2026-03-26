from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
import os

TOKEN = os.environ['TOKEN']

ONLY_GRADES = 1
CREDITS_GRADES = 2

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 CGPA Calculator Bot\n\n"
        "Use:\n"
        "/cgpa → Only grades\n"
        "/cgpa_credit → Credit + Grade"
    )

# Only grades
async def cgpa_only(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Enter grades only:\nExample: 3.50 4.00 3.75"
    )
    return ONLY_GRADES

# Credit + grade
async def cgpa_credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Enter credit & grade:\nExample: 3 3.50 4 4.00"
    )
    return CREDITS_GRADES

# Only grades calculation
async def calculate_only(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.text.strip().split()
    try:
        grades = [float(x) for x in data]

        if len(grades) == 0:
            await update.message.reply_text("No input given!")
            return ONLY_GRADES

        cgpa = sum(grades) / len(grades)

        await update.message.reply_text(
            f"✅ Your CGPA = {round(cgpa, 2)}\n\nType /cgpa to calculate again"
        )
        return ConversationHandler.END

    except ValueError:
        await update.message.reply_text("❌ Invalid input!")
        return ONLY_GRADES

# Credit + grade calculation
async def calculate_credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.text.strip().split()
    try:
        if len(data) % 2 != 0:
            await update.message.reply_text("❌ Enter pairs of credit & grade!")
            return CREDITS_GRADES

        total_points = 0
        total_credit = 0

        for i in range(0, len(data), 2):
            credit = float(data[i])
            grade = float(data[i+1])

            total_points += credit * grade
            total_credit += credit

        if total_credit == 0:
            await update.message.reply_text("Credit cannot be zero!")
            return CREDITS_GRADES

        cgpa = total_points / total_credit

        await update.message.reply_text(
            f"✅ Your CGPA = {round(cgpa, 2)}\n\nType /cgpa_credit to calculate again"
        )
        return ConversationHandler.END

    except ValueError:
        await update.message.reply_text("❌ Invalid input!")
        return CREDITS_GRADES

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Cancelled.")
    return ConversationHandler.END


if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("cgpa", cgpa_only),
            CommandHandler("cgpa_credit", cgpa_credit)
        ],
        states={
            ONLY_GRADES: [MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_only)],
            CREDITS_GRADES: [MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_credit)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)

    app.run_polling()
