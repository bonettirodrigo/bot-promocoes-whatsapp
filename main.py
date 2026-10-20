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
    
    # Estrutura exata da v1.8 para grupos sem o bloco 'options' que causava o erro 500
    payload = {
        "number": CHAT_ID,
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

    # Caso a sua versão específica da v1.8 exija fallback direto
    if res_send.status_code == 500:
        print("\n--- A tentar fallback para o formato raiz ---")
        url_fallback = f"{BASE_URL}/message/sendText/{INSTANCE}"
        payload_fallback = {
            "number": CHAT_ID,
            "text": "🔥 *OFERTA TESTE MERCADO LIVRE*\n\n📌 *Luminária LED Touch*\n✅ *Por: R$ 64.90*\n\n🔗 *Link:* https://mercadolivre.com.br"
        }
        res_fb = requests.post(url_fallback, json=payload_fallback, headers=HEADERS)
        print("Status HTTP Fallback:", res_fb.status_code)
        print("Resposta Fallback:", res_fb.text)

if __name__ == "__main__":
    enviar_mensagem()
