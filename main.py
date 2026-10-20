import os
import requests

EVOLUTION_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com").rstrip("/")
API_KEY = os.getenv("AUTHENTICATION_API_KEY")
INSTANCE_NAME = "bot_promocoes"
CHAT_ID = "120363430235680804@g.us"

HEADERS = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

def garantir_instancia():
    """Verifica se a instância existe; se não existir, cria-a automaticamente."""
    url_check = f"{EVOLUTION_URL}/instance/fetchInstances"
    try:
        res = requests.get(url_check, headers=HEADERS)
        if res.status_code == 200:
            instancias = res.json()
            # Procura a instância pelo nome
            for inst in instancias:
                if isinstance(inst, dict) and inst.get("name") == INSTANCE_NAME:
                    print(f"✅ Instância '{INSTANCE_NAME}' encontrada com sucesso.")
                    return True
    except Exception as e:
        print(f"Aviso ao consultar instâncias: {e}")

    print(f"⚠️ Instância '{INSTANCE_NAME}' não encontrada no servidor. Criando nova instância...")
    url_create = f"{EVOLUTION_URL}/instance/create"
    payload_create = {
        "instanceName": INSTANCE_NAME,
        "token": API_KEY,
        "qrcode": True
    }
    res_create = requests.post(url_create, json=payload_create, headers=HEADERS)
    print("Resultado da criação:", res_create.status_code, res_create.text)

def enviar_mensagem_teste():
    garantir_instancia()

    url_send = f"{EVOLUTION_URL}/message/sendText/{INSTANCE_NAME}"
    texto = (
        "🔥 *OFERTA MERCADO LIVRE*\n\n"
        "📌 *Luminária de Mesa LED Articulada Touch*\n"
        "❌ De: ~R$ 120.00~\n"
        "✅ *Por: R$ 64.90* (Cupom: `MELI10`)\n"
        "🚚 *Frete Grátis*\n"
        "⭐ Avaliação: 4.8/5.0\n\n"
        "🔗 *Garanta o seu aqui:* https://mercadolivre.com.br/sec/seu_link_afiliado"
    )

    payload = {
        "number": CHAT_ID,
        "options": {"delay": 1200, "presence": "composing"},
        "textMessage": {"text": texto}
    }

    print(f"Disparando mensagem para {CHAT_ID}...")
    response = requests.post(url_send, json=payload, headers=HEADERS)
    print("Código HTTP:", response.status_code)
    print("Resposta do WhatsApp:", response.text)

if __name__ == "__main__":
    enviar_mensagem_teste()
