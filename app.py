import os
import telebot
from flask import Flask, request

TOKEN = "8776199110:AAHdH5Iw46ipMYpApA3Hz5RW4yfourne3as"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
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
bot.remove_webhook()
bot.set_webhook(url="https://meu-bot-telegram-ip1g.onrender.com/webhook")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)