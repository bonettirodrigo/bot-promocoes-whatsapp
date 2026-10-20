import os
import requests

BASE_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com").strip().rstrip("/")
API_KEY = os.getenv("AUTHENTICATION_API_KEY", "").strip()
INSTANCE = "bot_promocoes"
GROUP_JID = "120363430235680804@g.us"

HEADERS = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

def enviar_promocao_grupo():
    url_send = f"{BASE_URL}/message/sendText/{INSTANCE}"
    
    # Payload validado para envio direto em grupos na Evolution API v1.8
    payload = {
        "number": GROUP_JID,
        "text": (
            "🔥 *OFERTA IMPERDÍVEL MERCADO LIVRE*\n\n"
            "📌 *Luminária LED Touch Sem Fio*\n"
            "✅ *Por apenas: R$ 64,90*\n\n"
            "🔗 *Garanta a sua aqui:* https://mercadolivre.com.br\n\n"
            "⚡ *Aproveite antes que acabe o estoque!*"
        ),
        "options": {
            "delay": 1200,
            "presence": "composing"
        }
    }

    print(f"Enviando mensagem para o grupo: {GROUP_JID}")
    res_send = requests.post(url_send, json=payload, headers=HEADERS)
    print("Status HTTP do Envio:", res_send.status_code)
    print("Resposta do Envio:", res_send.text)

if __name__ == "__main__":
    enviar_promocao_grupo()
