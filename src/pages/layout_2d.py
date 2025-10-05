"""
2D visualization page with configurations and explanations
"""
import streamlit as st
from src.components.config_panel import render_config_panel
from src.visualizations.layout_2d import create_2d_layout_plotly
from src.config.constants import ZONE_COLORS, ZONE_NAMES, MIN_FLOOR_AREA_PER_PERSON
from src.utils.calculations import (
    calculate_cylinder_volume, calculate_cylinder_floor_area,
    calculate_box_volume, calculate_box_floor_area,
    calculate_nhv, allocate_zones
)
from src.utils.nasa_calculations import calculate_nhv_per_person


def render_layout_2d_page():
    """Renders the 2D Layout page"""
    
    st.markdown("# 2D Layout - Habitat Floor Plan")
    
    # 2D visualization explanation
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(72, 187, 120, 0.1), rgba(56, 178, 172, 0.1)); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #48bb78; margin-bottom: 1.5rem;'>
        <h3 style='color: #48bb78; margin-top: 0;'>What is the 2D Floor Plan?</h3>
        <p style='color: #E2E8F0; line-height: 1.8;'>
            The 2D visualization shows the <strong>floor plan</strong> of your habitat - a top view that 
            reveals how the <strong>functional zones</strong> are distributed in the available space.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create two columns: configuration panel (left) and visualization (right)
    config_col, viz_col = st.columns([1, 2])
    
    with config_col:
        st.markdown("### Configuration")
        config = render_config_panel()
    
    # Validate if zones are selected
    if not config["zone_areas"]:
        st.warning("Please select at least one functional zone in the configuration.")
        st.stop()
    
    # Calculate metrics
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
    nhv_required_per_person = calculate_nhv_per_person(config["mission_duration"])
    
    # Allocate zones
    zones = allocate_zones(floor_area, config["crew_size"], config["zone_areas"])
    total_zone_area = sum(zones.values())
    
    with viz_col:
        st.markdown("### Floor Plan Visualization")
        
        # Quick summary metrics above visualization
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            shape_translated = "Cylindrical" if config['shape'] == 'Cylinder' else "Rectangular"
            st.metric("Shape", shape_translated)
        
        with metric_col2:
            st.metric("Floor Area", f"{floor_area:.1f} m²")
            st.caption(f"{floor_area_per_person:.1f} m²/person")
        
        with metric_col3:
            st.metric("Zones", f"{len(zones)}")
            st.caption(f"{total_zone_area:.1f} m² allocated")
        
        # 2D Visualization
        fig_2d = create_2d_layout_plotly(
            zones, floor_area, config["shape"], config["dimensions"],
            ZONE_COLORS, ZONE_NAMES
        )
        st.plotly_chart(fig_2d, use_container_width=True, config={"displayModeBar": True, "responsive": True})
        
        # Validation
        if floor_area_per_person < MIN_FLOOR_AREA_PER_PERSON:
            st.error(f"Floor area per person ({floor_area_per_person:.1f} m²) is below NASA minimum ({MIN_FLOOR_AREA_PER_PERSON} m²)")
        else:
            st.success(f"Floor area per person ({floor_area_per_person:.1f} m²) meets NASA standard")
    
    st.markdown("---")
    
    # Zone Legend below (full width)
    st.markdown("### Zone Distribution Details")
    
    legend_cols = st.columns(3)
    for idx, (zone_id, area) in enumerate(zones.items()):
        with legend_cols[idx % 3]:
            percentage = (area / total_zone_area) * 100
            st.markdown(f"""
            <div style='background: {ZONE_COLORS[zone_id]}20; padding: 1rem; border-radius: 8px; 
                        border-left: 4px solid {ZONE_COLORS[zone_id]}; margin-bottom: 1rem;'>
                <div style='color: {ZONE_COLORS[zone_id]}; font-weight: 700; font-size: 1.1rem;'>
                    {ZONE_NAMES[zone_id]}
                </div>
                <div style='color: #E2E8F0; font-size: 1.3rem; font-weight: 700; margin: 0.5rem 0;'>
                    {area:.1f} m²
                </div>
                <div style='color: #A0AEC0;'>
                    {percentage:.1f}% of total | {area/config['crew_size']:.1f} m²/person
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Interpretation tips
    st.markdown("---")
    st.markdown("### Design Insights")
    
    tip_col1, tip_col2 = st.columns(2)
    
    with tip_col1:
        st.markdown("""
        **Spatial Analysis:**
        - Larger zones = more area allocated for that function
        - Balanced distribution indicates well-designed habitat
        - Check if there's enough space for each activity
        - Compare with NASA minimum (10 m²/person)
        """)
    
    with tip_col2:
        st.markdown("""
        **Design Considerations:**
        - Separate incompatible zones (sleep vs exercise)
        - Place hygiene near sleeping quarters
        - Keep kitchen centrally accessible
        - Distribute storage strategically
        """)

