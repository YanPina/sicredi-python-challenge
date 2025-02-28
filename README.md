# Sicredi Python Challenge

## Descrição

Este repositório contém a solução para o desafio técnico de Python para a vaga de **Python Senior** no **Sicredi**.

A solução foi desenvolvida utilizando **Python 3.11** e segue boas práticas de código, incluindo Clean Code, testes unitários e otimização de desempenho. O projeto utiliza **Poetry** para gerenciamento de dependências e **pre-commit hooks** para garantir a qualidade do código.

Além disso, este projeto segue estritamente as melhores práticas de escrita de código Python, cumprindo as conformidades da **PEP8**, **Clean Code** e **TDD**.

## 📦 Configuração do Projeto

### 1️⃣ Instalar Dependências

#### Windows
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

#### Linux e macOS
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Em seguida, instale as dependências:
```bash
poetry install
```

### 2️⃣ Configuração dos Hooks do Pre-Commit

Este projeto utiliza hooks do pre-commit para linting e formatação. Para configurá-los, execute:
```bash
poetry run pre-commit install
```

Para executar os hooks manualmente em todos os arquivos:
```bash
poetry run pre-commit run --all-files
```

Para executar apenas nos arquivos modificados e novos:
```bash
poetry run pre-commit run --files $(git ls-files -m -o)
```

### 📏 Formatação e Linting do Código

Este projeto utiliza várias ferramentas para garantir a qualidade do código:
- **Black**: Formatador de código (`poetry run black .`)
- **Ruff**: Linter e auto-correção (`poetry run ruff .`)
- **isort**: Organização de imports (`poetry run isort .`)
- **mypy**: Verificação de tipos estática (`poetry run mypy .`)

Todos esses processos são executados automaticamente pelos hooks do `pre-commit`.

### 🧪 Executando Testes

Para rodar os testes unitários com pytest:
```bash
poetry run pytest
```

### 🚀 Executando a Aplicação

Para executar todo o projeto e rodar os serviços, basta rodar o seguinte comando:
```bash
poetry run python main.py
```
Isso iniciará os serviços e executará os cálculos de contratos e ordens de transporte de valores, registrando os resultados no log.

## Estrutura do Projeto

```bash
sicredi-python-challenge/
│-- src/                # Código-fonte do projeto
│   │-- core/           # Implementação de configurações do projeto
│   │-- models/         # Modelos Pydantic usados na validação
│   │-- services/       # Implementação dos serviços para os desafios
│-- tests/              # Testes unitários
│-- .gitignore                   # Arquivo de configuração do Git
│-- .pre-commit-config.yaml      # Configuração de pre-commit hooks
│-- Dockerfile                   # Arquivo para criação da imagem Docker
│-- LICENSE                      # Licença do projeto
│-- main.py                      # Arquivo principal para execução dos serviços
│-- poetry.lock                  # Arquivo de controle de dependências do Poetry
│-- pyproject.toml               # Configuração do Poetry
│-- README.md                    # Documentação do projeto
```

## Tecnologias Utilizadas

- **Python 3.11**
- **Poetry** para gerenciamento de pacotes
- **pytest** para testes unitários
- **Ruff, Black, Flake8, isort, mypy** para linting e formatação
- **GitHub Actions** (opcional, para automação de testes e lint)


## Boas Práticas Aplicadas
- **Código Limpo (Clean Code):** Código modular e bem estruturado
- **PEP8:** Seguindo os padrões oficiais da linguagem Python
- **TDD (Test-Driven Development):** Testes unitários desenvolvidos com `pytest`
- **Performance:** Algoritmos eficientes para manipulação de listas
- **Testes Unitários:** Cobertura completa com `pytest`
- **Linting & Formatação:** Garantia de qualidade com `Ruff`, `Black`, `Flake8`, `isort` e `mypy`
- **Documentação:** Explicação detalhada dos desafios e das soluções implementadas

## 📌 Decisões Técnicas e Melhorias Implementadas

### 1️⃣ Padrões de Nomeação e Conformidade com Snake Case
Durante a implementação, identifiquei que o nome do método `get_top_N_open_contracts` não seguia o padrão snake_case do Python. O correto, conforme a PEP8, é `get_top_n_open_contracts`. Fiz essa correção para garantir conformidade com os padrões da linguagem.

### 2️⃣ Implementação de Logs Estruturados
Foi adicionada uma configuração avançada de logging que inclui:
- Nome do arquivo e método que gerou o log.
- Logs detalhados para debugging.
- Registro de requisições e resultados dos serviços.

### 3️⃣ Separação de Responsabilidades
A implementação foi organizada em serviços (`ContractService` e `OrdersService`), garantindo modularidade e fácil manutenção.

### 4️⃣ Testes Abrangentes
Criei testes unitários para cobrir diferentes cenários, garantindo que as regras de negócios fossem corretamente aplicadas.

### 5️⃣ Uso de Estruturas Eficientes
- `get_top_n_open_contracts`: Uso de **heapq.nlargest()** para otimização, resultando na complexidade **O(n log k)**.
- `combine_orders`: Algoritmo de dois ponteiros (`O(n log n)`) para otimização das viagens.

## Autor
[Yan Pina](https://github.com/YanPina)
