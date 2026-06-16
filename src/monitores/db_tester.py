from src.database import salvar_produto, ler_produtos, inicializar_banco, limpar_banco, exportar_para_excel

inicializar_banco()

limpar_banco()

produtos_para_teste = [
    ("iPhone 16 Plus", 6500.00),
    ("iPhone 16 Pro Max", 8900.00)
]

print("Inserindo produtos...")
for titulo, preco in produtos_para_teste:
    salvar_produto(titulo, preco)

print("Lendo banco de dados:")
ler_produtos()

exportar_para_excel()