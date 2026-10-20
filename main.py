import os
import requests

BASE_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com").strip().rstrip("/")
API_KEY = os.getenv("AUTHENTICATION_API_KEY", "").strip()
INSTANCE = "bot_promocoes"

# Cole aqui o seu número de telemóvel no formato internacional (apenas dígitos)
NUMERO_PESSOAL = "554598542955"  

HEADERS = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

def testar_envio_pessoal():
    url_send = f"{BASE_URL}/message/sendText/{INSTANCE}"
    
    payload = {
        "number": NUMERO_PESSOAL,
        "options": {
            "delay": 1200,
            "presence": "composing",
            "linkPreview": False
        },
        "textMessage": {
            "text": "🧪 *TESTE DE ENVIO INDIVIDUAL*\n\nSe recebeu esta mensagem, a API e a sessão do WhatsApp estão 100% ativas!"
        }
    }

    print(f"Enviando teste individual para: {NUMERO_PESSOAL}")
    res_send = requests.post(url_send, json=payload, headers=HEADERS)
    print("Status HTTP do Envio:", res_send.status_code)
    print("Resposta do Envio:", res_send.text)

if __name__ == "__main__":
    testar_envio_pessoal()
