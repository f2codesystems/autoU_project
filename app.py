import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# ------------------------- CARREGAR VARIÁVEIS DE AMBIENTE -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # pasta do projeto
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ ERRO: OPENAI_API_KEY não encontrada no .env")

# ------------------------- INICIALIZAR CLIENTE OPENAI -------------------------
client = OpenAI()

# ------------------------- INICIALIZAR FLASK -------------------------
app = Flask(__name__)

# ------------------------- GARANTIR NLTK -------------------------
nltk_data_dir = os.path.join(BASE_DIR, "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", download_dir=nltk_data_dir, quiet=True)

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", download_dir=nltk_data_dir, quiet=True)

# ------------------------- FUNÇÕES -------------------------

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("portuguese"))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return " ".join(tokens)

def read_file(file):
    if file.filename.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
        return text

    return None

def classify_and_respond(email_text):
    processed = preprocess_text(email_text)

    prompt = f"""
Analise o seguinte e-mail e:
1. Classifique-o como 'Produtivo' ou 'Improdutivo'.
2. Sugira uma resposta automática (curta e objetiva).

E-mail original:
{email_text}

E-mail pré-processado:
{processed}
"""

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            temperature=0.5
        )

        return response.output_text

    except Exception as e:
        return f"❌ Erro ao acessar OpenAI: {e}"

# ------------------------- ROTAS -------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    if request.method == "POST":
        email_text = request.form.get("email_text")
        file = request.files.get("file")

        if file and file.filename:
            email_text = read_file(file)

        if email_text:
            result = classify_and_respond(email_text)
    
    return render_template("index.html", result=result)

# ------------------------- RUN -------------------------
if __name__ == "__main__":
    print("🔑 OPENAI_API_KEY carregada:", OPENAI_API_KEY[:10] + "... OK")
    port = int(os.environ.get("PORT", 5001))
    print(f"🚀 Iniciando Flask em http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)
