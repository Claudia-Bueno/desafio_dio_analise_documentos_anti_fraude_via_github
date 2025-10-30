# validator.py
# Simula validações anti-fraude do cartão usando configurações do Azure

from config import settings

def validate_card(card_data):
    """
    Recebe um dicionário com dados do cartão e retorna
    um dicionário com resultado das validações.
    """
    results = {
        "numero_valido": True,
        "cartao_vencido": False,
        "banco_suspeito": False
    }

    if settings.SIMULATE_VALIDATION:
        # Simulação de validação
        if card_data.get("numero") == "1234 5678 9012 3456":
            results["numero_valido"] = False
        if card_data.get("validade") == "12/20":
            results["cartao_vencido"] = True
        if card_data.get("banco") == "Banco Suspeito":
            results["banco_suspeito"] = True
    else:
        # Aqui você poderia colocar código real de integração com Azure
        results = {}
    
    return results


