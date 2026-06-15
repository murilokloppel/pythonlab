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