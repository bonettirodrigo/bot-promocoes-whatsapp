import os
import requests

# Configurações do ambiente
EVOLUTION_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com").rstrip("/")
API_KEY = os.getenv("AUTHENTICATION_API_KEY")
INSTANCE_NAME = "bot_promocoes"
CHAT_ID = "120363430235680804@g.us"

def enviar_mensagem_teste():
    # Rota padrão de envio de texto no Evolution API
    url = f"{EVOLUTION_URL}/message/sendText/{INSTANCE_NAME}"
    
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
            "text": (
                "🔥 *TESTE DE CONEXÃO COM O BOT*\n\n"
                "Se recebeu esta mensagem, o GitHub Actions e a Evolution API estão 100% integrados!"
            )
        }
    }
    
    print(f"Enviando requisição para: {url}")
    print(f"Usando chave apikey iniciada em: {str(API_KEY)[:5]}...")
    
    response = requests.post(url, json=payload, headers=headers)
    
    print("Código HTTP:", response.status_code)
    print("Resposta da API:", response.text)

if __name__ == "__main__":
    enviar_mensagem_teste()
