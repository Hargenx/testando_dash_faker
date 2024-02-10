# Sistema Clínica - Dashboard

Este é um projeto de dashboard para análise de dados de uma clínica médica, utilizando a biblioteca Dash em Python.

## Instalação

1. Clone o repositório:

```bash
   git clone https://github.com/Hargenx/testando_dash_faker.git
 ```

2. Instale as dependências:
```bash
    pip install -r requirements.txt
```

3. Execute o aplicativo:
```bash
    python tela.py
```
    - O aplicativo será executado em http://127.0.0.1:8050/ por padrão.

## Configuração do Ambiente Virtual (Opcional)

É recomendável criar um ambiente virtual para isolar as dependências do projeto. Use o seguinte comando para criar e ativar um ambiente virtual:
```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
 ```

## Gerar Dados Fictícios
Se desejar gerar dados fictícios para testes, você pode usar o script faker.py:
```bash
    python faker.py
```
- Este script criará um arquivo CSV chamado dados_exemplo_br.csv com dados fictícios brasileiros.

## Dependências
    - Dash
    - Plotly
    - Pandas
    - Faker

## Estrutura do Projeto
- tela.py: Código principal do aplicativo Dash.
- faker.py: Script para gerar dados fictícios.
- dados_exemplo_br.csv: Arquivo CSV com dados fictícios brasileiros.

## Licença

Este projeto está sob a [Licença MIT](LICENSE).
