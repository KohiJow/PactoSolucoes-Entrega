# Testes Automatizados - Pacto Soluções

Testes E2E em **Playwright** (Python) e **Cypress** (JavaScript) para validação de busca e termos de uso.

## Requisitos
- Python 3.12+
- Node.js 18+

## Atividades

### Atividade 1: Busca no Yahoo
Valida busca por "Pacto Soluções" no Yahoo BR
- Verifica resultados da busca
- Valida URL de resultados
- Confirma presença do termo

### Atividade 2: Termos de Uso UOL
Captura data de última atualização dos Termos de Uso da UOL
- Acessa página de termos
- Extrai data do campo `dateModified`
- Exibe data formatada

## Setup Playwright
```bash
# Instalar dependências
pip install playwright pytest-playwright

# Instalar navegadores
playwright install
```

## Rodar Playwright
```bash
# Executar todos os testes
pytest -v -s

# Executar teste específico do Yahoo
pytest -v -s test_yahoo.py

# Executar teste específico da UOL
pytest -v -s test_uol_playwright.py

# Modo headed (visualizar navegador)
pytest -v -s --headed --browser chromium
```

## Setup Cypress
```bash
# Inicializar projeto Node
npm init -y

# Instalar Cypress
npm install cypress --save-dev
```

## Rodar Cypress
```bash
# Abrir interface gráfica
npx cypress open

# Executar via linha de comando
npx cypress run

# Executar teste específico do Yahoo
npx cypress run --spec "cypress/e2e/yahoo.cy.js"

# Executar teste específico da UOL
npx cypress run --spec "cypress/e2e/uol.cy.js"
```

## Estrutura do Projeto
```
Playwright_2/
├── test_yahoo.py              # Teste Yahoo - Playwright
├── test_uol_playwright.py     # Teste UOL - Playwright
├── cypress/
│   └── e2e/
│       ├── yahoo.cy.js        # Teste Yahoo - Cypress
│       └── uol.cy.js          # Teste UOL - Cypress
├── cypress.config.js          # Configuração Cypress
└── README.md                  # Este arquivo
```

## Resultados Esperados

### Teste Yahoo
```
Validando busca por "Pacto Soluções"
URL: https://br.search.yahoo.com/...
Resultados encontrados: OK
```

### Teste UOL
```
============================================================
DATA DE ATUALIZACAO DOS TERMOS DE USO DA UOL
============================================================
Data encontrada: 2025-03-17T17:20:49-03:00
============================================================
```

## Troubleshooting

### Timeout no teste da UOL
Se o teste falhar com timeout, execute em modo headed:
```bash
pytest -v -s test_uol_playwright.py --headed
```

### Cypress não encontra arquivos
Certifique-se de que os arquivos estão em `cypress/e2e/`

## Entrega

Repositório: https://github.com/Kohijow/PactoSolucoes-Entrega

Enviar para:
- rh@pactosolucoes.com.br
- tiagosantana@pactosolucoes.com.br