
import os
import requests

BASE_URL = os.getenv(
    "EVOLUTION_URL",
    "https://evolution-api-0ptv.onrender.com"
).strip().rstrip("/")

API_KEY = os.getenv("AUTHENTICATION_API_KEY", "").strip()
INSTANCE = "bot_promocoes"

# Coloque seu número de WhatsApp no formato internacional
# Exemplo fictício: 5511999999999
DESTINO = "55DD9NUMERO"

url = f"{BASE_URL}/message/sendText/{INSTANCE}"

payload = {
    "number": DESTINO,
    "text": "Teste técnico da Evolution API"
}

headers = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(
    url,
    json=payload,
    headers=headers,
    timeout=30
)

print("Status HTTP:", response.status_code)
print("Resposta:", response.text)
