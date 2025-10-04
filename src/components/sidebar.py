"""
Componentes da interface Streamlit - Sidebar
"""
import streamlit as st
from ..config.constants import GRAVITY_ENVIRONMENTS, HABITAT_TYPES, NHV_REFERENCE


def render_sidebar():
    """
    Renderiza a sidebar com todos os inputs de configuração.
    
    Returns:
        Dicionário com todas as configurações selecionadas
    """
    st.sidebar.markdown("## Configuration")
    st.sidebar.markdown("---")
    
    # Forma do habitat
    shape = st.sidebar.selectbox("Habitat Shape", ["Cylinder", "Rectangular"])
    
    # Tipo de estrutura (Rígida ou Inflável)
    st.sidebar.markdown("#### Structure Type")
    structure_type = st.sidebar.radio(
        "Select Structure",
        ["rigid", "inflatable"],
        format_func=lambda x: HABITAT_TYPES[x]["description"],
        help="Estrutura rígida: volume limitado, alta proteção\nInflável: 3-4x maior volume, menor massa"
    )
    
    # Dimensões
    st.sidebar.markdown("#### Dimensions (meters)")
    
    if shape == "Cylinder":
        diameter = st.sidebar.number_input("Diameter", min_value=2.0, max_value=15.0, value=6.0, step=0.5)
        height = st.sidebar.number_input("Height", min_value=2.0, max_value=20.0, value=10.0, step=0.5)
        dimensions = {"diameter": diameter, "height": height, "length": None, "width": None}
    else:
        length = st.sidebar.number_input("Length", min_value=2.0, max_value=20.0, value=10.0, step=0.5)
        width = st.sidebar.number_input("Width", min_value=2.0, max_value=15.0, value=6.0, step=0.5)
        height = st.sidebar.number_input("Height", min_value=2.0, max_value=20.0, value=4.0, step=0.5)
        dimensions = {"length": length, "width": width, "height": height, "diameter": width}
    
    # Parâmetros da missão
    st.sidebar.markdown("#### Mission Parameters")
    crew_size = st.sidebar.slider("Crew Size", min_value=2, max_value=8, value=4)
    mission_duration = st.sidebar.number_input(
        "Mission Duration (days)", 
        min_value=1, 
        max_value=1000, 
        value=180,
        help="Usado para calcular NHV requerido pela fórmula NASA: 6.67 × ln(dias) - 7.79"
    )
    
    # Ambiente gravitacional
    st.sidebar.markdown("#### Gravity Environment")
    gravity_env = st.sidebar.selectbox(
        "Select Environment",
        ["microgravity", "lunar", "mars"],
        format_func=lambda x: GRAVITY_ENVIRONMENTS[x]["description"],
        help="Afeta se volume ou área horizontal é priorizada"
    )
    
    # Mostrar referências de NHV
    st.sidebar.markdown("#### NHV Reference")
    st.sidebar.info(f"""
    **NASA NHV Guidelines:**
    - 30 days: {NHV_REFERENCE[30]} m³/person
    - 180 days: {NHV_REFERENCE[180]} m³/person
    - 365 days: {NHV_REFERENCE[365]} m³/person
    - 500 days: {NHV_REFERENCE[500]} m³/person
    """)
    
    # Configurações avançadas
    st.sidebar.markdown("#### Advanced Settings")
    usable_factor = st.sidebar.slider(
        "Usable Volume Factor", 
        min_value=0.5, 
        max_value=0.9, 
        value=0.7, 
        step=0.05,
        help="Fração do volume total que é habitável líquido (NHV)"
    )
    
    # Modo de visualização
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### Visualization Mode")
    view_mode = st.sidebar.radio("Select View", ["2D Floor Plan", "3D Habitat", "Both"], index=2)
    
    return {
        "shape": shape,
        "structure_type": structure_type,
        "dimensions": dimensions,
        "crew_size": crew_size,
        "mission_duration": mission_duration,
        "gravity_env": gravity_env,
        "usable_factor": usable_factor,
        "view_mode": view_mode
    }
