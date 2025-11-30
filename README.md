# AutoU - Classificador e Resposta Automática de Emails

## Descrição

O **AutoU** é uma aplicação web que permite **classificar emails** em **Produtivo** ou **Improdutivo** e **sugerir respostas automáticas**, ajudando equipes a economizar tempo e aumentar produtividade.

---

## Funcionalidades

- Upload de emails em `.txt` ou `.pdf` ou inserção direta de texto.
- Classificação automática: **Produtivo** ou **Improdutivo**.
- Sugestão de respostas automáticas baseadas na categoria do email.
- Interface web simples e intuitiva conectada ao backend Python.

---

## Tecnologias Utilizadas

- **Frontend:** HTML, CSS  
- **Backend:** Python (Flask)  
- **Processamento de texto:** técnicas de análise de conteúdo  
- **Hospedagem:** (Render)

---

## Estrutura do Repositório



autoU_project/
│
├─ app.py # Backend principal (Flask)
├─ templates/ # HTML da interface web
├─ static/ # CSS, JS e imagens
├─ requirements.txt # Dependências do projeto
├─ Procfile # Configuração de deploy (Heroku)
├─ test_openai.py # Scripts de teste da aplicação
├─ .gitignore # Arquivos ignorados pelo Git
└─ README.md # Este arquivo


---

## Como Executar Localmente

1. Clone o repositório:

git clone https://github.com/f2codesystems/autoU_project.git
cd autoU_project


Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Instale as dependências:

pip install -r requirements.txt


Execute o servidor:

python app.py


Acesse a aplicação no navegador:

http://localhost:5000

Link da Aplicação Deployada

https://autou-project.onrender.com

Observações

O AutoU é um projeto focado em automatizar a leitura, classificação e resposta de emails, oferecendo uma solução prática para equipes que lidam com grande volume de mensagens.

