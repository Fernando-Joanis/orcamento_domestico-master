# API Orçamento Doméstico

API com a função de salvar e exibir seus gastos no mês atual.

## Endpoints

Api conta com os métodos abaixo:

| Verbo HTTP |        Path         |            Função            |
|:----------:|:-------------------:|:----------------------------:|
|    GET     |    /api/despesas    | Listar despesas mês corrente |
|    POST    |    /api/despesas    |      Cadastrar despesa       |


## Key e formato dos Values para envio

Para os métodos POST deve ser enviado os seguintes parâmetros:

|        KEY         |                 VALUE                  |
|:------------------:|:--------------------------------------:|
|       valor        |    números Exemplo: 1254 ou 123.25     |
|    data_compra     |    ANO-MÊS-DIA Exemplo: 2022-05-07     |
|     descricao      |                 String                 |
| tipos_pagamento_id | Número inteiro == ID tipo de pagamento |
|    categoria_id    |     Número inteiro == ID categoria     |

### Tipos pagamento IDs

| id  |  valor   |
|:---:|:--------:|
|  1  | dinheiro |
|  2  |  débito  |
|  3  | crédito  |
|  4  |   pix    |


### Categorias IDs

| id  |    valor     |
|:---:|:------------:|
|  1  |  custo fixo  |
|  2  | alimentação  |
|  3  |  transporte  |
|  4  | medicamentos |


```json
{
    "data": [{
      "id": 1,
      "valor": "R$1,234.00",
      "data_compra": "2022-09-20",
      "descricao": "Compra do mês",
      "tipos_pagamento_id": "débito",
      "categoria_id": "alimentação"
    }],
    "success": true
}
```
