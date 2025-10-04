import streamlit as st
from src.config.constants import (
    MIN_NHV_PER_PERSON, MIN_FLOOR_AREA_PER_PERSON,
    ZONE_COLORS, ZONE_NAMES, ZONE_MIN_AREA
)
from src.config.styles import CUSTOM_CSS
from src.utils.calculations import (
    calculate_cylinder_volume, calculate_cylinder_floor_area,
    calculate_box_volume, calculate_box_floor_area,
    calculate_nhv, allocate_zones
)
from src.utils.validators import validate_nasa_standards
from src.utils.nasa_calculations import (
    calculate_nhv_per_person,
    calculate_mission_resources,
    calculate_gravity_adjusted_metrics,
    validate_zone_compatibility,
    calculate_storage_volume,
    generate_layout_recommendations
)
from src.visualizations.layout_2d import create_2d_layout_plotly
from src.visualizations.layout_3d import create_3d_habitat_view
from src.components.sidebar import render_sidebar
from src.components.metrics import render_metrics, render_validation, render_zones
from src.components.export import render_export, create_habitat_data_dict

st.set_page_config(
    page_title="AEGIS - NASA Space Apps 2025",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Header com Logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("src/logo/AEGIS LOGO BRANCO.svg")

st.markdown("""
<div style='text-align: center; padding: 0.5rem 0 1rem 0;'>
    <p style='font-size: 1.2rem; color: #A0AEC0; font-weight: 500;'>Your Home in Space: The Habitat Layout Creator - NASA Space Apps Challenge 2025</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - Inputs de configuração
config = render_sidebar()

# Cálculos principais
if config["shape"] == "Cylinder":
    total_volume = calculate_cylinder_volume(
        config["dimensions"]["diameter"], 
        config["dimensions"]["height"]
    )
    floor_area = calculate_cylinder_floor_area(
        config["dimensions"]["diameter"], 
        config["dimensions"]["height"]
    )
else:
    total_volume = calculate_box_volume(
        config["dimensions"]["length"], 
        config["dimensions"]["width"], 
        config["dimensions"]["height"]
    )
    floor_area = calculate_box_floor_area(
        config["dimensions"]["length"], 
        config["dimensions"]["width"]
    )

nhv = calculate_nhv(total_volume, config["usable_factor"])
nhv_per_person = nhv / config["crew_size"]
floor_area_per_person = floor_area / config["crew_size"]

# Cálculos NASA quantitativos
nhv_required_per_person = calculate_nhv_per_person(config["mission_duration"])
mission_resources = calculate_mission_resources(config["crew_size"], config["mission_duration"])
gravity_metrics = calculate_gravity_adjusted_metrics(nhv, floor_area, config["gravity_env"])
storage_requirements = calculate_storage_volume(config["crew_size"], config["mission_duration"])
layout_recommendations = generate_layout_recommendations(
    config["crew_size"], 
    config["mission_duration"],
    config["gravity_env"],
    config["structure_type"]
)

total_water = mission_resources["total_mission"]["water_potable_kg"] + \
              mission_resources["total_mission"]["water_food_prep_kg"]

zones = allocate_zones(floor_area, config["crew_size"], ZONE_MIN_AREA)

# Validação de compatibilidade de zonas (simplificada - sem posições específicas)
# A validação completa de adjacência requer layout 2D gerado
zone_conflicts = []  # Vazio por enquanto, pode ser expandido quando layout 2D tiver posições

# Validação NASA
is_valid, issues = validate_nasa_standards(
    nhv_per_person, 
    floor_area_per_person,
    nhv_required_per_person,  # Usa NHV calculado pela fórmula NASA
    MIN_FLOOR_AREA_PER_PERSON
)

# Adiciona conflitos de zona aos issues
for conflict in zone_conflicts:
    issues.append(f" {conflict['type'].upper()}: {conflict['zone1']} <-> {conflict['zone2']} - {conflict['reason']}")

# Renderizar métricas aprimoradas
render_metrics(
    total_volume, floor_area, nhv, nhv_per_person, floor_area_per_person,
    config["crew_size"], total_water, config["mission_duration"],
    nhv_required_per_person, MIN_FLOOR_AREA_PER_PERSON
)

# Renderizar validação
render_validation(issues)

# Dashboard de Métricas NASA Quantitativas
st.markdown("---")
st.markdown("## NASA Quantitative Metrics Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### NHV Calculation")
    st.markdown(f"""
    **Formula:** `NHV = 6.67 × ln({config["mission_duration"]}) - 7.79`
    
    - **Required NHV/person:** {nhv_required_per_person:.2f} m³
    - **Actual NHV/person:** {nhv_per_person:.2f} m³
    - **Status:** {"Adequate" if nhv_per_person >= nhv_required_per_person else "❌ Insufficient"}
    """)
    
    st.markdown("### Gravity Environment")
    st.markdown(f"""
    **Environment:** {gravity_metrics["primary_metric"].upper()} Priority
    
    - Restraints Required: {"Yes" if gravity_metrics["restraints_required"] else "No"}
    - Use Ceiling/Walls: {"Yes" if gravity_metrics["use_ceiling_walls"] else "No"}
    - Habitability Score: {gravity_metrics["habitability_score"]:.1f}
    """)

with col2:
    st.markdown("##  Life Support (Daily)")
    st.markdown(f"""
    **Per Crew:**
    
    - Water (potable): {mission_resources["daily"]["water_potable_kg"]:.2f} kg/day
    - Water (food prep): {mission_resources["daily"]["water_food_prep_kg"]:.2f} kg/day
    - O₂ consumption: {mission_resources["daily"]["oxygen_kg"]:.2f} kg/day
    - CO₂ production: {mission_resources["daily"]["co2_produced_kg"]:.2f} kg/day
    - Food: {mission_resources["daily"]["food_kg"]:.2f} kg/day
    """)

with col3:
    st.markdown("### Storage Requirements")
    st.markdown(f"""
    **Total Mission:**
    
    - Water storage: {storage_requirements["water_storage_m3"]:.2f} m³
    - Food storage: {storage_requirements["food_storage_m3"]:.2f} m³
    - Equipment: {storage_requirements["equipment_storage_m3"]:.2f} m³
    - **Total:** {storage_requirements["total_storage_m3"]:.2f} m³
    
    BPC Area: {mission_resources["bpc_requirements"]["area_m2"]:.1f} m²
    """)

# Recomendações de Layout
st.markdown("### Layout Recommendations (NASA HIDH)")

rec_col1, rec_col2 = st.columns(2)

with rec_col1:
    st.markdown("#### Required Adjacencies")
    st.markdown("""
    - **Sleep ↔ Hygiene**: Conveniência de acesso
    - **Kitchen ↔ Work/Leisure**: Área social integrada
    - **Storage ↔ Kitchen**: Acesso a insumos
    """)
    
    st.markdown("#### Critical Paths")
    st.markdown(f"""
    **Emergency Egress:**
    - Min Width: {layout_recommendations["critical_paths"]["emergency_egress"]["width_min_m"]} m
    - Min Height: {layout_recommendations["critical_paths"]["emergency_egress"]["height_min_m"]} m
    - Must be unobstructed
    
    **High Traffic:**
    - Min Width: {layout_recommendations["critical_paths"]["high_traffic"]["width_min_m"]} m (double passage)
    """)

with rec_col2:
    st.markdown("#### Incompatible Zones")
    st.markdown("""
    - **Sleep ⨉ Exercise**: Ruído e vibração
    - **Sleep ⨉ Kitchen**: Odores e atividade
    - **Hygiene ⨉ Kitchen**: Razões sanitárias
    """)
    
    st.markdown("#### Zone Requirements")
    for zone_name, zone_data in layout_recommendations["zone_recommendations"].items():
        volume = zone_data.get("volume_m3", "N/A")
        st.markdown(f"**{zone_name.title()}**: {volume if isinstance(volume, str) else f'{volume:.1f}'} m³")

# Visualizações
st.markdown("---")
st.markdown("## Visual Layout")

if config["view_mode"] in ["2D Floor Plan", "Both"]:
    fig_2d = create_2d_layout_plotly(
        zones, floor_area, config["shape"], config["dimensions"],
        ZONE_COLORS, ZONE_NAMES
    )
    st.plotly_chart(fig_2d, use_container_width=True)

if config["view_mode"] in ["3D Habitat", "Both"]:
    fig_3d = create_3d_habitat_view(
        config["shape"], config["dimensions"], zones,
        ZONE_COLORS, ZONE_NAMES
    )
    st.plotly_chart(fig_3d, use_container_width=True)

# Zona Details
render_zones(zones, floor_area, ZONE_COLORS, ZONE_NAMES)

# Export
habitat_data = create_habitat_data_dict(
    config, total_volume, floor_area, nhv, nhv_per_person, total_water,
    zones, issues,
    nhv_per_person >= MIN_NHV_PER_PERSON,
    floor_area_per_person >= MIN_FLOOR_AREA_PER_PERSON
)
render_export(habitat_data)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 0; color: #718096;'>
    <p style='font-size: 1.1rem; font-weight: 600;'>AEGIS made by ENTERPRISE</p>
    <p style='font-size: 0.9rem;'>Your Home in Space: The Habitat Layout Creator - NASA Space Apps Challenge 2025</p>
</div>
""", unsafe_allow_html=True)
