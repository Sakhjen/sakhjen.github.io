from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

async def start(update: Update, context):
    # Создаем кнопку с WebAppInfo
    button = InlineKeyboardButton(text="Открыть", web_app=WebAppInfo(url="https://sakhjen.github.io/"))
    
    # Создаем клавиатуру с кнопкой
    keyboard = InlineKeyboardMarkup([[button]])
    
    # Отправляем сообщение с клавиатурой
    await update.message.reply_text(
        "Нажми, чтобы открыть мини-приложение:",
        reply_markup=keyboard
    )

if __name__ == '__main__':
    application = Application.builder().token('7819333375:AAGWbqTpcmDiHHSOEsVPZdPqWHwizq5Lw9s').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()