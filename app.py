import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard do Doug pra Imersão ALura / Dados com Python",
    page_icon="📊",
    layout="wide",
)

# --- ESTÉTICA NASAPUNK/BRUTALISTA ---
st.markdown("""
<style>
    /* Imports */
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Rubik:wght@300;500;700&display=swap');
    
    /* Paleta de cores quentes pastéis */
    :root {
        --coral-desbotado: #E8A598;
        --pessego: #FFDAB9;
        --terracota: #D4A69A;
        --bege-rosado: #E5D4CE;
        --laranja-queimado: #CC8866;
        --cinza-quente: #8B7E74;
        --off-white: #F5F1ED;
        --preto-suave: #2D2420;
    }
    
    /* Reset e base */
    .stApp {
        background-color: var(--off-white);
        font-family: 'Rubik', sans-serif;
    }
    
    /* Grid de fundo tipo wireframe */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(204, 136, 102, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(204, 136, 102, 0.03) 1px, transparent 1px);
        background-size: 40px 40px;
        pointer-events: none;
        z-index: 0;
    }
    
    /* Tipografia */
    h1, h2, h3 {
        font-family: 'Space Mono', monospace;
        color: var(--preto-suave);
        letter-spacing: -0.02em;
        font-weight: 700;
        text-transform: uppercase;
    }
    
    h1 {
        font-size: 2.8rem;
        border-left: 6px solid var(--laranja-queimado);
        padding-left: 20px;
        margin-bottom: 10px;
    }
    
    h2 {
        font-size: 1.4rem;
        color: var(--cinza-quente);
        margin-top: 40px;
        margin-bottom: 20px;
        position: relative;
    }
    
    h2::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 60px;
        height: 2px;
        background: var(--coral-desbotado);
    }
    
    h3 {
        font-size: 1rem;
        color: var(--cinza-quente);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--bege-rosado) 0%, var(--off-white) 100%);
        border-right: 2px solid var(--terracota);
        box-shadow: 4px 0 12px rgba(139, 126, 116, 0.08);
    }
    
    [data-testid="stSidebar"] h2 {
        color: var(--preto-suave);
        font-size: 1.1rem;
        padding: 10px;
        background: var(--coral-desbotado);
        margin: -10px -10px 20px -10px;
        border-bottom: 2px solid var(--laranja-queimado);
    }
    
    [data-testid="stSidebar"] h2::after {
        display: none;
    }
    
    /* Elementos sci-fi na sidebar */
    [data-testid="stSidebar"]::before {
        content: '▸ SYS.FILTER_MODULE';
        position: absolute;
        top: 60px;
        right: 10px;
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        color: var(--laranja-queimado);
        opacity: 0.5;
    }
    
    /* Multiselect e inputs */
    .stMultiSelect > div > div {
        background-color: white;
        border: 2px solid var(--terracota) !important;
        border-radius: 0px;
    }
    
    .stMultiSelect [data-baseweb="tag"] {
        background-color: var(--pessego);
        color: var(--preto-suave);
        border-radius: 0px;
        font-family: 'Space Mono', monospace;
        font-size: 0.75rem;
    }
    
    /* Métricas (KPIs) */
    [data-testid="stMetricValue"] {
        font-family: 'Space Mono', monospace;
        font-size: 2rem;
        color: var(--laranja-queimado);
        font-weight: 700;
    }
    
    [data-testid="stMetricLabel"] {
        font-family: 'Space Mono', monospace;
        font-size: 0.8rem;
        color: var(--cinza-quente);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    [data-testid="metric-container"] {
        background: white;
        padding: 20px;
        border: 2px solid var(--coral-desbotado);
        border-left: 6px solid var(--laranja-queimado);
        box-shadow: 4px 4px 0px var(--bege-rosado);
        position: relative;
    }
    
    /* Elemento decorativo nos cards */
    [data-testid="metric-container"]::before {
        content: '◼';
        position: absolute;
        top: 8px;
        right: 8px;
        color: var(--coral-desbotado);
        opacity: 0.3;
        font-size: 0.6rem;
    }
    
    /* Divisores */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, var(--coral-desbotado) 0%, transparent 100%);
        margin: 40px 0;
    }
    
    /* Warnings e alertas */
    .stAlert {
        background-color: var(--pessego);
        border-left: 4px solid var(--laranja-queimado);
        border-radius: 0px;
        color: var(--preto-suave);
        font-family: 'Space Mono', monospace;
    }
    
    /* Tabela de dados */
    .dataframe {
        font-family: 'Space Mono', monospace;
        font-size: 0.85rem;
        border: 2px solid var(--terracota) !important;
    }
    
    .dataframe thead tr th {
        background-color: var(--coral-desbotado) !important;
        color: var(--preto-suave) !important;
        font-weight: 700;
        border: 1px solid var(--terracota) !important;
    }
    
    .dataframe tbody tr:nth-child(even) {
        background-color: var(--off-white);
    }
    
    /* Texto descritivo */
    p, .stMarkdown {
        color: var(--cinza-quente);
        line-height: 1.6;
    }
    
    /* Elemento decorativo de canto */
    .corner-element {
        position: fixed;
        bottom: 20px;
        right: 20px;
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        color: var(--coral-desbotado);
        opacity: 0.4;
        z-index: 1000;
        pointer-events: none;
    }
</style>
<div class="corner-element">█ NASA.ANALYTICS.SYS</div>
""", unsafe_allow_html=True)

