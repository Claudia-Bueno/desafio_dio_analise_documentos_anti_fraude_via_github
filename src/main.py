# main.py
# Programa principal do projeto de análise anti-fraude

from analyzer import extract_card_data
from validator import validate_card
from config import settings

def main():
    # Mostra as configurações (simuladas)
    print("=== Configurações do Azure (Simuladas) ===")
    print(f"API Key: {settings.AZURE_API_KEY}")
    print(f"Endpoint: {settings.AZURE_ENDPOINT}\n")
    
    # Simula o caminho da imagem do cartão
    image_path = "data/sample_card.jpg"
    
    # Extrai dados do cartão (simulado)
    card_data = extract_card_data(image_path)
    
    # Valida o cartão (simulado)
    validation_results = validate_card(card_data)
    
    # Exibe os resultados
    print("=== Dados do Cartão ===")
    for key, value in card_data.items():
        print(f"{key}: {value}")
    
    print("\n=== Resultados da Validação Anti-fraude ===")
    for key, value in validation_results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

