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
    # PASSO 1: Forçar a API a carregar os dados do grupo na memória do Baileys
    print(f"--- PASSO 1: Sincronizando metadados do grupo {GROUP_JID} ---")
    url_find_group = f"{BASE_URL}/group/findGroupInfos/{INSTANCE}?groupJid={GROUP_JID}"
    
    try:
        res_sync = requests.get(url_find_group, headers=HEADERS)
        print("Status da sincronização:", res_sync.status_code)
    except Exception as e:
        print(f"Aviso na sincronização: {e}")

    # Aguarda 2 segundos para o soquete atualizar a sessão do grupo
    time.sleep(2)

    # PASSO 2: Enviar a mensagem para o grupo
    print("\n--- PASSO 2: Disparando a mensagem ---")
    url_send = f"{BASE_URL}/message/sendText/{INSTANCE}"
    
    payload = {
        "number": GROUP_JID,
        "textMessage": {
            "text": (
                "🔥 *OFERTA IMPERDÍVEL MERCADO LIVRE*\n\n"
                "📌 *Luminária LED Touch Sem Fio*\n"
                "✅ *Por apenas: R$ 64,90*\n\n"
                "🔗 *Garanta a sua aqui:* https://mercadolivre.com.br\n\n"
                "⚡ *Aproveite antes que acabe o estoque!*"
            )
        }
    }

    res_send = requests.post(url_send, json=payload, headers=HEADERS)
    print("Status HTTP do Envio:", res_send.status_code)
    print("Resposta do Envio:", res_send.text)

if __name__ == "__main__":
    enviar_promocao()
