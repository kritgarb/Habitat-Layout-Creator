import streamlit as st
from src.config.constants import (
    MIN_NHV_PER_PERSON, MIN_FLOOR_AREA_PER_PERSON, WATER_PER_DAY_PER_PERSON,
    ZONE_COLORS, ZONE_NAMES, ZONE_MIN_AREA
)
from src.config.styles import CUSTOM_CSS
from src.utils.calculations import (
    calculate_cylinder_volume, calculate_cylinder_floor_area,
    calculate_box_volume, calculate_box_floor_area,
    calculate_nhv, allocate_zones
)
from src.utils.validators import validate_nasa_standards
from src.visualizations.layout_2d import create_2d_layout_plotly
from src.visualizations.layout_3d import create_3d_habitat_view
from src.components.sidebar import render_sidebar
from src.components.metrics import render_metrics, render_validation, render_zones
from src.components.export import render_export, create_habitat_data_dict

st.set_page_config(
    page_title="Habitat Layout Creator - NASA Space Apps 2025",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Header
st.markdown("""
<div style='text-align: center; padding: 2rem 0 1rem 0;'>
    <h1 style='font-size: 3rem; margin-bottom: 0.5rem;'>HABITAT LAYOUT CREATOR</h1>
    <p style='font-size: 1.2rem; color: #A0AEC0; font-weight: 500;'>NASA Space Apps Challenge 2025</p>
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
total_water = WATER_PER_DAY_PER_PERSON * config["crew_size"] * config["mission_duration"]

zones = allocate_zones(floor_area, config["crew_size"], ZONE_MIN_AREA)

# Validação NASA
is_valid, issues = validate_nasa_standards(
    nhv_per_person, 
    floor_area_per_person,
    MIN_NHV_PER_PERSON,
    MIN_FLOOR_AREA_PER_PERSON
)

# Renderizar métricas
render_metrics(
    total_volume, floor_area, nhv, nhv_per_person, floor_area_per_person,
    config["crew_size"], total_water, config["mission_duration"],
    MIN_NHV_PER_PERSON, MIN_FLOOR_AREA_PER_PERSON
)

# Renderizar validação
render_validation(issues)

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
    <p style='font-size: 1.1rem; font-weight: 600;'>HABITAT LAYOUT CREATOR</p>
    <p style='font-size: 0.9rem;'>NASA Space Apps Challenge 2025</p>
</div>
""", unsafe_allow_html=True)
