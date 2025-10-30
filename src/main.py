# main.py
# Programa principal para simulação de análise anti-fraude

from analyzer import extract_card_data
from validator import validate_card_data

def main():
    # Simula o caminho de uma imagem de cartão
    image_path = "data/sample_card.jpg"

    # Extrai os dados do cartão
    card_data = extract_card_data(image_path)
    print("Dados do cartão extraídos:")
    for key, value in card_data.items():
        print(f"{key}: {value}")

    # Valida os dados do cartão
    alerts = validate_card_data(card_data)
    if alerts:
        print("\n⚠️ Alertas de fraude encontrados:")
        for alert in alerts:
            print(f"- {alert}")
    else:
        print("\n✅ Nenhum alerta de fraude encontrado.")

if __name__ == "__main__":
    main()
