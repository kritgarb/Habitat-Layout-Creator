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
    st.sidebar.markdown("## Configuração")
    st.sidebar.markdown("---")
    
    # Forma do habitat
    shape = st.sidebar.selectbox("Forma do Habitat", ["Cylinder", "Rectangular"])
    
    # Tipo de estrutura (Rígida ou Inflável)
    st.sidebar.markdown("#### Tipo de Estrutura")
    structure_type = st.sidebar.radio(
        "Selecione a Estrutura",
        ["rigid", "inflatable"],
        format_func=lambda x: HABITAT_TYPES[x]["description"],
        help="Estrutura rígida: volume limitado, alta proteção\nInflável: 3-4x maior volume, menor massa"
    )
    
    # Dimensões
    st.sidebar.markdown("#### Dimensões (metros)")
    
    if shape == "Cylinder":
        diameter = st.sidebar.number_input("Diâmetro", min_value=2.0, max_value=15.0, value=6.0, step=0.5)
        height = st.sidebar.number_input("Altura", min_value=2.0, max_value=20.0, value=10.0, step=0.5)
        dimensions = {"diameter": diameter, "height": height, "length": None, "width": None}
    else:
        length = st.sidebar.number_input("Comprimento", min_value=2.0, max_value=20.0, value=10.0, step=0.5)
        width = st.sidebar.number_input("Largura", min_value=2.0, max_value=15.0, value=6.0, step=0.5)
        height = st.sidebar.number_input("Altura", min_value=2.0, max_value=20.0, value=4.0, step=0.5)
        dimensions = {"length": length, "width": width, "height": height, "diameter": width}
    
    # Parâmetros da missão
    st.sidebar.markdown("#### Parâmetros da Missão")
    # Tripulação: mínimo 4, máximo 6 pessoas
    crew_size = st.sidebar.slider("Tamanho da Tripulação", min_value=4, max_value=6, value=4)
    mission_duration = st.sidebar.number_input(
        "Duração da Missão (dias)", 
        min_value=1, 
        max_value=1000, 
        value=180,
        help="Usado para calcular NHV requerido pela fórmula NASA: 6.67 × ln(dias) - 7.79"
    )
    
    # Ambiente gravitacional
    st.sidebar.markdown("#### Ambiente Gravitacional")
    gravity_env = st.sidebar.selectbox(
        "Selecione o Ambiente",
        ["microgravity", "lunar", "mars"],
        format_func=lambda x: GRAVITY_ENVIRONMENTS[x]["description"],
        help="Afeta se volume ou área horizontal é priorizada"
    )
    
    # Seleção de Zonas Funcionais
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### Zonas Funcionais")
    st.sidebar.caption("Selecione zonas para incluir e customize as áreas por pessoa:")
    
    selected_zones = {}
    zone_areas = {}
    
    # Importar constantes de zona
    from ..config.constants import ZONE_MIN_AREA, ZONE_NAMES
    
    for zone_id, zone_name in ZONE_NAMES.items():
        col1, col2 = st.sidebar.columns([3, 2])
        
        with col1:
            # Checkbox para incluir/excluir zona
            include_zone = st.checkbox(
                zone_name,
                value=True,  # Todas selecionadas por padrão
                key=f"zone_{zone_id}"
            )
        
        if include_zone:
            with col2:
                # Input de área por pessoa
                area = st.number_input(
                    "m²/person",
                    min_value=0.5,
                    max_value=20.0,
                    value=ZONE_MIN_AREA[zone_id],
                    step=0.5,
                    key=f"area_{zone_id}",
                    label_visibility="collapsed"
                )
                zone_areas[zone_id] = area
            selected_zones[zone_id] = True
    
    # Mostrar resumo das zonas selecionadas
    if zone_areas:
        total_area_per_person = sum(zone_areas.values())
        st.sidebar.success(f"{len(zone_areas)} zonas selecionadas · {total_area_per_person:.1f} m²/pessoa total")
    else:
        st.sidebar.warning("Nenhuma zona selecionada")
    
    # Mostrar referências de NHV
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### Referência NHV")
    st.sidebar.info(f"""
    **Diretrizes NASA NHV:**
    - 30 dias: {NHV_REFERENCE[30]} m³/pessoa
    - 180 dias: {NHV_REFERENCE[180]} m³/pessoa
    - 365 dias: {NHV_REFERENCE[365]} m³/pessoa
    - 500 dias: {NHV_REFERENCE[500]} m³/pessoa
    """)
    
    # Configurações avançadas
    st.sidebar.markdown("#### Configurações Avançadas")
    usable_factor = st.sidebar.slider(
        "Fator de Volume Utilizável", 
        min_value=0.5, 
        max_value=0.9, 
        value=0.7, 
        step=0.05,
        help="Fração do volume total que é habitável líquido (NHV)"
    )
    
    # Modo de visualização
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### Modo de Visualização")
    view_mode = st.sidebar.radio("Selecione a Vista", ["Planta 2D", "Habitat 3D", "Ambos"], index=2)
    
    return {
        "shape": shape,
        "structure_type": structure_type,
        "dimensions": dimensions,
        "crew_size": crew_size,
        "mission_duration": mission_duration,
        "gravity_env": gravity_env,
        "usable_factor": usable_factor,
        "view_mode": view_mode,
        "selected_zones": selected_zones,
        "zone_areas": zone_areas
    }
