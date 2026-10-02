# 🛡️ Projet Mini-SIEM Wazuh : ChatOps & Active Response

Ce dépôt documente la mise en place d'un système de détection et de réponse aux incidents (SIEM) basé sur Wazuh dans le cadre de mon projet de stage.

## 🎯 Objectifs du projet
- Déploiement d'un serveur Wazuh (v4.8.0) pour la surveillance des endpoints.
- **ChatOps :** Création d'un script d'intégration Python pour remonter les alertes critiques de sécurité en temps réel vers une plateforme de messagerie (Discord).
- **Active Response :** Configuration de règles de blocage automatique (`firewall-drop`) pour isoler les adresses IP attaquantes de manière autonome suite à la détection d'une menace.

## 📂 Contenu du dépôt
* `ossec.conf` : Configuration du gestionnaire Wazuh activant l'intégration personnalisée et les modules de réponse active.
* `custom-discord.py` : Script Python exploitant l'API Wazuh et les Webhooks pour formater et envoyer les alertes JSON vers Discord.
* `local_rules.xml` : Règles de détection personnalisées.

*Projet réalisé dans un environnement virtualisé fermé (VirtualBox).*