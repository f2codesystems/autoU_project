import os
from openai import OpenAI

# Pega a chave do ambiente
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Chave OPENAI_API_KEY não encontrada.")

client = OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Olá, teste de chave!"}],
        temperature=0
    )
    print("✅ Chave válida! Resposta da API:")
    print(response.choices[0].message.content)
except Exception as e:
    print("❌ Erro ao acessar OpenAI:", e)
