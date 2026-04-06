import telebot
import time

TOKEN = "8776199110:AAHdH5Iw46ipMYpApA3Hz5RW4yfourne3as"
bot = telebot.TeleBot(TOKEN)

# Responde no grupo
@bot.message_handler(func=lambda m: True)
def responder(message):
    msg = message.text.lower()
    
    if msg == 'menu' or msg == 'catálogo' or msg == 'preços':
        bot.reply_to(message, """📚 CATÁLOGO MÉTODOS BLACK:
1. Curso Black VIP - R$47
2. Pack Exclusivo - R$19,90
3. Combo (Curso + Pack) - R$59,90

Qual você quer? Diga "quero o curso" ou "quero o pack".""")
    
    elif 'quero o curso' in msg:
        bot.reply_to(message, "🔥 Curso Black VIP - R$47\nMe chama no privado que te passo o PIX: @digitalpay_ravi_bot")
    
    elif 'quero o pack' in msg:
        bot.reply_to(message, "📦 Pack Exclusivo - R$19,90\nMe chama no privado que te passo o PIX: @digitalpay_ravi_bot")
    
    elif 'combo' in msg or 'quero os dois' in msg:
        bot.reply_to(message, "🚀 Combo Completo - R$59,90\nMe chama no privado que te passo o PIX: @digitalpay_ravi_bot")
    
    elif msg == 'oi' or msg == 'olá' or msg == 'opa':
        bot.reply_to(message, "Fala, arrombado! 👊\nManda 'menu' pra ver o catálogo.")
    
    elif 'obrigado' in msg or 'valeu' in msg:
        bot.reply_to(message, "Disponha, caralho! 🚀")

print("✅ BOT RODANDO...")
bot.infinity_polling()