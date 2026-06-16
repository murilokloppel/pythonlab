from src.database import salvar_produto, ler_produtos

produtos_para_teste = [
    ("iPhone 15 Plus", 6500.00),
    ("iPhone 15 Pro Max", 8900.00)
]

print("Inserindo produtos...")
for titulo, preco in produtos_para_teste:
    salvar_produto(titulo, preco)

print("Lendo banco de dados:")
ler_produtos()