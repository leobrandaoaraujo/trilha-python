# CrossfitApi
## Version: 0.1.0

### /atletas/

#### GET
##### Summary:

Listar atletas

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

#### POST
##### Summary:

Criar um novo atleta

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

### /atletas/{id}

#### GET
##### Summary:

Consultar um atleta pelo ID

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string (uuid4) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### PATCH
##### Summary:

Editar um atleta pelo ID

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string (uuid4) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### DELETE
##### Summary:

Excluir um atleta pelo ID

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string (uuid4) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | Successful Response |
| 422 | Validation Error |

### /atletas/{nome}

#### GET
##### Summary:

Consultar um atleta pelo NOME

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| nome | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### /atletas/{cpf}

#### GET
##### Summary:

Consultar um atleta pelo CPF

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| cpf | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### /centros_treinamento/

#### GET
##### Summary:

Listar centros de treinamento

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

#### POST
##### Summary:

Criar um novo centro de treinamento

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

### /centros_treinamento/{id}

#### GET
##### Summary:

Consultar um centro de treinamento pelo ID

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string (uuid4) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### /categorias/

#### GET
##### Summary:

Listar categorias

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

#### POST
##### Summary:

Criar uma nova categoria

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

### /categorias/{id}

#### GET
##### Summary:

Consultar uma categoria pelo ID

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string (uuid4) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |
