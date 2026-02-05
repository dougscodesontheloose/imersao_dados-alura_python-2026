# 📊 Dashboard de Análise Salarial - Área de Dados

Dashboard interativo desenvolvido para a Imersão Dados com Python da Alura, explorando dados salariais na área de tecnologia e dados.

## 🚀 Demo

[Ver Dashboard ao Vivo](https://im-dados-alura-python-2026.streamlit.app/)

## 🎨 Temas Visuais

O dashboard oferece **3 temas distintos**, cada um com modo **claro** e **escuro**:

### Standard
Design profissional e corporativo com azuis clean. Ideal para apresentações formais.
- Fontes: Inter + Roboto Mono
- Paleta: Azuis corporativos (#0066CC, #3399FF)

### Retrofuturista
Estética NASA/Brutalista com tons terrosos e quentes inspirados em design espacial dos anos 70.
- Fontes: Rubik + Space Mono
- Paleta: Coral, terracota, pessego (#E8A598, #CC8866)

### Synthwave 80s
Visual neon cyberpunk com efeitos luminosos animados (modo escuro).
- Fontes: Rajdhani + Share Tech Mono
- Paleta: Rosa neon, roxo, azul elétrico (#FF006E, #8338EC, #3A86FF)
- Efeito especial: Glow animado no modo escuro

## 📈 Funcionalidades

### Filtros Interativos
- **Ano**: Filtre por ano específico ou múltiplos anos
- **Senioridade**: Entry, Mid, Senior, Executive
- **Tipo de Contrato**: Full-time, Part-time, Contract, Freelance
- **Tamanho da Empresa**: Small, Medium, Large

### Métricas em Destaque
- Salário médio (USD)
- Salário máximo (USD)
- Total de registros filtrados
- Cargo mais frequente

### Visualizações

**Top 10 Cargos por Salário Médio**
Gráfico de barras horizontais mostrando as posições mais bem remuneradas.

**Distribuição Salarial**
Histograma da distribuição de salários na base filtrada.

**Proporção de Trabalho Remoto**
Gráfico de pizza mostrando tipos de trabalho (presencial, remoto, híbrido).

**Mapa Global - Data Scientists**
Choropleth exibindo salário médio de cientistas de dados por país.

### Tabela Detalhada
Visualização completa dos dados filtrados com todas as colunas disponíveis.

## 🛠️ Tecnologias

- **Python 3.11**
- **Streamlit** - Framework de dashboard
- **Pandas** - Manipulação de dados
- **Plotly** - Visualizações interativas

## 📦 Instalação Local

```bash
# Clone o repositório
git clone https://github.com/dougscodesontheloose/imersao_dados-alura_python-2026.git
cd imersao_dados-alura_python-2026

# Instale as dependências
pip install -r requirements.txt

# Execute o dashboard
streamlit run app.py
```

## 📋 Requirements

```
streamlit
pandas>=2.0.0
plotly>=5.0.0
```

## 🗂️ Estrutura dos Dados

Dataset contém informações sobre salários na área de dados/tech:

| Coluna | Descrição |
|--------|-----------|
| `ano_trabalho` | Ano do registro |
| `senioridade` | Nível de senioridade (EN, MI, SE, EX) |
| `contrato` | Tipo de contrato (FT, PT, CT, FL) |
| `cargo` | Título da posição |
| `salario` | Salário na moeda original |
| `moeda` | Código da moeda |
| `usd` | Salário convertido para USD |
| `residencia` | País de residência (código ISO) |
| `remoto` | Percentual de trabalho remoto (0-100) |
| `empresa` | País da empresa (código ISO) |
| `tamanho_empresa` | Tamanho da empresa (S, M, L) |
| `ano` | Ano (campo duplicado para facilitar filtros) |

## 🎯 Casos de Uso

- Pesquisa salarial para negociação de oferta
- Análise de tendências de mercado por cargo
- Comparação de remuneração entre países
- Estudo da evolução salarial ao longo dos anos
- Planejamento de carreira baseado em dados

## 🐛 Resolução de Problemas

### Erro ao fazer deploy no Streamlit Cloud

**Problema:** `pandas==1.3.5` não compila no Python 3.13

**Solução:** 
1. Atualize o `requirements.txt` para `pandas>=2.0.0`
2. Crie arquivo `.python-version` com conteúdo `3.11`

### Gráficos não carregam

Verifique se você tem todas as dependências instaladas:
```bash
pip install plotly pandas streamlit
```

## 👨‍💻 Autor

**Doug** - Dashboard desenvolvido para Imersão Dados Alura 2026

## 📄 Licença

Projeto educacional - Alura

## 🙏 Créditos

- Dataset: [AI-Jobs.net Salaries Dataset](https://github.com/vqrca/dashboard_salarios_dados)
- Curso: Imersão Dados com Python - Alura
- Inspiração visual: NASA graphics, Synthwave aesthetics, Brutalist design

---

💡 **Dica:** Experimente alternar entre os temas e modos claro/escuro para encontrar a visualização perfeita para sua apresentação!
