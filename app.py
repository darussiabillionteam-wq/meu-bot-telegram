import os
import threading
import telebot
from flask import Flask

# ========== CONFIGURAÇÕES ==========
TOKEN = "8776199110:AAHdH5Iw46ipMYpApA3Hz5RW4yfourne3as"
bot = telebot.TeleBot(TOKEN)

# ========== COMANDOS DO BOT ==========
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Fala, arrombado! 👊\nManda 'menu' pra ver o catálogo.")

@bot.message_handler(func=lambda m: m.text.lower() == 'menu')
def menu(message):
    bot.reply_to(message, """📚 CATÁLOGO MÉTODOS BLACK:
1. Curso Black VIP - R$47
2. Pack Exclusivo - R$19,90
3. Combo - R$59,90

Qual você quer?""")

@bot.message_handler(func=lambda m: 'quero o curso' in m.text.lower())
def curso(message):
    bot.reply_to(message, "🔥 Curso Black VIP - R$47\nMe chama no privado: @digitalpay_ravi_bot")

@bot.message_handler(func=lambda m: 'quero o pack' in m.text.lower())
def pack(message):
    bot.reply_to(message, "📦 Pack Exclusivo - R$19,90\nMe chama no privado: @digitalpay_ravi_bot")

# ========== SERVIDOR WEB FALSO (PRO RENDER) ==========
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/health')
def health():
    return "OK", 200

def run_bot():
    """Roda o bot em thread separada"""
    print("✅ BOT RODANDO...")
    bot.infinity_polling()

if __name__ == "__main__":
    # Inicia o bot em background
    thread = threading.Thread(target=run_bot)
    thread.start()
    
    # Roda o servidor web (necessário pro Render)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)