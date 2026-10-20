import os
import requests

# Limpa o URL para garantir que não tem barras extras no final
BASE_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com").strip().rstrip("/")
API_KEY = os.getenv("AUTHENTICATION_API_KEY", "123456").strip()
INSTANCE = "bot_promocoes"
CHAT_ID = "120363430235680804@g.us"

def enviar_mensagem_teste():
    url = f"{BASE_URL}/message/sendText/{INSTANCE}"
    
    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "number": CHAT_ID,
        "options": {
            "delay": 1200,
            "presence": "composing"
        },
        "textMessage": {
            "text": "🔥 *OFERTA TESTE MERCADO LIVRE*\n\n📌 *Luminária LED Articulada Touch*\n✅ *Por: R$ 64.90*\n\n🔗 *Garanta aqui:* https://mercadolivre.com.br"
        }
    }
    
    print(f"A enviar requisição para: {url}")
    response = requests.post(url, json=payload, headers=headers)
    
    print("Código HTTP:", response.status_code)
    print("Resposta completa da API:", response.text)

if __name__ == "__main__":
    enviar_mensagem_teste()
