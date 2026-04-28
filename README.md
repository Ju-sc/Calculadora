# Calculadora

## 1. Introdução

Este projeto consiste em uma API de calculadora desenvolvida inteiramente em Python utilizando o framework FastAPI. A aplicação expõe operações matemáticas através de endpoints HTTP e foi estruturada de forma modular, com cada operação encapsulada em seu próprio arquivo. O objetivo é demonstrar a construção de uma API REST organizada, com tratamento de erros e integração contínua via GitHub Actions.

## 2. Propósito

O principal propósito deste projeto é servir como exercício prático de programação, explorando conceitos como criação de APIs REST com FastAPI, organização modular de código Python, roteamento com `APIRouter`, tratamento de entradas inválidas com respostas HTTP adequadas e automação de testes e releases com GitHub Actions. O projeto também serve para consolidar o conhecimento dos autores em desenvolvimento de APIs e boas práticas de versionamento.

### Funcionalidades

A API oferece sete operações matemáticas, cada uma em um módulo independente:

- Soma de dois números (`/soma`)
- Subtração de dois números (`/subtracao`)
- Multiplicação de dois números (`/multiplicacao`)
- Divisão de dois números, com tratamento de divisão por zero (`/divisao`)
- Exponenciação, com validação de base zero e expoente negativo (`/exponenciacao`)
- Raiz quadrada, retornando o resultado como inteiro (`/raizquad`)
- Fatorial, aceitando apenas inteiros positivos (`/fatorial`)

Todos os endpoints retornam JSON e aceitam parâmetros via query string. Em casos de entrada inválida, a API retorna status `400` com uma mensagem de erro descritiva.

### Endpoints

| Método | Rota | Parâmetros | Descrição |
|--------|------|------------|-----------|
| GET | `/soma` | `a`, `b` | Soma dois números |
| GET | `/subtracao` | `a`, `b` | Subtrai `b` de `a` |
| GET | `/multiplicacao` | `a`, `b` | Multiplica dois números |
| GET | `/divisao` | `a`, `b` | Divide `a` por `b` |
| GET | `/exponenciacao` | `a`, `b` | Eleva `a` à potência `b` |
| GET | `/raizquad` | `a` | Raiz quadrada de `a` |
| GET | `/fatorial` | `a` | Fatorial de `a` (inteiro positivo) |

Exemplos de uso:

```
GET /soma?a=5&b=3          → {"resultado": 8}
GET /divisao?a=10&b=2      → {"resultado": 5.0}
GET /fatorial?a=5          → {"resultado": 120}
GET /divisao?a=10&b=0      → 400 {"erro": "Não é possível dividir por 0"}
```

## 3. Como Usar

### 3.1 Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina. Em seguida, instale as dependências necessárias via pip:

```bash
pip install fastapi uvicorn
```

### 3.2 Executando a API

Clone ou baixe o repositório e, no terminal, navegue até a pasta do projeto e execute:

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`. O FastAPI gera automaticamente uma documentação interativa acessível em `http://localhost:8000/docs`, onde é possível testar todos os endpoints diretamente pelo navegador.

## 4. Estrutura do Projeto

```
Calculadora/
├── main.py            # Ponto de entrada — inicializa o app e registra os roteadores
├── soma.py            # Endpoint /soma
├── sub.py             # Endpoint /subtracao
├── multi.py           # Endpoint /multiplicacao
├── divi.py            # Endpoint /divisao
├── expo.py            # Endpoint /exponenciacao
├── raiz.py            # Endpoint /raizquad
├── fato.py            # Endpoint /fatorial
└── CI/
    ├── tests.sh                  # Script de testes executado no pipeline
    └── auto_release_ignore.txt   # Arquivos excluidos do artefato de release
```

## 5. CI/CD

O projeto utiliza três workflows do GitHub Actions para automatizar o ciclo de desenvolvimento:

- **save_dev.yml** — executa os testes a cada pull request aberto para a branch `dev`, impedindo que código com falhas avance no fluxo.
- **save_main.yml** — bloqueia pull requests para `main` que não se originem da branch `dev`, garantindo que todo código passe pela etapa de validação antes de chegar à produção.
- **auto_release.yml** — a cada push na `main`, gera automaticamente uma release no GitHub com o artefato `calc_exp.zip` e versão baseada em timestamp.

O fluxo de branches segue a seguinte hierarquia:

```
feature/* --> dev --> main
```

Pull requests diretos para `main` fora desse fluxo são automaticamente rejeitados pelo pipeline.
