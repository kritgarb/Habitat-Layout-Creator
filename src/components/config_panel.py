"""
Reusable configuration panel for each page
"""
import streamlit as st
from ..config.constants import GRAVITY_ENVIRONMENTS, HABITAT_TYPES, NHV_REFERENCE, ZONE_MIN_AREA, ZONE_NAMES


def render_config_panel():
    """
    Renders the habitat configuration panel.
    
    Returns:
        Dictionary with all selected configurations
    """
    st.markdown("### Habitat Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Shape and Structure")
        shape = st.selectbox("Habitat Shape", ["Cylinder", "Rectangular"], key="shape")
        structure_type = st.radio(
            "Structure Type",
            ["rigid", "inflatable"],
            format_func=lambda x: HABITAT_TYPES[x]["description"],
            help="Rigid structure: limited volume, high protection\nInflatable: 3-4x larger volume, lower mass",
            key="structure"
        )
        
    with col2:
        st.markdown("#### Mission Parameters")
        crew_size = st.slider("Crew Size", min_value=4, max_value=6, value=4, key="crew")
        mission_duration = st.number_input(
            "Mission Duration (days)", 
            min_value=1, 
            max_value=1000, 
            value=180,
            help="Used to calculate required NHV by NASA formula: 6.67 × ln(days) - 7.79",
            key="duration"
        )
        gravity_env = st.selectbox(
            "Gravitational Environment",
            ["microgravity", "lunar", "mars"],
            format_func=lambda x: GRAVITY_ENVIRONMENTS[x]["description"],
            help="Affects whether volume or horizontal area is prioritized",
            key="gravity"
        )
    
    st.markdown("#### Dimensions (meters)")
    dim_col1, dim_col2, dim_col3 = st.columns(3)
    
    if shape == "Cylinder":
        with dim_col1:
            diameter = st.number_input("Diameter", min_value=2.0, max_value=15.0, value=6.0, step=0.5, key="diameter")
        with dim_col2:
            height = st.number_input("Height", min_value=2.0, max_value=20.0, value=10.0, step=0.5, key="height")
        dimensions = {"diameter": diameter, "height": height, "length": None, "width": None}
    else:
        with dim_col1:
            length = st.number_input("Length", min_value=2.0, max_value=20.0, value=10.0, step=0.5, key="length")
        with dim_col2:
            width = st.number_input("Width", min_value=2.0, max_value=15.0, value=6.0, step=0.5, key="width")
        with dim_col3:
            height = st.number_input("Height", min_value=2.0, max_value=20.0, value=4.0, step=0.5, key="height")
        dimensions = {"length": length, "width": width, "height": height, "diameter": width}
    
    st.markdown("---")
    st.markdown("#### Functional Zones")
    st.caption("Select zones to include and customize areas per person:")
    
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
                    "m²/person",
                    min_value=0.5,
                    max_value=20.0,
                    value=ZONE_MIN_AREA[zone_id],
                    step=0.5,
                    key=f"area_{zone_id}"
                )
                zone_areas[zone_id] = area
    
    # Show summary
    if zone_areas:
        total_area_per_person = sum(zone_areas.values())
        st.success(f"{len(zone_areas)} zones selected · {total_area_per_person:.1f} m²/person total")
    else:
        st.warning("No zones selected")
    
    st.markdown("---")
    
    adv_col1, adv_col2 = st.columns(2)
    with adv_col1:
        usable_factor = st.slider(
            "Usable Volume Factor", 
            min_value=0.5, 
            max_value=0.9, 
            value=0.7, 
            step=0.05,
            help="Fraction of total volume that is net habitable (NHV)",
            key="usable"
        )
    
    with adv_col2:
        st.markdown("**NASA NHV Reference:**")
        st.caption(f"""
        - 30 days: {NHV_REFERENCE[30]} m³/person
        - 180 days: {NHV_REFERENCE[180]} m³/person
        - 365 days: {NHV_REFERENCE[365]} m³/person
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
