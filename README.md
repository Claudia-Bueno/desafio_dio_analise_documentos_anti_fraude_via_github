# Desafio DIO – Análise de Documentos Anti-fraude com Azure AI (Simulação via GitHub)

Projeto foi desenvolvido como parte do desafio **"Análise de Documentos Anti-fraude com Azure AI"** da **DIO**.  
Projeto foi feito com uma **simulação completa**, ilustrando como o sistema funcionaria com o Azure Document Intelligence (antigo Form Recognizer).

---

## Objetivo

O sistema tem como objetivo **analisar imagens de cartões bancários** e simular uma **verificação anti-fraude**, identificando possíveis irregularidades como:

- Número de cartão inválido;
- Cartão vencido;
- Banco suspeito.

Tudo foi implementado em **Python**, com uma estrutura modular e organizada, pronta para futura integração com o **Azure AI**.

---

## Estrutura do Projeto

```text
desafio_dio_analise_documentos_anti_fraude_via_github/
├── src/
│   ├── analyzer.py        # simula a extração de dados do cartão
│   ├── validator.py       # faz validações anti-fraude
│   └── main.py            # executa o programa principal
├── config/settings.py     # simula configurações do Azure
├── data/sample_card.jpg   # imagem de exemplo do cartão
├── requirements.txt       # bibliotecas utilizadas
└── README.md              # documentação completa


# Clone este repositório
git clone https://github.com/Claudia-Bueno/desafio_dio_analise_documentos_anti_fraude_via_github.git

# Entre na pasta do projeto
cd desafio_dio_analise_documentos_anti_fraude_via_github

# Execute o programa principal
python src/main.py

O sistema exibirá os dados simulados do cartão e o resultado da validação anti-fraude.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas padrão para manipulação de arquivos e simulação de dados
- Estrutura pensada para futura integração com Azure AI

---

## 📝 Observações

- Este projeto é uma **simulação completa** e não realiza validação real de cartões.
- Ideal para fins didáticos e demonstração de arquitetura de projeto.

---

### Próximo passo para salvar:

1. No GitHub, se você editou o README.md online:
   - Clique em **“Commit changes”** no final da página.
   - Coloque uma mensagem tipo: `Atualiza README com instruções e estrutura do projeto`.
   - Clique em **Commit changes**.

2. Se estiver editando localmente:
   - Salve o arquivo (Ctrl+S ou Cmd+S).
   - Faça o commit e push:

```bash
git add README.md
git commit -m "Atualiza README com instruções e estrutura do projeto"
git push origin main

 
