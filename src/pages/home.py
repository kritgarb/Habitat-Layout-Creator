"""
Home page with tool explanation and glossary
"""
import streamlit as st


def render_home_page():
    """Renders the home page"""
    
    st.markdown("# Welcome to AEGIS Habitat Creator")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15)); 
                padding: 2rem; border-radius: 10px; border-left: 4px solid #A68CFF; margin: 1rem 0;'>
        <h2 style='color: #A68CFF; margin-top: 0;'>What is this tool?</h2>
        <p style='font-size: 1.1rem; line-height: 1.8; color: #E2E8F0;'>
            The <strong>AEGIS Habitat Creator</strong> is an interactive tool developed for the 
            <strong>NASA Space Apps Challenge 2025</strong> that allows you to design and validate space habitats 
            following NASA's quantitative standards.
        </p>
        <p style='font-size: 1.1rem; line-height: 1.8; color: #E2E8F0;'>
            With this tool, you can create custom layouts for habitats in different environments 
            (orbit, Moon, Mars), visualize them in 2D and 3D, and validate whether your design meets the critical requirements 
            for habitable volume, floor area, and functional zone distribution.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # SDG Section
    st.markdown("---")
    st.markdown("## UN Sustainable Development Goals (SDGs)")
    
    st.markdown("""
    <p style='font-size: 1.1rem; line-height: 1.8; color: #E2E8F0; text-align: center; margin-bottom: 2rem;'>
        The AEGIS Habitat Creator project aligns with the UN Sustainable Development Goals, 
        contributing to a more sustainable future both on Earth and in space.
    </p>
    """, unsafe_allow_html=True)
    
    # SDG Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Load and display SDG 4 SVG
        svg_img = ""
        try:
            with open("src/selos/SDG-4- Educação de qualidade.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            # Modify SVG to limit size
            svg_img = svg_content.replace('<svg', '<svg width="80" height="80"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(196, 32, 50, 0.1); padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #C42032; height: 100%; min-height: 400px;'>
            <div style="text-align: center; margin-bottom: 1rem;">{svg_img}</div>
            <h4 style='color: #C42032; margin-top: 1rem;'>Quality Education</h4>
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                Our tool serves as an <strong>educational resource</strong> for students and professionals 
                to learn about space habitat design, aerospace engineering, and the challenges of 
                space exploration through an interactive interface based on real scientific standards.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Load and display SDG 9 SVG
        svg_img = ""
        try:
            with open("src/selos/SDG-9-Indústria, inovação e infraestrutura.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            # Modify SVG to limit size
            svg_img = svg_content.replace('<svg', '<svg width="80" height="80"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(253, 105, 37, 0.1); padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #FD6925; height: 100%; min-height: 400px;'>
            <div style="text-align: center; margin-bottom: 1rem;">{svg_img}</div>
            <h4 style='color: #FD6925; margin-top: 1rem;'>Industry, Innovation and Infrastructure</h4>
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                We promote <strong>innovation in space infrastructure</strong> through simulation and 
                design tools that enable the development of safe and efficient habitats. 
                3D visualization technology drives technological advancement.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Load and display SDG 11 SVG
        svg_img = ""
        try:
            with open("src/selos/SDG-11 -  Cidades e comunidades sustentáveis.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            # Modify SVG to limit size
            svg_img = svg_content.replace('<svg', '<svg width="80" height="80"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(253, 157, 36, 0.1); padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #FD9D24; height: 100%; min-height: 400px;'>
            <div style="text-align: center; margin-bottom: 1rem;">{svg_img}</div>
            <h4 style='color: #FD9D24; margin-top: 1rem;'>Sustainable Cities and Communities</h4>
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                We develop concepts for <strong>sustainable communities in space</strong> through 
                optimized resource planning, efficient habitable volume management, and 
                long-term sustainability considerations for extended space missions.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        # Load and display SDG 17 SVG
        svg_img = ""
        try:
            with open("src/selos/SDG-17 Parcerias e meios de implementação.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            # Modify SVG to limit size
            svg_img = svg_content.replace('<svg', '<svg width="80" height="80"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(25, 72, 106, 0.1); padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #19486A; height: 100%; min-height: 400px;'>
            <div style="text-align: center; margin-bottom: 1rem;">{svg_img}</div>
            <h4 style='color: #19486A; margin-top: 1rem;'>Partnerships and Implementation Means</h4>
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                Created for the <strong>NASA Space Apps Challenge</strong>, this project exemplifies 
                global collaboration on space challenges. The open-source tool fosters partnerships 
                between educators, engineers, and space enthusiasts around the world.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # How to Use
    st.markdown("## How to Use")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 1 Configure
        On the **2D Layout** or **3D Layout** pages, configure:
        - Habitat shape (Cylindrical/Rectangular)
        - Physical dimensions
        - Crew size
        - Mission duration
        - Desired functional zones
        """)
    
    with col2:
        st.markdown("""
        ### 2 Visualize
        View your habitat in:
        - **2D Floor Plan**: Zone layout with real proportions
        - **3D Model**: Interactive three-dimensional visualization
        - Colors indicate different functional zones
        """)
    
    with col3:
        st.markdown("""
        ### 3 Validate
        On the **NASA Metrics** page:
        - Check that it meets NASA standards
        - Analyze NHV (Net Habitable Volume)
        - Check water and resource requirements
        - Export data in JSON
        """)
    
    st.markdown("---")
    
    # Glossary
    st.markdown("## Terms Glossary")
    
    glossary = {
        "NHV (Net Habitable Volume)": {
            "desc": "The usable interior space of the habitat, excluding equipment, walls, and inaccessible areas.",
            "formula": "NHV = Total Volume × Usability Factor (typically 0.7)",
            "ref": "NASA Formula: NHV (m³/person) = 6.67 × ln(duration_days) - 7.79"
        },
        "Cylindrical Habitat": {
            "desc": "Circular format optimized for uniform pressurization and structural efficiency in low-gravity environments, such as in orbits.",
            "formula": "Volume = π × (diameter/2)² × height",
            "ref": "Based on ISS and NASA TransHab design"
        },
        "Rectangular Habitat": {
            "desc": "Modular format that facilitates connection between modules and maximizes usable floor area.",
            "formula": "Volume = length × width × height",
            "ref": "Used in lunar/Martian surface habitats"
        },
        "Functional Zones": {
            "desc": "Areas designated for specific crew activities.",
            "formula": "Zone Area = m²/person × number of crew members",
            "ref": "6 main zones: Sleep, Hygiene, Kitchen, Exercise, Storage, Work/Leisure"
        },
        "Rigid Structure": {
            "desc": "Aluminum or composite construction with high resistance and protection against micrometeoroids.",
            "formula": "Mass ≈ 150 kg/m³ of volume",
            "ref": "Example: International Space Station modules"
        },
        "Inflatable Structure": {
            "desc": "Expandable softgoods that offer 3-4x more volume with lower launch mass.",
            "formula": "Mass ≈ 40 kg/m³ of volume",
            "ref": "Example: BEAM (Bigelow Expandable Activity Module) on ISS"
        },
        "Microgravity (0g)": {
            "desc": "Orbital environment where gravity is negligible. Crew can use walls and ceiling.",
            "formula": "Main metric: Volume (m³) | Range: 10⁻⁶g to 10⁻¹g",
            "ref": "ISS, Earth-Mars transit habitats"
        },
        "Lunar Gravity (1/6g)": {
            "desc": "16.7% of Earth gravity. Requires functional floor area.",
            "formula": "Main metric: Horizontal area (m²) | g ≈ 0.17g or 1/6g",
            "ref": "Lunar surface habitats"
        },
        "Martian Gravity (3/8g)": {
            "desc": "37.5% of Earth gravity. Behavior closer to Earth.",
            "formula": "Main metric: Horizontal area (m²) | g ≈ 0.38g",
            "ref": "Martian surface habitats"
        },
        "Mission Resources": {
            "desc": "Critical supplies for life support during the mission.",
            "formula": "• Potable water: 2.0 kg/person/day\n• Food water: 0.5 kg/person/day\n• Oxygen: 0.82 kg/person/day",
            "ref": "NASA-STD-3001 Human Integration Design Handbook"
        }
    }
    
    # Exibir glossário em cards
    for idx, (term, info) in enumerate(glossary.items()):
        if idx % 2 == 0:
            col1, col2 = st.columns(2)
        
        with col1 if idx % 2 == 0 else col2:
            with st.expander(f"**{term}**", expanded=False):
                st.markdown(f"**Description:**")
                st.write(info["desc"])
                st.markdown(f"**Calculation/Formula:**")
                st.code(info["formula"], language=None)
                st.caption(f"Ref: {info['ref']}")
    
    st.markdown("---")
    
    # Quick navigation guide
    st.markdown("## Navigation")
    
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)
    
    with nav_col1:
        st.markdown("""
        ### 2D Layout
        - Habitat floor plan
        - Zone distribution
        - Top view
        - Scale proportions
        """)
    
    with nav_col2:
        st.markdown("""
        ### 3D Layout
        - Three-dimensional model
        - Interactive visualization
        - Zone divisions
        - Rotational camera
        """)
    
    with nav_col3:
        st.markdown("""
        ### NASA Metrics
        - Standards validation
        - Calculated NHV
        - Required resources
        - Compliance status
        """)
    
    with nav_col4:
        st.markdown("""
        ### Documentation
        - Complete usage guide
        - Detailed NASA standards
        - Technical references
        - Practical examples
        """)
    
    with nav_col5:
        st.markdown("""
        ### About
        - Project information
        - AEGIS Team
        - NASA Space Apps 2025
        - Contact and credits
        """)
    
    st.markdown("---")
    
    # Call to action
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2)); 
                border-radius: 10px; margin: 2rem 0;'>
        <h2 style='color: #A68CFF;'>Ready to Get Started?</h2>
        <p style='font-size: 1.2rem; color: #E2E8F0;'>
            Go to <strong>2D Layout</strong> or <strong>3D Layout</strong> to start designing your space habitat!
        </p>
    </div>
    """, unsafe_allow_html=True)
