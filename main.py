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

def validar_e_enviar():
    print(f"--- TESTE 1: Checando status da instância '{INSTANCE}' ---")
    url_status = f"{BASE_URL}/instance/connectionState/{INSTANCE}"
    
    try:
        res_status = requests.get(url_status, headers=HEADERS)
        print("Status HTTP da consulta:", res_status.status_code)
        print("Resposta da consulta:", res_status.text)
        
        # Como verificar o sucesso desta etapa:
        # A resposta precisa conter '"state":"open"' ou '"status":"open"'
    except Exception as e:
        print(f"Erro ao conectar com o servidor: {e}")
        return

    print("\n--- TESTE 2: Enviando mensagem ---")
    url_send = f"{BASE_URL}/message/sendText/{INSTANCE}"
    payload = {
        "number": CHAT_ID,
        "options": {"delay": 1200, "presence": "composing"},
        "textMessage": {
            "text": "🔥 *OFERTA TESTE MERCADO LIVRE*\n\n📌 *Luminária LED Touch*\n✅ *Por: R$ 64.90*\n\n🔗 *Link:* https://mercadolivre.com.br"
        }
    }

    res_send = requests.post(url_send, json=payload, headers=HEADERS)
    print("Status HTTP do Envio:", res_send.status_code)
    print("Resposta do Envio:", res_send.text)

if __name__ == "__main__":
    validar_e_enviar()
