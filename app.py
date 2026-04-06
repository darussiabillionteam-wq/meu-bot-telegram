import os
import telebot
from flask import Flask, request

TOKEN = "8776199110:AAHdH5Iw46ipMYpApA3Hz5RW4yfourne3as"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Health check para o Render
@app.route('/', methods=['GET'])
def home():
    return "Bot is running!", 200

# Health check específico para o UptimeRobot
@app.route('/health', methods=['GET'])
def health():
    return "OK", 200

# Webhook endpoint (aceita GET e POST)
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "Webhook endpoint. Use POST for updates.", 200
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK', 200

# Comandos
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

# Remove webhook antigo e seta o novo
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://meu-bot-telegram-ip1g.onrender.com/webhook")
    print("✅ Webhook configurado com sucesso!")
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)