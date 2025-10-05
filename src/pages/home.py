"""
Home page with tool explanation and glossary - Redesigned
"""
import streamlit as st
from src.visualizations.layout_3d import create_3d_habitat_view
from src.config.constants import ZONE_COLORS, ZONE_NAMES
from src.utils.calculations import allocate_zones


def render_home_page():
    """Renders the home page with an inviting design"""
    # Create demo 3D visualization
    demo_dimensions = {"diameter": 6.0, "height": 10.0, "length": None, "width": None}
    demo_zones_config = {
        "sleep": 2.5,
        "work_leisure": 3.0,
        "hygiene": 1.5,
        "kitchen": 1.5,
        "exercise": 3.0,
        "storage": 1.5
    }
    demo_floor_area = 3.14159 * (3.0 ** 2)  # π * r²
    demo_zones = allocate_zones(demo_floor_area, 4, demo_zones_config)
    
    fig_3d_demo = create_3d_habitat_view(
        "Cylinder", demo_dimensions, demo_zones,
        ZONE_COLORS, ZONE_NAMES
    )
    
    st.plotly_chart(fig_3d_demo, use_container_width=True, config={"displayModeBar": True, "responsive": True})
    
    st.markdown("""
    <div style='text-align: center; padding: 1.5rem; background: rgba(102, 126, 234, 0.08); 
                border-radius: 10px; margin: 1.5rem auto; max-width: 700px;'>
        <p style='color: #E2E8F0; font-size: 1.05rem; margin: 0;'>
            <strong style='color: #667EEA;'>Sample Configuration:</strong> 
            Cylindrical Habitat · 6m diameter × 10m height · 4 crew members · 6 functional zones
        </p>
        <p style='color: #94A3B8; font-size: 0.95rem; margin: 0.5rem 0 0 0;'>
            Navigate to <strong>2D Layout</strong> or <strong>3D Layout</strong> to create your own custom design!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main value proposition
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15)); 
                padding: 2.5rem; border-radius: 15px; border: 2px solid rgba(166, 140, 255, 0.3);
                margin: 2rem 0; box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2);'>
        <div style='text-align: center;'>
            <h2 style='color: #A68CFF; margin-bottom: 1.5rem; font-size: 2rem;'>
                Build the Future of Space Living
            </h2>
            <p style='font-size: 1.15rem; line-height: 1.8; color: #E2E8F0; max-width: 900px; margin: 0 auto;'>
                An interactive tool developed for the <strong style='color: #667EEA;'>NASA Space Apps Challenge 2025</strong> 
                that empowers you to create custom layouts for habitats in different environments — 
                <strong>orbit, Moon, or Mars</strong> — and validate them against critical NASA requirements.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Start Guide - Visual Steps
    st.markdown("""
    <h2 style='text-align: center; color: #A68CFF; font-size: 2.2rem; margin: 3rem 0 2rem 0;'>
        Quick Start in 3 Steps
    </h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1)); 
                    padding: 2rem; border-radius: 15px; border-left: 5px solid #3B82F6; 
                    height: 100%; text-align: center;'>
            <div style='font-size: 3rem; font-weight: 800; color: #3B82F6; margin-bottom: 1rem;'>01</div>
            <h3 style='color: #3B82F6; margin-bottom: 1rem;'>Configure</h3>
            <p style='font-size: 1rem; line-height: 1.7; color: #CBD5E1;'>
                Choose your habitat type, dimensions, crew size, mission duration, and functional zones
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(124, 58, 237, 0.1)); 
                    padding: 2rem; border-radius: 15px; border-left: 5px solid #8B5CF6; 
                    height: 100%; text-align: center;'>
            <div style='font-size: 3rem; font-weight: 800; color: #8B5CF6; margin-bottom: 1rem;'>02</div>
            <h3 style='color: #8B5CF6; margin-bottom: 1rem;'>Visualize</h3>
            <p style='font-size: 1rem; line-height: 1.7; color: #CBD5E1;'>
                View your habitat in 2D floor plans and interactive 3D models with real proportions
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1)); 
                    padding: 2rem; border-radius: 15px; border-left: 5px solid #10B981; 
                    height: 100%; text-align: center;'>
            <div style='font-size: 3rem; font-weight: 800; color: #10B981; margin-bottom: 1rem;'>03</div>
            <h3 style='color: #10B981; margin-bottom: 1rem;'>Validate</h3>
            <p style='font-size: 1rem; line-height: 1.7; color: #CBD5E1;'>
                Check NASA compliance, analyze metrics, and export your validated design
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
    # SDG Section
    st.markdown("""
    <h2 style='text-align: center; color: #A68CFF; font-size: 2.2rem; margin: 2rem 0 1.5rem 0;'>
        Contributing to UN Sustainable Development Goals
    </h2>
    <p style='font-size: 1.1rem; line-height: 1.8; color: #94A3B8; text-align: center; 
              margin-bottom: 2.5rem; max-width: 800px; margin-left: auto; margin-right: auto;'>
        This project aligns with global sustainability efforts, advancing space exploration 
        while promoting education, innovation, and international collaboration
    </p>
    """, unsafe_allow_html=True)
    
    # SDG Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        svg_img = ""
        try:
            with open("src/selos/SDG-4- Educação de qualidade.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            svg_img = svg_content.replace('<svg', '<svg width="135" height="135"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(102, 126, 234, 0.08); padding: 2rem; border-radius: 12px; 
                    border: 2px solid rgba(196, 32, 50, 0.4); height: 100%; min-height: 440px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
            <div style="text-align: center; margin-bottom: 1.3rem;">{svg_img}</div>
            <h4 style='color: #C42032; margin-top: 1rem; text-align: center; font-weight: 700; font-size: 1.5rem;'>Quality Education</h4>
            <p style='font-size: 1rem; line-height: 1.7; color: #E2E8F0;'>
                Educational resource for students and professionals to learn space habitat design 
                and aerospace engineering through interactive, standards-based tools
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        svg_img = ""
        try:
            with open("src/selos/SDG-9-Indústria, inovação e infraestrutura.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            svg_img = svg_content.replace('<svg', '<svg width="135" height="135"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(102, 126, 234, 0.08); padding: 2rem; border-radius: 12px; 
                    border: 2px solid rgba(253, 105, 37, 0.4); height: 100%; min-height: 440px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
            <div style="text-align: center; margin-bottom: 1.3rem;">{svg_img}</div>
            <h4 style='color: #FD6925; margin-top: 1rem; text-align: center; font-weight: 700; font-size: 1.5rem;'>Industry, Innovation and Infrastructure</h4>
            <p style='font-size: 1rem; line-height: 1.7; color: #E2E8F0;'>
                Promotes innovation in space infrastructure through advanced simulation 
                and 3D visualization technology for safe, efficient habitat development
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        svg_img = ""
        try:
            with open("src/selos/SDG-11 -  Cidades e comunidades sustentáveis.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            svg_img = svg_content.replace('<svg', '<svg width="135" height="135"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(102, 126, 234, 0.08); padding: 2rem; border-radius: 12px; 
                    border: 2px solid rgba(253, 157, 36, 0.4); height: 100%; min-height: 440px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
            <div style="text-align: center; margin-bottom: 1.3rem;">{svg_img}</div>
            <h4 style='color: #FD9D24; margin-top: 1rem; text-align: center; font-weight: 700; font-size: 1.5rem;'>Sustainable Cities and Communities</h4>
            <p style='font-size: 1rem; line-height: 1.7; color: #E2E8F0;'>
                Develops sustainable space communities through optimized resource planning, 
                efficient volume management, and long-term mission sustainability
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        svg_img = ""
        try:
            with open("src/selos/SDG-17 Parcerias e meios de implementação.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            svg_img = svg_content.replace('<svg', '<svg width="135" height="135"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(102, 126, 234, 0.08); padding: 2rem; border-radius: 12px; 
                    border: 2px solid rgba(25, 72, 106, 0.4); height: 100%; min-height: 440px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
            <div style="text-align: center; margin-bottom: 1.3rem;">{svg_img}</div>
            <h4 style='color: #19486A; margin-top: 1rem; text-align: center; font-weight: 700; font-size: 1.5rem;'>Partnerships and Implementation</h4>
            <p style='font-size: 1rem; line-height: 1.7; color: #E2E8F0;'>
                Exemplifies global collaboration through NASA Space Apps Challenge, 
                fostering partnerships between educators, engineers, and space enthusiasts worldwide
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Glossary Section
    st.markdown("""
    <h2 style='text-align: center; color: #A68CFF; font-size: 2.2rem; margin: 3rem 0 2rem 0;'>
        Technical Glossary
    </h2>
    """, unsafe_allow_html=True)
    
    glossary = {
        "NHV (Net Habitable Volume)": {
            "desc": "The usable interior space of the habitat, excluding equipment, walls, and inaccessible areas.",
            "formula": "NHV = Total Volume × Usability Factor (typically 0.7)",
            "ref": "NASA Formula: NHV (m³/person) = 6.67 × ln(duration_days) - 7.79"
        },
        "Cylindrical Habitat": {
            "desc": "Circular format optimized for uniform pressurization and structural efficiency in low-gravity environments.",
            "formula": "Volume = π × (diameter/2)² × height",
            "ref": "Based on ISS and NASA TransHab design"
        },
        "Rectangular Habitat": {
            "desc": "Modular format that facilitates connection between modules and maximizes usable floor area.",
            "formula": "Volume = length × width × height",
            "ref": "Used in lunar/Martian surface habitats"
        },
        "Functional Zones": {
            "desc": "Areas designated for specific crew activities and operations.",
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
            "ref": "Example: BEAM (Bigelow Expandable Activity Module)"
        },
        "Microgravity (0g)": {
            "desc": "Orbital environment where gravity is negligible. Crew can utilize walls and ceiling.",
            "formula": "Main metric: Volume (m³) | Range: 10⁻⁶g to 10⁻¹g",
            "ref": "ISS, Earth-Mars transit habitats"
        },
        "Lunar Gravity (1/6g)": {
            "desc": "16.7% of Earth gravity. Requires functional floor area for operations.",
            "formula": "Main metric: Horizontal area (m²) | g ≈ 0.17g",
            "ref": "Lunar surface habitats"
        },
        "Martian Gravity (3/8g)": {
            "desc": "37.5% of Earth gravity. Behavior closer to terrestrial environments.",
            "formula": "Main metric: Horizontal area (m²) | g ≈ 0.38g",
            "ref": "Martian surface habitats"
        },
        "Mission Resources": {
            "desc": "Critical supplies for life support systems during extended missions.",
            "formula": "• Potable water: 2.0 kg/person/day\n• Food water: 0.5 kg/person/day\n• Oxygen: 0.82 kg/person/day",
            "ref": "NASA-STD-3001 Human Integration Design Handbook"
        }
    }
    
    # Display glossary in expandable cards
    for idx, (term, info) in enumerate(glossary.items()):
        if idx % 2 == 0:
            col1, col2 = st.columns(2)
        
        with col1 if idx % 2 == 0 else col2:
            with st.expander(f"**{term}**", expanded=False):
                st.markdown(f"**Description:**")
                st.write(info["desc"])
                st.markdown(f"**Calculation/Formula:**")
                st.code(info["formula"], language=None)
                st.caption(f"Reference: {info['ref']}")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Navigation Guide
    st.markdown("""
    <h2 style='text-align: center; color: #A68CFF; font-size: 2.2rem; margin: 3rem 0 2rem 0;'>
        Explore All Features
    </h2>
    """, unsafe_allow_html=True)
    
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)
    
    with nav_col1:
        st.markdown("""
        <div style='background: rgba(59, 130, 246, 0.08); padding: 1.5rem; border-radius: 10px; 
                    border: 1px solid rgba(59, 130, 246, 0.2); text-align: center; height: 100%;'>
            <h4 style='color: #3B82F6; margin-bottom: 0.8rem;'>2D Layout</h4>
            <p style='font-size: 0.9rem; color: #94A3B8; line-height: 1.5;'>
                Floor plan view<br>Zone distribution<br>Scale proportions
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with nav_col2:
        st.markdown("""
        <div style='background: rgba(139, 92, 246, 0.08); padding: 1.5rem; border-radius: 10px; 
                    border: 1px solid rgba(139, 92, 246, 0.2); text-align: center; height: 100%;'>
            <h4 style='color: #8B5CF6; margin-bottom: 0.8rem;'>3D Layout</h4>
            <p style='font-size: 0.9rem; color: #94A3B8; line-height: 1.5;'>
                3D model<br>Interactive view<br>Rotational camera
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with nav_col3:
        st.markdown("""
        <div style='background: rgba(16, 185, 129, 0.08); padding: 1.5rem; border-radius: 10px; 
                    border: 1px solid rgba(16, 185, 129, 0.2); text-align: center; height: 100%;'>
            <h4 style='color: #10B981; margin-bottom: 0.8rem;'>NASA Metrics</h4>
            <p style='font-size: 0.9rem; color: #94A3B8; line-height: 1.5;'>
                Standards validation<br>NHV calculations<br>Compliance status
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with nav_col4:
        st.markdown("""
        <div style='background: rgba(245, 158, 11, 0.08); padding: 1.5rem; border-radius: 10px; 
                    border: 1px solid rgba(245, 158, 11, 0.2); text-align: center; height: 100%;'>
            <h4 style='color: #F59E0B; margin-bottom: 0.8rem;'>Documentation</h4>
            <p style='font-size: 0.9rem; color: #94A3B8; line-height: 1.5;'>
                Usage guide<br>NASA standards<br>Technical references
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with nav_col5:
        st.markdown("""
        <div style='background: rgba(236, 72, 153, 0.08); padding: 1.5rem; border-radius: 10px; 
                    border: 1px solid rgba(236, 72, 153, 0.2); text-align: center; height: 100%;'>
            <h4 style='color: #EC4899; margin-bottom: 0.8rem;'>About</h4>
            <p style='font-size: 0.9rem; color: #94A3B8; line-height: 1.5;'>
                Project info<br>AEGIS Team<br>Contact & credits
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)