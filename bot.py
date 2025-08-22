import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from translator import traduzir_para_espanhol

# Carregar variáveis do .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Comando /start
async def start(update, context):
    await update.message.reply_text("Envia a frase, ruivinha")

# Quando o usuário mandar mensagem
async def traduzir(update, context):
    texto = update.message.text
    traducao = traduzir_para_espanhol(texto)
    await update.message.reply_text(f"🇪🇸: {traducao} ✨")

def main():
    app = Application.builder().token(TOKEN).build()

    # Registrar comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, traduzir))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
