# CrossfitApi
## Version: 0.1.0

## With: FastAPI | Uvicorn | SQLAlchemy | Pydantic

### Schema Model (Exemplo)

    {
      "pk_id": "e544f399-e148-4068-8112-613886d598aa",
      "created_at": "2024-06-05T20:35:33.095Z",
      "nome": "João",
      "cpf": "12345678911",
      "idade": 25,
      "peso": 75.5,
      "altura": 1.7,
      "sexo": "M",
      "categoria": {
        "nome": "Scale"
      },
      "centro_treinamento": {
        "nome": "King",
        "endereco": "Rua A, 123, São José",
        "proprietario": "Marcus Silva"
      }
    }

# Endpoints (Atletas)

### GET /atletas/

    curl -X 'GET' 'http://127.0.0.1:8000/atletas/' -H 'accept: application/json'

    Request URL: http://127.0.0.1:8000/atletas/

#### Ação: Listar atletas

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

### POST /atletas/

    curl -X 'POST' 'http://127.0.0.1:8000/atletas/' -H 'accept: application/json' -H 'Content-Type: application/json'
      -d '{
        "pk_id": "string",
        "created_at": "2024-06-05T20:35:33.095Z",
        "nome": "João",
        "cpf": "12345678911",
        "idade": 25,
        "peso": 75.5,
        "altura": 1.7,
        "sexo": "M",
        "categoria": {
          "nome": "Scale"
        },
        "centro_treinamento": {
          "nome": "King",
          "endereco": "Rua A, 123, São José",
          "proprietario": "Marcus Silva"
        }
      }'

#### Ação: Criar um novo atleta

#### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

### GET /atletas/{id}

    curl -X 'GET' 'http://127.0.0.1:8000/atletas/e544f399-e148-4068-8112-613886d598aa' -H 'accept: application/json'

    Request URL: http://127.0.0.1:8000/atletas/e544f399-e148-4068-8112-613886d598aa

#### Ação: Consultar um atleta pelo ID

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| pk_id | path |  | Yes | string (uuid4) |

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### PATCH /atletas/{id}

    curl -X 'PATCH' 'http://127.0.0.1:8000/atletas/e544f399-e148-4068-8112-613886d598aa' -H 'accept: application/json' -H 'Content-Type: application/json'
      -d '{
        "pk_id": "string",
        "created_at": "2024-06-05T21:00:01.644Z",
        "nome": "João",
        "cpf": "12345678911",
        "idade": 25,
        "peso": 75.5,
        "altura": 1.7,
        "sexo": "M",
        "categoria": {
          "nome": "Scale"
        },
        "centro_treinamento": {
          "nome": "King",
          "endereco": "Rua A, 123, São José",
          "proprietario": "Marcus Silva"
        }
      }'

    Request URL: http://127.0.0.1:8000/atletas/e544f399-e148-4068-8112-613886d598aa      

#### Ação: Editar um atleta pelo ID

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| pk_id | path |  | Yes | string (uuid4) |

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### DELETE /atletas/{id}

    curl -X 'DELETE' 'http://127.0.0.1:8000/atletas/e544f399-e148-4068-8112-613886d598aa' -H 'accept: */*'

    Request URL: http://127.0.0.1:8000/atletas/e544f399-e148-4068-8112-613886d598aa

#### Ação: Excluir um atleta pelo ID

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| pk_id | path |  | Yes | string (uuid4) |

#### Responses

| Code | Description |
| ---- | ----------- |
| 204 | Successful Response |
| 422 | Validation Error |

### GET /atletas/{nome}

    curl -X 'GET' 'http://127.0.0.1:8000/atletas/Marcelo' -H 'accept: application/json'

    Request URL: http://127.0.0.1:8000/atletas/Marcelo

#### Ação: Consultar um atleta pelo NOME

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| nome | path |  | Yes | string |

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### GET /atletas/{cpf}

    curl -X 'GET' 'http://127.0.0.1:8000/atletas/12345678911' -H 'accept: application/json'

    Request URL: http://127.0.0.1:8000/atletas/12345678911

#### Ação: Consultar um atleta pelo CPF

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| cpf | path |  | Yes | string |

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

# Endpoints (Centros de Treinamento)

### GET /centros_treinamento/

    curl -X 'GET' 'http://127.0.0.1:8000/centros_treinamento/' -H 'accept: application/json'

    Request URL: http://127.0.0.1:8000/centros_treinamento/

#### Ação: Listar centros de treinamento

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

### POST

    curl -X 'POST' 'http://127.0.0.1:8000/centros_treinamento/' -H 'accept: application/json' -H 'Content-Type: application/json'
      -d '{
          "nome": "King",
          "endereco": "Rua A, 123, São José",
          "proprietario": "Marcus Silva"
        }'

#### Ação: Criar um novo centro de treinamento

#### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

### GET /centros_treinamento/{id}

    curl -X 'GET' 'http://127.0.0.1:8000/centros_treinamento/e544f399-e148-4068-8112-613886d598aa' -H 'accept: application/json'

    Request URL: http://127.0.0.1:8000/centros_treinamento/e544f399-e148-4068-8112-613886d598aa

#### Ação: Consultar um centro de treinamento pelo ID

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string (uuid4) |

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

# Endpoints (Categorias)

### GET /categorias/

    curl -X 'GET' 'http://127.0.0.1:8000/categorias/' -H 'accept: application/json'

    Request URL: http://127.0.0.1:8000/categorias/

#### Ação: Listar categorias

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

### POST

    curl -X 'POST' 'http://127.0.0.1:8000/categorias/' -H 'accept: application/json' -H 'Content-Type: application/json'
      -d '{
          "nome": "Scale"
        }'

#### Ação: Criar uma nova categoria

#### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

### GET /categorias/{id}

    curl -X 'GET' 'http://127.0.0.1:8000/categorias/e544f399-e148-4068-8112-613886d598aa' -H 'accept: application/json'

    Request URL: http://127.0.0.1:8000/categorias/e544f399-e148-4068-8112-613886d598aa

#### Ação: Consultar uma categoria pelo ID

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string (uuid4) |

#### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |
