"""
NASA metrics page with configurations and educational explanations
"""
import streamlit as st
from src.components.config_panel import render_config_panel
from src.components.metrics import render_metrics
from src.config.constants import MIN_FLOOR_AREA_PER_PERSON
from src.utils.calculations import (
    calculate_cylinder_volume, calculate_cylinder_floor_area,
    calculate_box_volume, calculate_box_floor_area,
    calculate_nhv, allocate_zones
)
from src.utils.nasa_calculations import calculate_nhv_per_person


def render_metrics_page():
    """Renders the NASA Metrics page"""
    
    st.markdown("# NASA Metrics - Quantitative Analysis")
    
    # NASA metrics explanation
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(236, 72, 153, 0.1), rgba(219, 39, 119, 0.1)); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #ec4899; margin-bottom: 2rem;'>
        <h3 style='color: #ec4899; margin-top: 0;'>What are NASA Metrics?</h3>
        <p style='color: #E2E8F0; line-height: 1.8;'>
            The quantitative metrics from <strong>NASA Human Integration Design Handbook (HIDH)</strong> are 
            scientific standards established through decades of space mission research. 
            They ensure the habitat is <strong>safe, functional, and psychologically healthy</strong> 
            for the crew.
        </p>
        <h4 style='color: #ec4899; margin-top: 1.5rem;'>Why do these metrics matter?</h4>
        <ul style='color: #E2E8F0; line-height: 1.8;'>
            <li><strong>Physical Health:</strong> Insufficient space causes mobility problems, fatigue, and 
            increased accident risk.</li>
            <li><strong>Psychological Well-being:</strong> Over-confined environments increase stress, interpersonal 
            conflicts, and team performance deterioration.</li>
            <li><strong>Operational Efficiency:</strong> Poorly dimensioned layouts reduce productivity and 
            complicate critical daily activities.</li>
            <li><strong>Mission Safety:</strong> NASA standards are based on data from ISS, Skylab, Mir 
            and other real missions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Configuration panel
    with st.expander("Configure Habitat", expanded=True):
        config = render_config_panel()
    
    # Validate if zones are selected
    if not config["zone_areas"]:
        st.warning("Please select at least one functional zone in the configuration above.")
        st.stop()
    
    st.markdown("---")
    
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
    
    # Calculate required water
    total_water = config["crew_size"] * config["mission_duration"] * 2.5  # 2.5 kg/person/day
    
    # Allocate zones
    zones = allocate_zones(floor_area, config["crew_size"], config["zone_areas"])
    
    # Metrics dashboard
    st.markdown("### Complete Metrics Dashboard")
    render_metrics(
        total_volume=total_volume,
        floor_area=floor_area,
        nhv=nhv,
        nhv_per_person=nhv_per_person,
        floor_area_per_person=floor_area_per_person,
        crew_size=config["crew_size"],
        total_water=total_water,
        mission_duration=config["mission_duration"],
        min_nhv=nhv_required_per_person,
        min_floor_area=MIN_FLOOR_AREA_PER_PERSON
    )
    
    st.markdown("---")
    
    # Educational explanations of main metrics
    st.markdown("### Metrics Interpretation Guide")
    
    # NHV
    with st.expander("Net Habitable Volume (NHV) - Net Habitable Volume", expanded=True):
        st.markdown(f"""
        **Definition:**  
        NHV is the interior volume **actually usable** by astronauts, excluding space occupied 
        by equipment, life support systems, storage, and structures.
        
        **Formula:**
        ```
        NHV = Total Volume × Usability Factor
        ```
        
        **Your Habitat:**
        - Total Volume: **{total_volume:.1f} m³**
        - Usability Factor: **{config['usable_factor']*100:.0f}%**
        - Resulting NHV: **{nhv:.1f} m³**
        - NHV per Person: **{nhv_per_person:.1f} m³/person**
        
        **NASA Standards (based on mission duration):**
        - ≤30 days: 12.7 m³/person
        - 31-90 days: 16.7 m³/person
        - 91-180 days: 20.0 m³/person
        - 181-360 days: 22.5 m³/person
        - &gt;360 days: 27.9 m³/person
        
        **For your {config['mission_duration']}-day mission:**
        - Required NHV: **{nhv_required_per_person:.1f} m³/person**
        - Your NHV: **{nhv_per_person:.1f} m³/person**
        - Status: {'ADEQUATE' if nhv_per_person >= nhv_required_per_person else f'BELOW STANDARD (deficit of {nhv_required_per_person - nhv_per_person:.1f} m³/person)'}
        
        **Why this matters:**  
        NASA studies show that insufficient NHV correlates with increased stress, 
        interpersonal conflicts, sleep problems, and cognitive performance decline. Adequate NHV 
        provides space for movement, privacy, and recreational activities essential for 
        long-duration missions.
        """)
    
    # Floor area
    with st.expander("Floor Area - Floor Area"):
        st.markdown(f"""
        **Definition:**  
        Floor area is the horizontal space available for circulation, work, and daily activities.
        
        **Formula:**
        - **Cylinder:** Area = π × (Diameter/2)²
        - **Rectangle:** Area = Length × Width
        
        **Your Habitat:**
        - Total Floor Area: **{floor_area:.1f} m²**
        - Area per Person: **{floor_area_per_person:.1f} m²/person**
        
        **NASA Minimum Standard:**
        - Required: **{MIN_FLOOR_AREA_PER_PERSON} m²/person**
        - Status: {'MEETS STANDARD' if floor_area_per_person >= MIN_FLOOR_AREA_PER_PERSON else f'BELOW MINIMUM (deficit of {MIN_FLOOR_AREA_PER_PERSON - floor_area_per_person:.1f} m²/person)'}
        
        **Why this matters:**  
        Floor area directly impacts mobility, especially in microgravity environments 
        where astronauts use walls and ceiling to move. Insufficient area increases collision 
        risk, hampers simultaneous work by multiple crew members, and reduces 
        operational efficiency.
        """)
    
    # Zone distribution
    with st.expander("Zone Distribution - Zone Distribution"):
        st.markdown(f"""
        **Definition:**  
        Functional zones divide the habitat into specialized areas for different activities 
        (sleeping, working, hygiene, eating, etc.).
        
        **Your Habitat:**
        - Number of Zones: **{len(zones)}**
        - Total Allocated Area: **{sum(zones.values()):.1f} m²**
        
        **Detailed Distribution:**
        """)
        
        from ..config.constants import ZONE_NAMES
        for zone_id, area in zones.items():
            percentage = (area / sum(zones.values())) * 100
            area_per_person = area / config["crew_size"]
            st.markdown(f"""
            - **{ZONE_NAMES[zone_id]}:** {area:.1f} m² ({percentage:.1f}%) = {area_per_person:.1f} m²/person
            """)
        
        st.markdown("""
        **NASA Recommendations by Zone:**
        - **Sleep:** 2-4 m²/person (privacy essential)
        - **Work:** 3-5 m²/person (space for equipment)
        - **Hygiene:** 1.5-2 m²/person (bathroom + personal hygiene)
        - **Food:** 1-2 m²/person (preparation + consumption)
        - **Exercise:** 3-4 m²/person (equipment + movement)
        - **Recreation:** 2-3 m²/person (psychological well-being)
        - **Storage:** 1-2 m²/person (supplies + equipment)
        
        **Why this matters:**  
        Adequate zone distribution is critical for separating incompatible activities (e.g. sleeping 
        and exercise), maintaining hygiene (separation of wet/dry areas), and optimizing crew 
        workflow.
        """)
    
    # Usability factor
    with st.expander("Usability Factor - Usability Factor"):
        st.markdown(f"""
        **Definition:**  
        The usability factor represents the percentage of total volume that is actually usable 
        by crew members, discounting space occupied by systems and equipment.
        
        **Your Habitat:**
        - Usability Factor: **{config['usable_factor']*100:.0f}%**
        - Structure: **{config['structure_type']}**
        
        **Typical Ranges by Structure Type:**
        - **Rigid Structures (Metallic):** 70-80%
          - More integrated equipment (HVAC, power, communication)
          - Control panels and systems occupy walls
          - More robust structure = more lost space
        
        - **Inflatable Structures (Soft Goods):** 85-90%
          - Less fixed structural equipment
          - Flexible walls allow better space utilization
          - More compact or external systems
        
        **Historical Examples:**
        - ISS: ~75% (complex rigid structure)
        - Bigelow BEAM: ~88% (inflatable module)
        - Skylab: ~72% (rigid structure)
        
        **Why this matters:**  
        An overestimated usability factor results in unrealistic NHV, leading to designs that appear 
        adequate on paper but are claustrophobic in practice. Conservative values (70-75%) are 
        safer for preliminary designs.
        """)
    
    # Gravity and resources
    with st.expander("Gravity & Resources - Gravity and Resources"):
        st.markdown(f"""
        **Your Habitat:**
        - Gravity Environment: **{config['gravity_env']}**
        - Mission Duration: **{config['mission_duration']} days**
        - Crew Size: **{config['crew_size']} people**
        
        **Gravity Impact on Design:**
        
        **Microgravity (0g):**
        - Astronauts use all surfaces (walls, ceiling, floor)
        - 3D volume is more important than floor area
        - Need for anchor points and restraints
        - Higher risk of collisions and spatial disorientation
        
        **Lunar Gravity (1/6g = 0.165g):**
        - Movement is still "floating" but with preferred direction
        - Floor is more important but ceiling/walls still usable
        - Equipment can have gravitational orientation
        - Easier adaptation than microgravity
        
        **Martian Gravity (3/8g = 0.38g):**
        - Behavior closer to Earth
        - Floor is primary work surface
        - More traditional design with clear "up/down"
        - Fewer equipment orientation restrictions
        
        **Duration Impact:**
        - **Short (&lt;30 days):** Focus on functionality, comfort secondary
        - **Medium (30-180 days):** Need recreational spaces and privacy
        - **Long (&gt;180 days):** Psychological well-being critical, environment variety essential
        
        **Why this matters:**  
        The gravitational environment and mission duration dramatically influence volume, layout, 
        and amenity requirements. Long missions in microgravity require the largest volumes 
        per person to maintain crew mental health.
        """)
    
    st.markdown("---")
    
    # Validation summary
    st.markdown("### NASA Compliance Summary")
    
    validations = []
    
    # Validate NHV
    if nhv_per_person >= nhv_required_per_person:
        validations.append(("NHV per Person", True, f"{nhv_per_person:.1f} m³ (required: {nhv_required_per_person:.1f} m³)"))
    else:
        validations.append(("NHV per Person", False, f"{nhv_per_person:.1f} m³ (required: {nhv_required_per_person:.1f} m³) - Deficit: {nhv_required_per_person - nhv_per_person:.1f} m³"))
    
    # Validate floor area
    if floor_area_per_person >= MIN_FLOOR_AREA_PER_PERSON:
        validations.append(("Floor Area", True, f"{floor_area_per_person:.1f} m²/person (minimum: {MIN_FLOOR_AREA_PER_PERSON} m²)"))
    else:
        validations.append(("Floor Area", False, f"{floor_area_per_person:.1f} m²/person (minimum: {MIN_FLOOR_AREA_PER_PERSON} m²) - Deficit: {MIN_FLOOR_AREA_PER_PERSON - floor_area_per_person:.1f} m²"))
    
    # Validate minimum zones
    if len(zones) >= 3:
        validations.append(("Zone Diversity", True, f"{len(zones)} functional zones"))
    else:
        validations.append(("Zone Diversity", False, f"{len(zones)} zones (recommended: minimum 3 for basic functionality)"))
    
    # Display validations
    for metric_name, is_valid, description in validations:
        if is_valid:
            st.success(f"**{metric_name}:** {description}")
        else:
            st.error(f"**{metric_name}:** {description}")
    
    # Conclusion
    all_valid = all(v[1] for v in validations)
    if all_valid:
        st.success("Congratulations! Your habitat meets all analyzed NASA HIDH standards.")
    else:
        st.warning("Attention: Your habitat does not meet all NASA standards. Review the metrics in red and adjust the configurations.")
