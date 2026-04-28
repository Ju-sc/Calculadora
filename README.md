# Calculadora 
API de calculadora construída com FastAPI. Expõe operações matemáticas via HTTP e inclui um frontend em HTML.
Tecnologias

Python 3 + FastAPI
GitHub Actions (CI/CD)

Instalação
bashpip install fastapi uvicorn
Execução
bashuvicorn main:app --reload
A API estará disponível em http://localhost:8000. A documentação interativa gerada pelo FastAPI fica em http://localhost:8000/docs.
Endpoints
Todos os endpoints aceitam parâmetros via query string e retornam JSON.
MétodoRotaParâmetrosDescriçãoGET/somaa, bSoma dois númerosGET/subtracaoa, bSubtrai b de aGET/multiplicacaoa, bMultiplica dois númerosGET/divisaoa, bDivide a por bGET/exponenciacaoa, bEleva a à potência bGET/raizquadaRetorna a raiz quadrada de a (inteiro)GET/fatorialaRetorna o fatorial de a (inteiro positivo)
Exemplos
GET /soma?a=5&b=3
{"resultado": 8}

GET /divisao?a=10&b=2
{"resultado": 5.0}

GET /fatorial?a=5
{"resultado": 120}
Tratamento de erros
Alguns endpoints retornam 400 em casos inválidos:

/divisao — b = 0
/exponenciacao — a = 0 com expoente negativo
/raizquad — a = 0
/fatorial — a <= 0 ou valor não inteiro

Estrutura do projeto
Calculadora/
├── main.py            # Ponto de entrada da aplicação FastAPI
├── soma.py
├── sub.py
├── multi.py
├── divi.py
├── expo.py
├── raiz.py
├── fato.py
└── CI/
    ├── tests.sh                  # Script de testes
    └── auto_release_ignore.txt   # Arquivos excluidos do artefato de release
CI/CD
O projeto usa três workflows do GitHub Actions:

save_dev.yml — executa os testes a cada pull request aberto para a branch dev
save_main.yml — bloqueia pull requests para main que não venham da branch dev
auto_release.yml — gera uma release automaticamente a cada push na main, com o artefato calc_exp.zip e versão baseada em timestamp

Fluxo de branches
feature/* --> dev --> main
PRs diretos para main sem passar por dev são rejeitados pelo workflow.