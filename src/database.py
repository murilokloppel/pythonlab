import sqlite3

def inicializar_banco():
    conn = sqlite3.connect('monitor_precos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            preco REAL,
            data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def salvar_produto(titulo, preco):
    conn = sqlite3.connect('monitor_precos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (titulo, preco) VALUES (?, ?)", (titulo, preco))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    inicializar_banco()
    print("Banco de dados 'monitor_precos.db' criado/verificado com sucesso!")


def ler_produtos():
    conn = sqlite3.connect('monitor_precos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    resultados = cursor.fetchall()

    if not resultados:
        print("O banco de dados está vazio.")
    else:
        for linha in resultados:
            # linha[0] é o id, linha[1] é o título, linha[2] é o preço, linha[3] é a data
            print(f"ID: {linha[0]} | Produto: {linha[1]} | Preço: R${linha[2]:.2f} | Coleta: {linha[3]}")

    conn.close()