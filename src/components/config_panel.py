"""
Painel de configuração reutilizável para cada página
"""
import streamlit as st
from ..config.constants import GRAVITY_ENVIRONMENTS, HABITAT_TYPES, NHV_REFERENCE, ZONE_MIN_AREA, ZONE_NAMES


def render_config_panel():
    """
    Renderiza o painel de configuração do habitat.
    
    Returns:
        Dicionário com todas as configurações selecionadas
    """
    st.markdown("### Configuração do Habitat")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Forma e Estrutura")
        shape = st.selectbox("Forma do Habitat", ["Cylinder", "Rectangular"], key="shape")
        structure_type = st.radio(
            "Tipo de Estrutura",
            ["rigid", "inflatable"],
            format_func=lambda x: HABITAT_TYPES[x]["description"],
            help="Estrutura rígida: volume limitado, alta proteção\nInflável: 3-4x maior volume, menor massa",
            key="structure"
        )
        
    with col2:
        st.markdown("#### Parâmetros da Missão")
        crew_size = st.slider("Tamanho da Tripulação", min_value=2, max_value=8, value=4, key="crew")
        mission_duration = st.number_input(
            "Duração da Missão (dias)", 
            min_value=1, 
            max_value=1000, 
            value=180,
            help="Usado para calcular NHV requerido pela fórmula NASA: 6.67 × ln(dias) - 7.79",
            key="duration"
        )
        gravity_env = st.selectbox(
            "Ambiente Gravitacional",
            ["microgravity", "lunar", "mars"],
            format_func=lambda x: GRAVITY_ENVIRONMENTS[x]["description"],
            help="Afeta se volume ou área horizontal é priorizada",
            key="gravity"
        )
    
    st.markdown("#### Dimensões (metros)")
    dim_col1, dim_col2, dim_col3 = st.columns(3)
    
    if shape == "Cylinder":
        with dim_col1:
            diameter = st.number_input("Diâmetro", min_value=2.0, max_value=15.0, value=6.0, step=0.5, key="diameter")
        with dim_col2:
            height = st.number_input("Altura", min_value=2.0, max_value=20.0, value=10.0, step=0.5, key="height")
        dimensions = {"diameter": diameter, "height": height, "length": None, "width": None}
    else:
        with dim_col1:
            length = st.number_input("Comprimento", min_value=2.0, max_value=20.0, value=10.0, step=0.5, key="length")
        with dim_col2:
            width = st.number_input("Largura", min_value=2.0, max_value=15.0, value=6.0, step=0.5, key="width")
        with dim_col3:
            height = st.number_input("Altura", min_value=2.0, max_value=20.0, value=4.0, step=0.5, key="height")
        dimensions = {"length": length, "width": width, "height": height, "diameter": width}
    
    st.markdown("---")
    st.markdown("#### Zonas Funcionais")
    st.caption("Selecione zonas para incluir e customize as áreas por pessoa:")
    
    zone_cols = st.columns(3)
    zone_areas = {}
    
    for idx, (zone_id, zone_name) in enumerate(ZONE_NAMES.items()):
        with zone_cols[idx % 3]:
            include_zone = st.checkbox(
                zone_name,
                value=True,
                key=f"zone_{zone_id}"
            )
            if include_zone:
                area = st.number_input(
                    "m²/pessoa",
                    min_value=0.5,
                    max_value=20.0,
                    value=ZONE_MIN_AREA[zone_id],
                    step=0.5,
                    key=f"area_{zone_id}"
                )
                zone_areas[zone_id] = area
    
    # Mostrar resumo
    if zone_areas:
        total_area_per_person = sum(zone_areas.values())
        st.success(f"{len(zone_areas)} zonas selecionadas · {total_area_per_person:.1f} m²/pessoa total")
    else:
        st.warning("Nenhuma zona selecionada")
    
    st.markdown("---")
    
    adv_col1, adv_col2 = st.columns(2)
    with adv_col1:
        usable_factor = st.slider(
            "Fator de Volume Utilizável", 
            min_value=0.5, 
            max_value=0.9, 
            value=0.7, 
            step=0.05,
            help="Fração do volume total que é habitável líquido (NHV)",
            key="usable"
        )
    
    with adv_col2:
        st.markdown("**Referência NHV NASA:**")
        st.caption(f"""
        - 30 dias: {NHV_REFERENCE[30]} m³/pessoa
        - 180 dias: {NHV_REFERENCE[180]} m³/pessoa
        - 365 dias: {NHV_REFERENCE[365]} m³/pessoa
        """)
    
    return {
        "shape": shape,
        "structure_type": structure_type,
        "dimensions": dimensions,
        "crew_size": crew_size,
        "mission_duration": mission_duration,
        "gravity_env": gravity_env,
        "usable_factor": usable_factor,
        "zone_areas": zone_areas
    }
