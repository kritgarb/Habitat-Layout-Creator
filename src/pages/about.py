"""
About page with project information
"""
import streamlit as st


def render_about_page():
    """Renders the About page"""
    
    st.markdown("# About AEGIS Habitat Layout Creator")
    
    # Hero section
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(79, 70, 229, 0.1)); 
                padding: 2rem; border-radius: 10px; border-left: 4px solid #6366f1; margin-bottom: 2rem; text-align: center;'>
        <h2 style='color: #6366f1; margin-top: 0;'>AEGIS Habitat Layout Creator</h2>
        <p style='color: #E2E8F0; font-size: 1.2rem; line-height: 1.8;'>
            Interactive design tool for space habitats following NASA HIDH standards
        </p>
        <p style='color: #A0AEC0; font-size: 1rem;'>
            Version 1.0.0 | Developed with Streamlit + Plotly
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Our Team")
    team_col1, team_col2, team_col3 = st.columns([1, 4, 1])
    with team_col2:
        st.image("src/img/FOTO-GRUPO.svg", width="stretch")
        st.markdown("""
        <p style='text-align: center; color: #CBD5F5; font-size: 0.95rem; margin-top: 0.75rem;'>
            Multidisciplinary ENTERPRISE team with expertise in computer science, design, and systems analysis and development.
        </p>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Mission and Vision
    st.markdown("### Mission and Vision")
    
    mission_col1, mission_col2 = st.columns(2)
    
    with mission_col1:
        st.markdown("""
        <div style='background: rgba(72, 187, 120, 0.1); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #48bb78; height: 100%;'>
            <h4 style='color: #48bb78;'>Our Mission</h4>
            <p style='color: #E2E8F0; line-height: 1.8;'>
                Democratize access to professional space design tools, enabling 
                engineers, researchers, and enthusiasts to create and validate space habitat layouts 
                following rigorous NASA standards.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with mission_col2:
        st.markdown("""
        <div style='background: rgba(139, 92, 246, 0.1); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #8b5cf6; height: 100%;'>
            <h4 style='color: #8b5cf6;'>Our Vision</h4>
            <p style='color: #E2E8F0; line-height: 1.8;'>
                Be the reference tool for conceptual space habitat design, 
                accelerating space architecture development and contributing to the 
                sustainable expansion of humanity beyond Earth.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # About the project
    st.markdown("### About the Project")
    
    st.markdown("""
    The **AEGIS Habitat Layout Creator** was born from the need for an accessible and intuitive 
    tool for space habitat design. While professional CAD and structural analysis software 
    are essential for final projects, there's a gap in the conceptual stage - where ideas need 
    to be quickly tested and validated against NASA standards.
    
    Our tool fills this gap by offering:
    
    - **Instant Validation:** NASA metrics calculated in real time
    - **Interactive Visualizations:** Understand your design in 2D and 3D
    - **Education:** Educational explanations of space concepts and standards
    - **Accessibility:** Web interface with no installation required
    - **Open Standards:** Based on public NASA HIDH documentation
    """)
    
    st.markdown("---")
    
    # Main features
    st.markdown("### Main Features")
    
    feature_col1, feature_col2, feature_col3 = st.columns(3)
    
    with feature_col1:
        st.markdown("""
        **Interactive Design**
        - Intuitive parameter configuration
        - Immediate visual feedback
        - Multiple shapes and structures
        - Complete zone customization
        """)
        
        st.markdown("""
        **NASA Metrics**
        - HIDH-compliant calculations
        - Automatic validation
        - Detailed explanations
        - Complete dashboard
        """)
    
    with feature_col2:
        st.markdown("""
        **Visualizations**
        - Professional 2D floor plans
        - Interactive 3D models
        - Rotation and zoom
        - Legends and annotations
        """)
        
        st.markdown("""
        **Documentation**
        - Complete usage guide
        - Terms glossary
        - Tips and best practices
        - NASA references
        """)
    
    with feature_col3:
        st.markdown("""
        **Export**
        - Structured JSON format
        - All metrics included
        - Automatic timestamp
        - Easy sharing
        """)
        
        st.markdown("""
        **Accessibility**
        - Responsive web interface
        - No installation required
        - Multi-language support
        - Free and open-source
        """)
    
    st.markdown("---")
    
    # Technology stack
    st.markdown("### Technology Stack")
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.markdown("""
        **Frontend:**
        - **Streamlit** - Interactive web application framework
        - **Plotly** - Interactive 3D graphics and visualizations
        - **HTML/CSS** - Custom styling
        
        **Backend:**
        - **Python 3.11+** - Main language
        - **NumPy** - Efficient numerical calculations
        - **Python Math** - Precise geometric calculations
        
        **Development:**
        - **VS Code** - Primary development IDE
        - **Claude Sonnet 4** - AI agent for technical assistance
        - **Notebook LLM** - Study and prototyping tool
        """)
    
    with tech_col2:
        st.markdown("""
        **Architecture:**
        - Modular and scalable
        - Clear separation of responsibilities
        - Reusable components
        - Easy maintenance
        
        **Deployment & DevOps:**
        - **Docker** - Application containerization
        - **Docker Compose** - Container orchestration
        - Cloud-ready (Google Cloud Run)
        - CI/CD pipeline
        - Horizontal scalability
        
        **Version Control:**
        - **Git** - Version control system
        - **GitHub** - Remote repository and collaboration
        """)
    
    st.markdown("---")
    
    # Standards and references
    st.markdown("### Standards and References")
    
    st.markdown("""
    This tool implements calculations and validations based on:
    
    **NASA Human Integration Design Handbook (HIDH):**
    - NASA/SP-2010-3407 - Habitable volume and space requirements
    - NASA-STD-3001 - Human Systems Integration Requirements
    - NASA Technical Standards - Habitability and Human Factors
    
    **Reference Missions:**
    - **International Space Station (ISS)** - Long-duration operational data
    - **Skylab** - First studies of habitable volume
    - **Mir Space Station** - Experiências soviéticas/russas
    - **Apollo/Gemini** - Short-duration missions
    
    **Programas Futuros:**
    - **Artemis Gateway** - Lunar orbital station
    - **Mars Design Reference Architectures** - Martian missions
    - **Commercial LEO Destinations** - Commercial space stations
    
    **Scientific Publications:**
    - "Volume and Surface Area Allocations for Crew Habitability"
    - "Psychological and Human Factors in Long Duration Spaceflight"
    - "Architectural Approaches to Space Habitat Design"
    """)
    
    st.markdown("---")
    
    # Contributions
    st.markdown("### How to Contribute")
    
    contribute_col1, contribute_col2 = st.columns(2)
    
    with contribute_col1:
        st.markdown("""
        **For Developers:**
        - Contribute code on GitHub
        - Report bugs and issues
        - Suggest new features
        - Improve documentation
        - Add automated tests
        
        **Required Technologies:**
        - Python 3.11+
        - Streamlit
        - Git/GitHub
        - Docker (optional)
        """)
    
    with contribute_col2:
        st.markdown("""
        **For Non-Developers:**
        - Share your designs
        - Give usability feedback
        - Contribute with documentation
        - Suggest UI/UX improvements
        - Promote the tool
        
        **Contribution Areas:**
        - Calculation validation
        - Real use cases
        - Tutorials and guides
        - Translations
        """)
    
    st.markdown("---")
    
    # License
    st.markdown("### License and Usage")
    
    st.markdown("""
    **License:** MIT License
    
    This project is **open-source** and free for use, modification and distribution, provided that 
    original credits are maintained.
    
    **You can:**
    - Use commercially
    - Modify the code
    - Distribute copies
    - Private use
    - Create derivative works
    
    **You must:**
    - Include the original license
    - Maintain copyright credits
    - Document significant changes
    
    **Disclaimer:**
    
    This tool is provided "as is" for educational and conceptual design purposes. 
    **It does not replace professional structural, thermal or systems analysis** required 
    for real flight projects. Always consult qualified engineers and follow applicable 
    aerospace regulations for production designs.
    """)
    
    st.markdown("---")
    
    # Contact and support
    st.markdown("### Contact and Support")
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        **Project Repository:**
        - GitHub: [Habitat-Layout-Creator](https://github.com/kritgarb/Habitat-Layout-Creator)
        """)
    
    with contact_col2:
        st.markdown("""
        **Social Networks:**
        - LinkedIn: [Benjamin Vieira](https://www.linkedin.com/in/garbkrit/)
        - LinkedIn: [Alice Araujo](https://www.linkedin.com/in/alice-araujo-892258238)
        """)
    
    st.markdown("---")
    
    # Acknowledgments
    st.markdown("### Acknowledgments")
    
    st.markdown("""
    This project would not be possible without:
    
    **NASA** - For decades of research in space habitability and for making publicly available 
    the HIDH standards that form the basis of this tool.
    
    **Innovation Center and Grupo Tiradentes** - For institutional support and fostering technological innovation.
    
    **Leonardo Sales** - Local organizer of the NASA Space Apps Challenge, for fostering technology in 
    Northeast Brazil and encouraging young people in this innovation environment.
    
    **Open-Source Community** - Streamlit, Plotly, and countless Python libraries that make 
    development fast and accessible.
    
    **Researchers and Engineers** - Whose work in space architecture, human factors and 
    life support systems inform the algorithms and validations of this tool.
    
    **You** - For using this tool and contributing to the future of space exploration!
    """)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: rgba(99, 102, 241, 0.1); border-radius: 10px; margin-top: 2rem;'>
        <h3 style='color: #6366f1;'>Let's Build the Space Future Together!</h3>
        <p style='color: #E2E8F0; font-size: 1.1rem; line-height: 1.8;'>
            Every great journey begins with a small step. Your design could be the next habitat 
            to shelter humanity among the stars.
        </p>
        <p style='color: #A0AEC0; margin-top: 1rem;'>
            Made with love for the space community | © 2025 ENTERPRISE
        </p>
    </div>
    """, unsafe_allow_html=True)
