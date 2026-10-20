import os
import requests

BASE_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com").strip().rstrip("/")
API_KEY = os.getenv("AUTHENTICATION_API_KEY", "").strip()
INSTANCE = "bot_promocoes"
CHAT_ID = "120363430235680804@g.us"

HEADERS = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

def enviar_mensagem():
    url_send = f"{BASE_URL}/message/sendText/{INSTANCE}"
    
    # Payload no formato nativo completo para aceitar grupos (@g.us)
    payload = {
        "number": CHAT_ID,
        "options": {
            "delay": 1200,
            "presence": "composing",
            "linkPreview": False
        },
        "textMessage": {
            "text": (
                "🔥 *OFERTA TESTE MERCADO LIVRE*\n\n"
                "📌 *Luminária LED Touch*\n"
                "✅ *Por: R$ 64.90*\n\n"
                "🔗 *Link:* https://mercadolivre.com.br"
            )
        }
    }

    print(f"Disparando mensagem para: {url_send}")
    res_send = requests.post(url_send, json=payload, headers=HEADERS)
    print("Status HTTP do Envio:", res_send.status_code)
    print("Resposta do Envio:", res_send.text)

if __name__ == "__main__":
    enviar_mensagem()
