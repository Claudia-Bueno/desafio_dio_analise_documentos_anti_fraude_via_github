# validator.py
# Simula validações anti-fraude em dados de cartão

def validate_card(card_data):
    """
    Recebe um dicionário com os dados do cartão e retorna
    um dicionário com possíveis alertas de fraude.
    """
    alerts = []

    # Validação do número do cartão (simulada)
    if card_data["numero"].startswith("0000"):
        alerts.append("Número de cartão inválido")

    # Validação da data de validade
    if card_data["validade"] < "23/10":  # data atual simulada
        alerts.append("Cartão vencido")

    # Validação do banco
    if card_data["banco"] == "Banco Suspeito":
        alerts.append("Banco suspeito")

    if not alerts:
        alerts.append("Cartão aprovado")

    return alerts
