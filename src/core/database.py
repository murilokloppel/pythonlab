import sqlite3
import pandas as pd

class ConexaoBanco:
    def __init__(self, db_path='bd_precos.db', excel_path='excel_precos.xlsx'):
        self.db_path = db_path
        self.excel_path = excel_path
        self.inicializar_banco()

    def inicializar_banco(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL UNIQUE, 
                    preco REAL NOT NULL,
                    data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def salvar(self, item):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO produtos (titulo, preco) VALUES (?, ?)",
                               (item['titulo'], item['preco']))
                conn.commit()
        except sqlite3.IntegrityError:
            print(f"Aviso: O produto '{item['titulo']}' já existe. Ignorando...")

    def ler_todos(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produtos")
            return cursor.fetchall()

    def limpar_banco(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos")
            conn.commit()
        print("Banco limpo!")

    def exportar_para_excel(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                df = pd.read_sql_query("SELECT * FROM produtos", conn)

            df.to_excel(self.excel_path, index=False)
            print(f"Sucesso! O arquivo '{self.excel_path}' foi gerado.")
        except Exception as e:
            print(f"Erro ao gerar Excel: {e}")