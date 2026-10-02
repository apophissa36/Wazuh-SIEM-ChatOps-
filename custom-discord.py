#!/var/ossec/framework/python/bin/python3
import sys
import json
import requests


alert_file = open(sys.argv[1])
alert_json = json.loads(alert_file.read())
alert_file.close()


description = alert_json.get('rule', {}).get('description', 'Alerte non définie')
level = alert_json.get('rule', {}).get('level', 0)
agent = alert_json.get('agent', {}).get('name', 'Agent inconnu')


WEBHOOK_URL = "MON_LIEN_WEBHOOK_DISCORD_ICI"

message_content = f"🚨 **ALERTE CRITIQUE SOC** 🚨\n**Gravité :** {level}\n**Machine cible :** {agent}\n**Détails de l'attaque :** {description}"

payload = {
    "content": message_content,
    "username": "SOC Wazuh Bot"
}


requests.post(WEBHOOK_URL, json=payload)