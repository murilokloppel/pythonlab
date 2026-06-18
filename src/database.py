import sqlite3
import pandas as pd

def inicializar_banco():
    with sqlite3.connect('DB_PATH') as conn:
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

def salvar_produto(titulo, preco):
    try:
        with sqlite3.connect('DB_PATH') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO produtos (titulo, preco) VALUES (?, ?)", (titulo, preco))
            conn.commit()
    except sqlite3.IntegrityError:
        print(f"Aviso: O produto '{titulo}' já existe no banco. Ignorando...")

def ler_produtos():
    with sqlite3.connect('DB_PATH') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        resultados = cursor.fetchall()

    if not resultados:
        print("O banco de dados está vazio.")
    else:
        for linha in resultados:
            print(f"ID: {linha[0]} | Produto: {linha[1]} | Preço: R${linha[2]:.2f} | Coleta (UTC): {linha[3]}")

def limpar_banco():
    with sqlite3.connect('DB_PATH') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos")
        conn.commit()
    print("Banco limpo! Prontinho para novos dados.")


def exportar_para_excel():
    try:
        conn = sqlite3.connect('DB_PATH')

        query = "SELECT * FROM produtos"
        df = pd.read_sql_query(query, conn)

        conn.close()


        df.to_excel('EXCEL_PATH', index=False)
        print("Sucesso! O arquivo 'EXCEL_PATH' foi gerado.")

    except Exception as e:
        print(f"Erro ao gerar Excel: {e}")