import streamlit as st
from src.config.styles import CUSTOM_CSS
from src.pages.home import render_home_page
from src.pages.layout_2d import render_layout_2d_page
from src.pages.layout_3d import render_layout_3d_page
from src.pages.metrics import render_metrics_page
from src.pages.documentation import render_documentation_page
from src.pages.about import render_about_page

st.set_page_config(
    page_title="AEGIS - NASA Space Apps 2025",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Inicializar estado da página
if 'page' not in st.session_state:
    st.session_state.page = 'Início'

# Header com Logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("src/logo/AEGIS LOGO BRANCO.svg")

st.markdown("""
<div style='text-align: center; padding: 0.5rem 0 0.5rem 0;'>
    <p style='font-size: 1.2rem; color: #A0AEC0; font-weight: 500;'>Sua Casa no Espaço: O Criador de Layout de Habitat - NASA Space Apps Challenge 2025</p>
</div>
""", unsafe_allow_html=True)

# Menu de Navegação Horizontal
st.markdown("---")
menu_col1, menu_col2, menu_col3, menu_col4, menu_col5, menu_col6 = st.columns(6)

with menu_col1:
    if st.button("Início", use_container_width=True, type="primary" if st.session_state.page == 'Início' else "secondary"):
        st.session_state.page = 'Início'
        st.rerun()

with menu_col2:
    if st.button("Layout 2D", use_container_width=True, type="primary" if st.session_state.page == 'Layout 2D' else "secondary"):
        st.session_state.page = 'Layout 2D'
        st.rerun()

with menu_col3:
    if st.button("Layout 3D", use_container_width=True, type="primary" if st.session_state.page == 'Layout 3D' else "secondary"):
        st.session_state.page = 'Layout 3D'
        st.rerun()

with menu_col4:
    if st.button("Métricas NASA", use_container_width=True, type="primary" if st.session_state.page == 'Métricas NASA' else "secondary"):
        st.session_state.page = 'Métricas NASA'
        st.rerun()

with menu_col5:
    if st.button("Documentação", use_container_width=True, type="primary" if st.session_state.page == 'Documentação' else "secondary"):
        st.session_state.page = 'Documentação'
        st.rerun()

with menu_col6:
    if st.button("Sobre", use_container_width=True, type="primary" if st.session_state.page == 'Sobre' else "secondary"):
        st.session_state.page = 'Sobre'
        st.rerun()

st.markdown("---")

# Roteamento de páginas
if st.session_state.page == 'Início':
    render_home_page()

elif st.session_state.page == 'Layout 2D':
    render_layout_2d_page()

elif st.session_state.page == 'Layout 3D':
    render_layout_3d_page()

elif st.session_state.page == 'Métricas NASA':
    render_metrics_page()

elif st.session_state.page == 'Documentação':
    render_documentation_page()

elif st.session_state.page == 'Sobre':
    render_about_page()

# Footer (em todas as páginas)
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 0; color: #718096;'>
    <p style='font-size: 1.1rem; font-weight: 600;'>AEGIS made by ENTERPRISE</p>
    <p style='font-size: 0.9rem;'>Your Home in Space: The Habitat Layout Creator - NASA Space Apps Challenge 2025</p>
</div>
""", unsafe_allow_html=True)
