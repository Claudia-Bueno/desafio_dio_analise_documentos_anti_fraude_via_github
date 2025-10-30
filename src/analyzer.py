# analyzer.py
# Simula a extração de dados do cartão bancário usando configurações do Azure

from config import settings

def extract_card_data(image_path):
    """
    Recebe o caminho da imagem do cartão e retorna um dicionário
    com dados simulados do cartão.
    """
    if settings.SIMULATE_EXTRACTION:
        # Simulação de dados extraídos
        card_data = {
            "numero": "1234 5678 9012 3456",
            "validade": "12/25",
            "banco": "Banco Exemplo"
        }
    else:
        # Aqui você poderia colocar código real de integração com Azure
        card_data = {}
    
    return card_data
