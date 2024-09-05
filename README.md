# Automação de Busca no Google com Selenium

Este projeto realiza a automação do processo de busca no Google e captura os títulos dos resultados da pesquisa utilizando a biblioteca Selenium.

## Estrutura do Projeto

automacao-google-selenium/
│
├── src/
│   └── automacao_google.py
│
├── .gitignore
├── README.md
└── requirements.txt


## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/automacao-google-selenium.git
   cd automacao-google-selenium

2.  Construa a imagem Docker:
    docker build -t automacao-google-selenium .

3.  Execute o contêiner Docker:
    docker run --rm automacao-google-selenium