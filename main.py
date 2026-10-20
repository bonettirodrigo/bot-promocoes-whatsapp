import os
import requests
import time

BASE_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com").strip().rstrip("/")
API_KEY = os.getenv("AUTHENTICATION_API_KEY", "").strip()
INSTANCE = "bot_promocoes"
GROUP_JID = "120363430235680804@g.us"

HEADERS = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

def enviar_promocao():
    # PASSO 1: Manter a sincronização do grupo na memória que retornou 200
    print(f"--- PASSO 1: Sincronizando grupo {GROUP_JID} ---")
    url_sync = f"{BASE_URL}/group/findGroupInfos/{INSTANCE}?groupJid={GROUP_JID}"
    try:
        res_sync = requests.get(url_sync, headers=HEADERS)
        print("Status da sincronização:", res_sync.status_code)
    except Exception as e:
        print(f"Aviso na sincronização: {e}")

    time.sleep(1)

    # PASSO 2: Envio com a estrutura plana aceita para JIDs de grupo
    print("\n--- PASSO 2: Disparando mensagem ---")
    url_send = f"{BASE_URL}/message/sendText/{INSTANCE}"
    
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
            "presence": "composing",
            "linkPreview": False
        }
    }

    res_send = requests.post(url_send, json=payload, headers=HEADERS)
    print("Status HTTP do Envio:", res_send.status_code)
    print("Resposta do Envio:", res_send.text)

if __name__ == "__main__":
    enviar_promocao()
