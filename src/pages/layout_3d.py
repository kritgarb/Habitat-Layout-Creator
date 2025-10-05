"""
3D visualization page with configurations and explanations
"""
import streamlit as st
from src.components.config_panel import render_config_panel
from src.visualizations.layout_3d import create_3d_habitat_view
from src.config.constants import ZONE_COLORS, ZONE_NAMES, MIN_FLOOR_AREA_PER_PERSON
from src.utils.calculations import (
    calculate_cylinder_volume, calculate_cylinder_floor_area,
    calculate_box_volume, calculate_box_floor_area,
    calculate_nhv, allocate_zones
)
from src.utils.nasa_calculations import calculate_nhv_per_person


def render_layout_3d_page():
    """Renders the 3D Layout page"""
    
    st.markdown("# 3D Layout - Three-Dimensional Visualization")
    
    # 3D visualization explanation
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(168, 85, 247, 0.1)); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #8b5cf6; margin-bottom: 1.5rem;'>
        <h3 style='color: #8b5cf6; margin-top: 0;'>What is 3D Visualization?</h3>
        <p style='color: #E2E8F0; line-height: 1.8;'>
            The 3D visualization shows the <strong>complete volume</strong> of your space habitat, 
            allowing you to see the <strong>real dimensions</strong> and <strong>zone distribution</strong> 
            in three dimensions.
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
        st.markdown("### Interactive 3D Model")
        
        # Quick summary metrics above visualization
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            st.metric("Total Volume", f"{total_volume:.1f} m³")
            st.caption(f"NHV: {nhv:.1f} m³")
        
        with metric_col2:
            st.metric("NHV/Person", f"{nhv_per_person:.1f} m³")
            st.caption(f"NASA: {nhv_required_per_person:.1f} m³")
        
        with metric_col3:
            if config["shape"] == "Cylinder":
                st.metric("Dimensions", f"D{config['dimensions']['diameter']}m × H{config['dimensions']['height']}m")
                st.caption("Cylinder")
            else:
                st.metric("Dimensions", f"{config['dimensions']['length']}m × {config['dimensions']['width']}m × {config['dimensions']['height']}m")
                st.caption("Rectangle")
        
        # Interaction tip
        st.info("Tip: Click and drag to rotate. Use mouse wheel to zoom. Double-click to reset view.")
        
        # 3D Visualization
        fig_3d = create_3d_habitat_view(
            config["shape"], config["dimensions"], zones,
            ZONE_COLORS, ZONE_NAMES
        )
        st.plotly_chart(fig_3d, use_container_width=True, config={"displayModeBar": True, "responsive": True})
        
        # Validations
        val_col1, val_col2 = st.columns(2)
        
        with val_col1:
            if nhv_per_person >= nhv_required_per_person:
                st.success(f"NHV per person ({nhv_per_person:.1f} m³) meets NASA standard ({nhv_required_per_person:.1f} m³)")
            else:
                st.error(f"NHV per person ({nhv_per_person:.1f} m³) is below NASA minimum ({nhv_required_per_person:.1f} m³)")
                st.caption(f"Deficit: {nhv_required_per_person - nhv_per_person:.1f} m³/person")
        
        with val_col2:
            if floor_area_per_person >= MIN_FLOOR_AREA_PER_PERSON:
                st.success(f"Floor area per person ({floor_area_per_person:.1f} m²) meets NASA standard ({MIN_FLOOR_AREA_PER_PERSON} m²)")
            else:
                st.error(f"Floor area per person ({floor_area_per_person:.1f} m²) is below NASA minimum ({MIN_FLOOR_AREA_PER_PERSON} m²)")
                st.caption(f"Deficit: {MIN_FLOOR_AREA_PER_PERSON - floor_area_per_person:.1f} m²/person")
    
    st.markdown("---")
    
    # Zone Legend below (full width)
    st.markdown("### Zone Distribution Details")
    
    legend_cols = st.columns(3)
    for idx, (zone_id, area) in enumerate(zones.items()):
        with legend_cols[idx % 3]:
            percentage = (area / total_zone_area) * 100
            volume_per_zone = (total_volume / len(zones))  # Simplification
            st.markdown(f"""
            <div style='background: {ZONE_COLORS[zone_id]}20; padding: 1rem; border-radius: 8px; 
                        border-left: 4px solid {ZONE_COLORS[zone_id]}; margin-bottom: 1rem;'>
                <div style='color: {ZONE_COLORS[zone_id]}; font-weight: 700; font-size: 1.1rem;'>
                    {ZONE_NAMES[zone_id]}
                </div>
                <div style='color: #E2E8F0; font-size: 1.1rem; margin: 0.5rem 0;'>
                    Area: {area:.1f} m² ({percentage:.1f}%)
                </div>
                <div style='color: #A0AEC0;'>
                    Estimated volume: ~{volume_per_zone:.1f} m³
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Interpretation tips
    st.markdown("---")
    st.markdown("### Design Insights")
    
    tip_col1, tip_col2 = st.columns(2)
    
    with tip_col1:
        st.markdown("""
        **Volumetric Analysis:**
        - 3D volume is critical for pressurized environments
        - NHV (Net Habitable Volume) excludes equipment and structures
        - Larger volume = more psychological comfort for crew
        - NASA recommends minimums based on mission duration
        """)
        
        st.markdown("""
        **NASA References:**
        - Short missions (30 days): 12.7 m³/person
        - Medium missions (90 days): 16.7 m³/person  
        - Long missions (360+ days): 22.5 m³/person
        """)
    
    with tip_col2:
        st.markdown("""
        **Rotation and Exploration:**
        - Visualize the habitat from all angles
        - Check proportions and spatial distribution
        - Consider movement flow between zones
        - Evaluate suitability for specific activities
        """)
        
        st.markdown("""
        **Usability Factors:**
        - Usability factor reduces total volume to NHV
        - Rigid structures: 70-80% (more equipment)
        - Inflatable structures: 85-90% (less equipment)
        """)
