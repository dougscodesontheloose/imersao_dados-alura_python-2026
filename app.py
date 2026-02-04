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

# --- Sistema de Temas ---
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'theme' not in st.session_state:
    st.session_state.theme = 'retrofuturista'

# --- Paletas de Cores por Tema ---
def get_theme_colors(theme, dark_mode):
    themes = {
        'standard': {
            'light': {
                'bg_primary': '#FFFFFF',
                'bg_secondary': '#F8F9FA',
                'accent_1': '#0066CC',
                'accent_2': '#0052A3',
                'accent_3': '#3399FF',
                'accent_4': '#66B2FF',
                'text_primary': '#212529',
                'text_secondary': '#6C757D',
                'grid_color': 'rgba(0, 102, 204, 0.05)',
                'border_color': '#DEE2E6'
            },
            'dark': {
                'bg_primary': '#1A1D23',
                'bg_secondary': '#2C3038',
                'accent_1': '#3399FF',
                'accent_2': '#0066CC',
                'accent_3': '#66B2FF',
                'accent_4': '#99CCFF',
                'text_primary': '#F8F9FA',
                'text_secondary': '#ADB5BD',
                'grid_color': 'rgba(51, 153, 255, 0.08)',
                'border_color': '#495057'
            }
        },
        'retrofuturista': {
            'light': {
                'bg_primary': '#F5F1ED',
                'bg_secondary': '#FFFFFF',
                'accent_1': '#E8A598',
                'accent_2': '#CC8866',
                'accent_3': '#D4A69A',
                'accent_4': '#FFDAB9',
                'text_primary': '#2D2420',
                'text_secondary': '#8B7E74',
                'grid_color': 'rgba(204, 136, 102, 0.03)',
                'border_color': '#D4A69A'
            },
            'dark': {
                'bg_primary': '#1A1512',
                'bg_secondary': '#2D2420',
                'accent_1': '#E8A598',
                'accent_2': '#CC8866',
                'accent_3': '#D4A69A',
                'accent_4': '#FFDAB9',
                'text_primary': '#F5F1ED',
                'text_secondary': '#E5D4CE',
                'grid_color': 'rgba(232, 165, 152, 0.08)',
                'border_color': '#8B7E74'
            }
        },
        'synthwave': {
            'light': {
                'bg_primary': '#FFF5F7',
                'bg_secondary': '#FFFFFF',
                'accent_1': '#FF006E',
                'accent_2': '#8338EC',
                'accent_3': '#3A86FF',
                'accent_4': '#FB5607',
                'text_primary': '#2B2D42',
                'text_secondary': '#8D99AE',
                'grid_color': 'rgba(255, 0, 110, 0.05)',
                'border_color': '#EF476F'
            },
            'dark': {
                'bg_primary': '#0A0E27',
                'bg_secondary': '#1A1F3A',
                'accent_1': '#FF006E',
                'accent_2': '#8338EC',
                'accent_3': '#3A86FF',
                'accent_4': '#FB5607',
                'text_primary': '#F72585',
                'text_secondary': '#B5179E',
                'grid_color': 'rgba(255, 0, 110, 0.12)',
                'border_color': '#7209B7'
            }
        }
    }
    
    mode = 'dark' if dark_mode else 'light'
    return themes[theme][mode]
# compute colors from selected theme and mode
colors = get_theme_colors(st.session_state.theme, st.session_state.dark_mode)

# --- Configurações específicas por tema ---
theme_config = {
    'standard': {
        'font_primary': 'Inter, system-ui, sans-serif',
        'font_mono': 'Roboto Mono, monospace',
        'import': "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&family=Roboto+Mono:wght@400;700&display=swap');",
        'corner_text': '▌ DATA.ANALYTICS',
        'sidebar_prefix': '▸ FILTERS',
        'text_shadow': 'none',
        'neon_effect': ''
    },
    'retrofuturista': {
        'font_primary': 'Rubik, sans-serif',
        'font_mono': 'Space Mono, monospace',
        'import': "@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Rubik:wght@300;500;700&display=swap');",
        'corner_text': '▌ NASA.ANALYTICS.SYS',
        'sidebar_prefix': '▸ SYS.FILTER_MODULE',
        'text_shadow': 'none',
        'neon_effect': ''
    },
    'synthwave': {
        'font_primary': 'Rajdhani, sans-serif',
        'font_mono': 'Share Tech Mono, monospace',
        'import': "@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;500;700&family=Share+Tech+Mono&display=swap');",
        'corner_text': '◢ NEON.DATA.NET ◣',
        'sidebar_prefix': '◢ CTRL.FILTER',
        'text_shadow': 'none',
        'neon_effect': ''
    }
}

