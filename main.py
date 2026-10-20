
import os
import requests

BASE_URL = os.getenv(
    "EVOLUTION_URL",
    "https://evolution-api-0ptv.onrender.com"
).strip().rstrip("/")

API_KEY = os.getenv("AUTHENTICATION_API_KEY", "").strip()
INSTANCE = "bot_promocoes"
CHAT_ID = "120363430235680804@g.us"

HEADERS = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

def enviar_mensagem():
    if not API_KEY:
        print("ERRO: a variável AUTHENTICATION_API_KEY está vazia.")
        return

    url = f"{BASE_URL}/message/sendText/{INSTANCE}"

    payload = {
        "number": CHAT_ID,
        "textMessage": {
            "text": (
                "🔥 *OFERTA TESTE MERCADO LIVRE*\n\n"
                "📌 *Luminária LED Touch*\n"
                "✅ *Por: R$ 64,90*\n\n"
                "🔗 *Link:* https://mercadolivre.com.br"
            )
        },
        "options": {
            "delay": 1200,
            "presence": "composing"
        }
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=HEADERS,
            timeout=30
        )

        print("Status HTTP:", response.status_code)
        print("Resposta:", response.text)

    except requests.RequestException as erro:
        print("Erro na requisição:", erro)

if __name__ == "__main__":
    enviar_mensagem()
