#!/var/ossec/framework/python/bin/python3
import sys
import json
import requests

# Lecture du fichier d'alerte généré par Wazuh
alert_file = open(sys.argv[1])
alert_json = json.loads(alert_file.read())
alert_file.close()

# Extraction des données clés de l'alerte
description = alert_json.get('rule', {}).get('description', 'Alerte non définie')
level = alert_json.get('rule', {}).get('level', 0)
agent = alert_json.get('agent', {}).get('name', 'Agent inconnu')

# Lien Webhook Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/1543790900583600159/3CucyZpTeuIZqcF0-wepnNzsBajh4OpT2NZ2cFxBNyQBq449gIXaZUmUC3jAoi2GdeoX"

# Formatage du message
message_content = f"🚨 **ALERTE CRITIQUE SOC** 🚨\n**Gravité :** {level}\n**Machine cible :** {agent}\n**Détails de l'attaque :** {description}"

payload = {
    "content": message_content,
    "username": "SOC Wazuh Bot"
}

# Envoi de la requête vers le salon Discord
requests.post(WEBHOOK_URL, json=payload) 