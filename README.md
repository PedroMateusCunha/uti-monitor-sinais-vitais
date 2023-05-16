# Monitor de UTI - Emulador de Sinais Vitais com IoT

Este repositório contém um microserviço em Python que emula um monitor de sinais vitais de UTI (Unidade de Terapia Intensiva) usando o framework FastAPI.

### Recursos
- Simula dados de sinais vitais para vários leitos de UTI.
- Gera leituras aleatórias de sinais vitais dentro de faixas pré-definidas.
- Detecta sinais vitais anormais e dispara alertas.
- Fornece uma API para recuperar dados de sinais vitais de cada leito.

Instalação
Clone o repositório:

bash
$ git clone <URL_DO_REPOSITÓRIO>
Acesse o diretório do projeto:

bash
$ cd <NOME_DO_DIRETÓRIO>
Instale as dependências:

bash
$ pip install -r requirements.txt
Uso
Inicie o servidor FastAPI:

bash
$ uvicorn main:app --reload
O servidor estará em execução em http://localhost:8000.

Acesse as rotas da API usando uma ferramenta como cURL ou Postman.

Rotas da API
Obter leitos da UTI
Endpoint: /leitos
Método: GET
Descrição: Recupera a lista de leitos da UTI juntamente com seus IDs.
Obter Sinais Vitais de uma Cama
Endpoint: /leitos/{id_cama}/sinais-vitais
Método: GET
Descrição: Recupera os últimos dados de sinais vitais para uma cama específica da UTI.
Obter Alertas de uma Cama
Endpoint: /leitos/{id_cama}/alertas
Método: GET
Descrição: Recupera os últimos alertas para uma cama específica da UTI.
Obter Dados de Todas as leitos
Endpoint: /leitos/todas
Método: GET
Descrição: Recupera os últimos dados de sinais vitais e alertas para todas as leitos da UTI.
