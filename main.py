import json
from src.crawlers.mercado_livre_crawler import MercadoLivreMonitor

def iniciar_monitoramento():
    try:
        with open("produtos.json", "r", encoding="utf-8") as f:
            lista_de_produtos = json.load(f)
    except FileNotFoundError:
        print("Erro: O arquivo 'produtos.json' não foi encontrado na raiz.")
        return
    except json.JSONDecodeError as e:
        print(f"Erro ao ler 'produtos.json': {e}")
        return

    monitor = None
    try:
        monitor = MercadoLivreMonitor()
        print(f"Iniciando monitoramento de {len(lista_de_produtos)} produtos...")
        dados_coletados = monitor.executar(lista_de_produtos)
        print("\n--- Resultados Coletados ---")
        print(json.dumps(dados_coletados, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")
    finally:
        if monitor:
            try:
                monitor.fechar()
            except Exception:
                pass
        print("\nNavegador fechado. Processo concluído.")

if __name__ == "__main__":
    iniciar_monitoramento()
