import os
import requests

EVOLUTION_URL = os.getenv("EVOLUTION_URL", "https://evolution-api-0ptv.onrender.com")
API_KEY = os.getenv("AUTHENTICATION_API_KEY", "123456")
INSTANCE_NAME = "bot_promocoes"
CHAT_ID = "120363430235680804@g.us"

PRECO_MAXIMO = 200.00
AVALIACAO_MINIMA = 4.5
CATEGORIAS_PERMITIDAS = [
    "Casa e Móveis", 
    "Tecnologia", 
    "Eletrodomésticos"
]

def validar_oferta(produto):
    if produto['preco_novo'] > PRECO_MAXIMO:
        return False
    if produto.get('avaliacao', 5.0) < AVALIACAO_MINIMA:
        return False
    if not produto.get('frete_gratis', True):
        return False
    if produto.get('categoria') not in CATEGORIAS_PERMITIDAS:
        return False
    return True

def formatar_e_enviar(produto):
    if not validar_oferta(produto):
        print(f"Produto ignorado pelos filtros: {produto['titulo']} (R$ {produto['preco_novo']})")
        return

    url = f"{EVOLUTION_URL}/message/sendText/{INSTANCE_NAME}"
    texto_cupom = f"\n🎟️ *Cupom Mercado Livre:* `{produto['cupom']}`" if produto.get('cupom') else ""
    
    texto_mensagem = (
        f"🔥 *OFERTA MERCADO LIVRE (Até R$ 200)*\n\n"
        f"📌 *{produto['titulo']}*\n"
        f"❌ De: ~R$ {produto['preco_antigo']:.2f}~\n"
        f"✅ *Por: R$ {produto['preco_novo']:.2f}*{texto_cupom}\n"
        f"🚚 *Frete Grátis*\n"
        f"⭐ Avaliação: {produto.get('avaliacao', 5.0)}/5.0\n\n"
        f"🔗 *Garanta o seu aqui:* {produto['link']}"
    )
    
    payload = {
        "number": CHAT_ID,
        "options": {"delay": 1200, "presence": "composing"},
        "textMessage": {"text": texto_mensagem}
    }
    
    headers = {"apikey": API_KEY, "Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    exemplo_produto = {
        "titulo": "Luminária de Mesa LED Articulada Touch",
        "preco_antigo": 120.00,
        "preco_novo": 64.90,
        "avaliacao": 4.8,
        "frete_gratis": True,
        "categoria": "Casa e Móveis",
        "cupom": "MELI10",
        "link": "https://mercadolivre.com.br/sec/seu_link_afiliado"
    }
    print("Enviando promoção de teste do Mercado Livre...")
    resultado = formatar_e_enviar(exemplo_produto)
    print("Resposta do WhatsApp:", resultado)
