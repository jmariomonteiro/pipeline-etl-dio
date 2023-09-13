
# Projeto de Atribuição de Nomes e Frases Motivacionais

Este projeto consiste em um script Python que atribui nomes e frases motivacionais a usuários com base em um arquivo CSV de entrada. Ele também inclui a funcionalidade de atualizar as frases motivacionais existentes no JSON resultante.

## Requisitos

- Python 3.x
- Pandas (instalável via `pip install pandas`)
- OpenAI Python (instalável via `pip install openai`)

## Uso

1. Clone o repositório para o seu sistema local.

2. Configure sua chave de API da OpenAI no arquivo Python.

3. Coloque o arquivo CSV de entrada na pasta de dados.

4. Execute o script Python:


5. O script atribuirá nomes e frases motivacionais aos usuários e atualizará as frases existentes no JSON.

6. Os resultados serão exibidos no console e salvos em um arquivo JSON.

## Configuração da Chave de API da OpenAI

Para usar a API da OpenAI, é necessário configurar a sua chave de API no arquivo Python. Você pode obtê-la na [plataforma da OpenAI](https://platform.openai.com/account/api-keys).

```python
openai.api_key = 'SUA_CHAVE_DE_API_AQUI'

