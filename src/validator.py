# validator.py
# Simula validações anti-fraude para dados do cartão

def validate_card_data(card_data):
    """
    Recebe um dicionário com dados do cartão e retorna
    um dicionário com possíveis alertas de fraude.
    """
    alerts = []

    # Verifica se o número do cartão tem 16 dígitos
    numero = card_data.get("numero", "").replace(" ", "")
    if len(numero) != 16 or not numero.isdigit():
        alerts.append("Número do cartão inválido")

    # Verifica se o cartão está vencido (simulação simples)
    validade = card_data.get("validade", "")
    if validade < "10/23":  # só como exemplo
        alerts.append("Cartão vencido")

    # Verifica se o banco é suspeito
    banco = card_data.get("banco", "")
    bancos_suspeitos = ["Banco Suspeito", "Banco X"]
    if banco in bancos_suspeitos:
        alerts.append("Banco suspeito")

    return alerts

