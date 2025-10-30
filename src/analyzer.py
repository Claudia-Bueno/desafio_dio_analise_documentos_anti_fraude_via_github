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
        "banco": "Banco Exemplo"
    }
    return card_data
