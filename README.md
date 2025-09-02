# ✈️ Previsão de Atraso de Voos

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/) 
[![Streamlit](https://img.shields.io/badge/streamlit-v1.49.1-orange)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.1-green)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

---

## 🔹 Descrição
Projeto para **prever atrasos em voos** usando dados públicos, pipeline ETL, Machine Learning e deploy em nuvem (AWS). Inclui dashboard interativo com Streamlit.

---

## 🗂 Estrutura do Projeto

flight-delay-mlops/
├─ README.md
├─ requirements.txt
├─ .env.example
├─ data/
│ ├─ raw/
│ └─ processed/
├─ models/
│ └─ model.joblib
├─ sql/
│ └─ create_tables.sql
├─ terraform/
│ └─ main.tf
└─ src/
├─ config.py
├─ utils.py
├─ make_sample.py
├─ etl.py
├─ train.py
├─ evaluate.py
├─ api_flask.py
└─ lambda_handler.py


---

## ⚡ Tecnologias
- Python 3.12  
- Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- Boto3 (AWS)  
- Flask, Streamlit  
- AWS S3, Lambda, EC2 (serverless e deploy)  
- Terraform (infraestrutura opcional)

---

## 🚀 Instalação

1. Clone o repositório:  
bash
git clone https://github.com/GabrielGomesAL/prever-atraso-de-voo.git
cd prever-atraso-de-voo/flight-delay-mlops
Crie e ative o ambiente virtual:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt


Configure variáveis de ambiente copiando .env.example para .env.

🧰 Uso
1. ETL
python src/etl.py

2. Treinamento do Modelo
python src/train.py

3. Avaliação do Modelo
python src/evaluate.py

4. Dashboard com Streamlit
streamlit run src/make_sample.py

5. API Flask (opcional)
python src/api_flask.py

📊 Dashboard

Visualiza taxa de atraso por companhia aérea

Horários com mais atrasos

Performance do modelo de IA

💡 Observações

Dados brutos ficam em data/raw

Dados processados em data/processed

Modelo treinado em models/model.joblib

Scripts de infraestrutura na pasta terraform/
