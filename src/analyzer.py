# analyzer.py
# Simula a extração de dados do cartão bancário

def extract_card_data(image_path):
    """
    Recebe o caminho da imagem do cartão e retorna um dicionário
    com dados simulados do cartão.
    """
    # Simulação de dados extraídos
    card_data = {
        "numero": "1234 5678 9012 3456",
        "validade": "12/25",
        "banco": "Banco Exemplo",
        "titular": "Claudia Bueno"
    }
    print(f"[INFO] Dados extraídos da imagem {image_path}: {card_data}")
    return card_data

# Teste rápido
if __name__ == "__main__":
    sample_image = "data/sample_card.jpg"
    extract_card_data(sample_image)
