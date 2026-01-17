# Teste Automatizado: Yahoo Busca "Pacto Soluções"

Teste E2E em **Playwright** (Python) e **Cypress** (JS) validando busca no Yahoo BR.

## Requisitos
- Python 3.12+
- Node.js 18+ (para Cypress)

##  Setup Playwright
```bash
pip install playwright pytest-playwright
playwright install

##  Rodar Playwright
pytest --browser chromium -v -s

##  Setup Cypress
npm init -y
npm i cypress --save-dev
npx cypress open

##  Rodar Cypress
pytest --browser chromium -v -s
npx cypress run