# --- Carregamento dos dados ---
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")

# Filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

# Filtro de Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

# Filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

# --- Filtragem do DataFrame ---
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard do Doug pra Imersão ALura / Dados com Python")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

# --- Tema customizado para gráficos Plotly ---
template_nasapunk = {
    'layout': {
        'font': {'family': 'Space Mono, monospace', 'color': '#2D2420'},
        'plot_bgcolor': '#F5F1ED',
        'paper_bgcolor': 'white',
        'colorway': ['#E8A598', '#CC8866', '#D4A69A', '#FFDAB9', '#8B7E74'],
        'title': {
            'font': {'size': 16, 'color': '#2D2420', 'family': 'Space Mono, monospace'},
            'x': 0.05,
            'xanchor': 'left'
        },
        'xaxis': {
            'gridcolor': 'rgba(204, 136, 102, 0.2)',
            'linecolor': '#D4A69A',
            'linewidth': 2,
            'tickfont': {'size': 11}
        },
        'yaxis': {
            'gridcolor': 'rgba(204, 136, 102, 0.2)',
            'linecolor': '#D4A69A',
            'linewidth': 2,
            'tickfont': {'size': 11}
        }
    }
}

# --- Análises Visuais com Plotly ---
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''},
            template=template_nasapunk
        )
        grafico_cargos.update_traces(marker_color='#E8A598', marker_line_color='#CC8866', marker_line_width=2)
        grafico_cargos.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''},
            template=template_nasapunk
        )
        grafico_hist.update_traces(marker_color='#D4A69A', marker_line_color='#CC8866', marker_line_width=2)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5,
            template=template_nasapunk,
            color_discrete_sequence=['#E8A598', '#FFDAB9', '#D4A69A', '#CC8866']
        )
        grafico_remoto.update_traces(
            textinfo='percent+label',
            textfont_size=12,
            marker=dict(line=dict(color='#CC8866', width=2))
        )
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(
            media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale=['#F5F1ED', '#FFDAB9', '#E8A598', '#D4A69A', '#CC8866'],
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'},
            template=template_nasapunk
        )
        grafico_paises.update_geos(
            bgcolor='#F5F1ED',
            showcountries=True,
            countrycolor='#D4A69A',
            countrywidth=1
        )
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.") 

# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)