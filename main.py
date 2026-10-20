import os
import requests

EVOLUTION_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com").rstrip("/")
API_KEY = os.getenv("AUTHENTICATION_API_KEY", "123456")
INSTANCE_NAME = "bot_promocoes"
CHAT_ID = "120363430235680804@g.us"

def enviar_mensagem_teste():
    # Rota padrão para envio de texto no Evolution API
    url = f"{EVOLUTION_URL}/message/sendText/{INSTANCE_NAME}"
    
    texto_mensagem = (
        "🔥 *TESTE DE CONEXÃO COM O BOT*\n\n"
        "Se recebeu esta mensagem, o GitHub Actions e a Evolution API estão 100% integrados!"
    )
    
    payload = {
        "number": CHAT_ID,
        "text": texto_mensagem
    }
    
    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }
    
    print(f"Enviando requisição para: {url}")
    response = requests.post(url, json=payload, headers=headers)
    
    print("Código HTTP:", response.status_code)
    print("Resposta do WhatsApp:", response.text)
    return response

if __name__ == "__main__":
    enviar_mensagem_teste()