# add dynamic synthwave effects now that `colors` and session state exist
if st.session_state.theme == 'synthwave':
    if st.session_state.dark_mode:
        theme_config['synthwave']['text_shadow'] = f"0 0 10px {colors['accent_1']}, 0 0 20px {colors['accent_1']}, 0 0 30px {colors['accent_2']}"
        theme_config['synthwave']['neon_effect'] = f"""
        text-shadow: 0 0 10px {colors['accent_1']}, 0 0 20px {colors['accent_2']};
        animation: neon-flicker 3s infinite alternate;
        """

config = theme_config[st.session_state.theme]

st.markdown(f"""
<style>
    /* Imports */
    {config['import']}
    
    /* Animação neon (synthwave) */
    @keyframes neon-flicker {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.95; }}
    }}
    
    /* Reset e base */
    .stApp {{
        background-color: {colors['bg_primary']};
        font-family: {config['font_primary']};
    }}
    
    /* Grid de fundo tipo wireframe */
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient({colors['grid_color']} 1px, transparent 1px),
            linear-gradient(90deg, {colors['grid_color']} 1px, transparent 1px);
        background-size: 40px 40px;
        pointer-events: none;
        z-index: 0;
    }}
    
    /* Tipografia */
    h1, h2, h3 {{
        font-family: {config['font_mono']};
        color: {colors['text_primary']};
        letter-spacing: -0.02em;
        font-weight: 700;
        text-transform: uppercase;
        {config['neon_effect']}
    }}
    
    h1 {{
        font-size: 2.8rem;
        border-left: 6px solid {colors['accent_2']};
        padding-left: 20px;
        margin-bottom: 10px;
    }}
    
    h2 {{
        font-size: 1.4rem;
        color: {colors['text_secondary']};
        margin-top: 40px;
        margin-bottom: 20px;
        position: relative;
    }}
    
    h2::after {{
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 60px;
        height: 2px;
        background: {colors['accent_1']};
    }}
    
    h3 {{
        font-size: 1rem;
        color: {colors['text_secondary']};
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {colors['bg_secondary']} 0%, {colors['bg_primary']} 100%);
        border-right: 2px solid {colors['border_color']};
        box-shadow: 4px 0 12px rgba(139, 126, 116, 0.15);
    }}
    
    [data-testid="stSidebar"] h2 {{
        color: {colors['text_primary']};
        font-size: 1.1rem;
        padding: 10px;
        background: {colors['accent_1']};
        margin: -10px -10px 20px -10px;
        border-bottom: 2px solid {colors['accent_2']};
    }}
    
    [data-testid="stSidebar"] h2::after {{
        display: none;
    }}
    
    /* Elementos sci-fi na sidebar */
    [data-testid="stSidebar"]::before {{
        content: '{config['sidebar_prefix']}';
        position: absolute;
        top: 60px;
        right: 10px;
        font-family: {config['font_mono']};
        font-size: 0.65rem;
        color: {colors['accent_2']};
        opacity: 0.5;
    }}
    
    /* Multiselect e inputs */
    .stMultiSelect > div > div {{
        background-color: {colors['bg_secondary']};
        border: 2px solid {colors['border_color']} !important;
        border-radius: 0px;
    }}
    
    .stMultiSelect [data-baseweb="tag"] {{
        background-color: {colors['accent_4']};
        color: {colors['text_primary']};
        border-radius: 0px;
        font-family: {config['font_mono']};
        font-size: 0.75rem;
    }}
    
    /* Métricas (KPIs) */
    [data-testid="stMetricValue"] {{
        font-family: {config['font_mono']};
        font-size: 2rem;
        color: {colors['accent_2']};
        font-weight: 700;
        {config['neon_effect']}
    }}
    
    [data-testid="stMetricLabel"] {{
        font-family: {config['font_mono']};
        font-size: 0.8rem;
        color: {colors['text_secondary']};
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    
    [data-testid="metric-container"] {{
        background: {colors['bg_secondary']};
        padding: 20px;
        border: 2px solid {colors['accent_1']};
        border-left: 6px solid {colors['accent_2']};
        box-shadow: 4px 4px 0px {colors['accent_3']};
        position: relative;
    }}
    
    /* Elemento decorativo nos cards */
    [data-testid="metric-container"]::before {{
        content: '◼';
        position: absolute;
        top: 8px;
        right: 8px;
        color: {colors['accent_1']};
        opacity: 0.3;
        font-size: 0.6rem;
    }}
    
    /* Divisores */
    hr {{
        border: none;
        height: 2px;
        background: linear-gradient(90deg, {colors['accent_1']} 0%, transparent 100%);
        margin: 40px 0;
    }}
    
    /* Warnings e alertas */
    .stAlert {{
        background-color: {colors['accent_4']};
        border-left: 4px solid {colors['accent_2']};
        border-radius: 0px;
        color: {colors['text_primary']};
        font-family: {config['font_mono']};
    }}
    
    /* Tabela de dados */
    .dataframe {{
        font-family: {config['font_mono']};
        font-size: 0.85rem;
        border: 2px solid {colors['border_color']} !important;
    }}
    
    .dataframe thead tr th {{
        background-color: {colors['accent_1']} !important;
        color: {colors['text_primary']} !important;
        font-weight: 700;
        border: 1px solid {colors['border_color']} !important;
    }}
    
    .dataframe tbody tr:nth-child(even) {{
        background-color: {colors['bg_secondary']};
    }}
    
    /* Texto descritivo */
    p, .stMarkdown {{
        color: {colors['text_secondary']};
        line-height: 1.6;
    }}
    
    /* Elemento decorativo de canto */
    .corner-element {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        font-family: {config['font_mono']};
        font-size: 0.7rem;
        color: {colors['accent_1']};
        opacity: 0.4;
        z-index: 1000;
        pointer-events: none;
        {config['neon_effect']}
    }}
</style>
<div class="corner-element">{config['corner_text']}</div>
""", unsafe_allow_html=True)

