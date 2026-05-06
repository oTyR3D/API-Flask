# API de Testes – Calculadora, Usuários e Produtos

Projeto desenvolvido para a disciplina de testes de software e APIs, utilizando Python + Flask para implementação dos endpoints e Insomnia/Postman para validação das requisições.

---

# Objetivo do Projeto

O objetivo desta aplicação é demonstrar, de forma prática, diferentes tipos de testes aplicados em APIs REST:

- Testes funcionais
- Testes exploratórios
- Testes de regressão
- Testes não funcionais

A API foi construída com foco educacional, simulando cenários reais de validação de serviços HTTP.

---

# Tecnologias Utilizadas

- Python 3
- Flask
- JSON
- Insomnia / Postman

---

# Estrutura da API

## Endpoints disponíveis

### Calculadora

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/dividir?a=10&b=2` | Realiza divisão |
| GET | `/multiplicar?a=3&b=4` | Realiza multiplicação |

---

### Usuários

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/usuarios` | Cria usuário |
| DELETE | `/usuarios/<id>` | Remove usuário |

---

### Produtos

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/produtos` | Cria produto |
| GET | `/produtos` | Lista produtos |
| GET | `/produtos?categoria=vestuario` | Filtra produtos |

---

### Status

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/status` | Verifica disponibilidade da API |

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/oTyR3D/API-Flask.git
```

---

## 2. Entrar na pasta do projeto

```bash
cd API-Flask
```

---

## 3. Criar ambiente virtual (opcional)

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4. Instalar dependências

```bash
pip install flask
```
---

## 5. Executar a API

```bash
python app.py
```

A aplicação ficará disponível em:

```txt
http://localhost:5000
```

---

# Exemplos de Requisição

## Divisão válida

```http
GET /dividir?a=10&b=2
```

Resposta:

```json
{
  "resultado": 5
}
```

---

## Divisão por zero

```http
GET /dividir?a=10&b=0
```

Resposta:

```json
{
  "erro": "Divisão por zero não é permitida."
}
```

---

## Criação de produto

```http
POST /produtos
```

Body:

```json
{
  "nome": "Camiseta Básica",
  "preco": 29.90,
  "categoria": "vestuario"
}
```

---

# Testes Realizados

## Teste Funcional

Validação das operações matemáticas:
- divisão
- multiplicação
- tratamento de erro

---

## Teste Exploratório

Validação de:
- JSON inválido
- métodos incorretos
- recursos inexistentes

---

## Teste de Regressão

Verificação de que novas funcionalidades não quebraram funcionalidades antigas.

---

## Teste Não Funcional

Análise de:
- tempo de resposta
- estabilidade
- consistência da API

---

# Organização do Projeto

```txt
API-Flask/
│
├── app.py
├── README.md

```

---

# Autor

Desenvolvido por: **Filipe Silva da Fonseca**

Disciplina: Testes de Software / APIs REST

---

# Observações

Este projeto possui finalidade acadêmica e educacional.

As funcionalidades da API foram implementadas manualmente pelo autor. Ferramentas de Inteligência Artificial foram utilizadas como apoio na documentação, comentários explicativos e organização textual do projeto.
