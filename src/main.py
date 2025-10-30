from analyzer import extract_card_data
from validator import validate_card

def main():
    # Simula a leitura de um cartão
    card_image = "data/sample_card.jpg"
    card_data = extract_card_data(card_image)

    # Validação anti-fraude
    validation_result = validate_card(card_data)

    # Exibe os resultados
    print("Dados do cartão:")
    for key, value in card_data.items():
        print(f"{key}: {value}")

    print("\nResultado da validação anti-fraude:")
    print(validation_result)

if __name__ == "__main__":
    main()