# --- Carregamento dos dados ---
# prefer local file in workspace; fallback to remote if not found
import os
local_csv = "dados-imersao-final.csv"
if os.path.exists(local_csv):
    df = pd.read_csv(local_csv)
else:
    df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")

# Seletor de tema
st.sidebar.markdown("### 🎨 Aparência")
theme_options = {
    'Standard': 'standard',
    'Retrofuturista': 'retrofuturista',
    'Synthwave 80s': 'synthwave'
}
selected_theme = st.sidebar.selectbox(
    "Tema",
    options=list(theme_options.keys()),
    index=list(theme_options.values()).index(st.session_state.theme)
)
if theme_options[selected_theme] != st.session_state.theme:
    st.session_state.theme = theme_options[selected_theme]
    st.rerun()

# Toggle de modo claro/escuro
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("☀️ Claro", use_container_width=True, disabled=not st.session_state.dark_mode):
        st.session_state.dark_mode = False
        st.rerun()
with col2:
    if st.button("🌙 Escuro", use_container_width=True, disabled=st.session_state.dark_mode):
        st.session_state.dark_mode = True
        st.rerun()

st.sidebar.markdown("---")

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
template_custom = {
    'layout': {
        'font': {'family': config['font_mono'], 'color': colors['text_primary']},
        'plot_bgcolor': colors['bg_primary'],
        'paper_bgcolor': colors['bg_secondary'],
        'colorway': [colors['accent_1'], colors['accent_2'], colors['accent_3'], colors['accent_4']],
        'title': {
            'font': {'size': 16, 'color': colors['text_primary'], 'family': config['font_mono']},
            'x': 0.05,
            'xanchor': 'left'
        },
        'xaxis': {
            'gridcolor': colors['grid_color'].replace('0.03', '0.15').replace('0.05', '0.15').replace('0.08', '0.15').replace('0.12', '0.2'),
            'linecolor': colors['border_color'],
            'linewidth': 2,
            'tickfont': {'size': 11}
        },
        'yaxis': {
            'gridcolor': colors['grid_color'].replace('0.03', '0.15').replace('0.05', '0.15').replace('0.08', '0.15').replace('0.12', '0.2'),
            'linecolor': colors['border_color'],
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
            template=template_custom
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
            template=template_custom
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
            template=template_custom,
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
        media_ds_pais = df_ds.groupby('residencia')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(
            media_ds_pais,
            locations='residencia',
            color='usd',
            color_continuous_scale=['#F5F1ED', '#FFDAB9', '#E8A598', '#D4A69A', '#CC8866'],
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia': 'País'},
            template=template_custom
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
