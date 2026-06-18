import json
from src.monitores.mercado_livre_monitor import MercadoLivreMonitor

def iniciar_monitoramento():

    try:
        with open("produtos.json", "r", encoding="utf-8") as f:
            lista_de_produtos = json.load(f)
    except FileNotFoundError:
        print("Erro: O arquivo 'produtos.json' não foi encontrado na raiz.")
        return

    monitor = MercadoLivreMonitor()

    try:
        print(f"Iniciando monitoramento de {len(lista_de_produtos)} produtos...")

        # 3. Executa a busca
        dados_coletados = monitor.executar(lista_de_produtos)

        print("\n--- Resultados Coletados ---")
        print(json.dumps(dados_coletados, indent=4, ensure_ascii=False))


    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")

    finally:

        monitor.fechar()
        print("\nNavegador fechado. Processo concluído.")

if __name__ == "__main__":
    iniciar_monitoramento()