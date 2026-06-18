import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("ML_TOKEN")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://www.mercadolivre.com.br/",
    "Origin": "https://www.mercadolivre.com.br/",
    "Connection": "keep-alive"
}
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(ROOT_DIR, "bd_precos.db")
EXCEL_PATH = os.path.join(ROOT_DIR, "excel_precos.xlsx")
