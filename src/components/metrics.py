"""
Componentes da interface Streamlit - Métricas e Validações
"""
import streamlit as st


def render_metrics(total_volume: float, floor_area: float, nhv: float, 
                   nhv_per_person: float, floor_area_per_person: float,
                   crew_size: int, total_water: float, mission_duration: int,
                   min_nhv: float, min_floor_area: float):
    """
    Renderiza os cards de métricas do habitat.
    
    Args:
        total_volume: Volume total (m³)
        floor_area: Área de piso (m²)
        nhv: Net Habitable Volume total (m³)
        nhv_per_person: NHV por pessoa (m³)
        floor_area_per_person: Área por pessoa (m²)
        crew_size: Tamanho da tripulação
        total_water: Água total necessária (litros)
        mission_duration: Duração da missão (dias)
        min_nhv: NHV mínimo NASA (m³)
        min_floor_area: Área mínima NASA (m²)
    """
    st.markdown("## Habitat Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Volume", f"{total_volume:.1f} m³")
        st.metric("Floor Area", f"{floor_area:.1f} m²")
    
    with col2:
        nhv_delta = "normal" if nhv_per_person >= min_nhv else "inverse"
        st.metric("NHV Total", f"{nhv:.1f} m³")
        st.metric("NHV per Person", f"{nhv_per_person:.1f} m³", 
                  delta=f"{nhv_per_person - min_nhv:.1f} vs min",
                  delta_color=nhv_delta)
    
    with col3:
        floor_delta = "normal" if floor_area_per_person >= min_floor_area else "inverse"
        st.metric("Area per Person", f"{floor_area_per_person:.1f} m²",
                  delta=f"{floor_area_per_person - min_floor_area:.1f} vs min",
                  delta_color=floor_delta)
        st.metric("Crew Size", f"{crew_size} persons")
    
    with col4:
        st.metric("Total Water Needed", f"{total_water:.0f} L")
        st.metric("Mission Duration", f"{mission_duration} days")


def render_validation(issues: list):
    """
    Renderiza a seção de validação NASA.
    
    Args:
        issues: Lista de problemas encontrados (vazio se tudo OK)
    """
    st.markdown("---")
    st.markdown("## ✓ NASA Standards Validation")
    
    if issues:
        for issue in issues:
            st.error(f"✗ {issue}")
    else:
        st.success("✓ All critical NASA standards are met!")


def render_zones(zones: dict, floor_area: float, zone_colors: dict, zone_names: dict):
    """
    Renderiza os cards das zonas funcionais.
    
    Args:
        zones: Dicionário com áreas das zonas
        floor_area: Área total de piso (m²)
        zone_colors: Cores das zonas
        zone_names: Nomes das zonas
    """
    st.markdown("---")
    st.markdown("## Functional Zones")
    
    cols = st.columns(3)
    for idx, (zone, area) in enumerate(zones.items()):
        with cols[idx % 3]:
            percentage = (area / floor_area) * 100
            st.markdown(f"""
            <div class='zone-card' style='border-left-color: {zone_colors[zone]};'>
                <div style='color: {zone_colors[zone]}; font-weight: 700; font-size: 1.1rem;'>{zone_names[zone]}</div>
                <div style='color: #E8EAED; font-size: 1.5rem; font-weight: 700; margin: 0.5rem 0;'>{area:.1f} m²</div>
                <div style='color: #A0AEC0;'>{percentage:.1f}% of total floor</div>
            </div>
            """, unsafe_allow_html=True)
