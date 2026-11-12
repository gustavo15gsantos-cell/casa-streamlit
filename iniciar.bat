@echo off
cd /d "%~dp0"
if not exist .venv (
  echo Criando ambiente virtual...
  python -m venv .venv
)
call .venv\Scripts\activate
echo Instalando bibliotecas...
pip install -r requirements.txt
echo Iniciando o site...
streamlit run app.py
pause
