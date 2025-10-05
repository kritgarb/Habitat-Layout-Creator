"""
Documentation page with complete usage guide
"""
import streamlit as st


def render_documentation_page():
    """Renders the Documentation page"""
    
    st.markdown("# Documentation - Complete Usage Guide")
    
    # Introduction
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1)); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #3b82f6; margin-bottom: 2rem;'>
        <h3 style='color: #3b82f6; margin-top: 0;'>Welcome to Documentation</h3>
        <p style='color: #E2E8F0; line-height: 1.8;'>
            This comprehensive guide will help you master the <strong>AEGIS Habitat Layout Creator</strong>, 
            from basic concepts to advanced space design techniques.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Table of contents
    st.markdown("## Table of Contents")
    st.markdown("""
    1. [Getting Started](#1-getting-started)
    2. [Fundamental Concepts](#2-fundamental-concepts)
    3. [Step-by-Step Guide](#3-step-by-step-guide)
    4. [Configuration Parameters](#4-configuration-parameters)
    5. [Interpreting Visualizations](#5-interpreting-visualizations)
    6. [Understanding NASA Metrics](#6-understanding-nasa-metrics)
    7. [Resource and Life Support Requirements](#6-5-resource-and-life-support-requirements)
    8. [Tips and Best Practices](#7-tips-and-best-practices)
    9. [Data Export](#8-data-export)
    10. [Troubleshooting](#9-troubleshooting)
    11. [NASA Documentation](#10-nasa-documentation)
    """)
    
    st.markdown("---")
    
    # Section 1: Getting Started
    with st.expander("### 1. Getting Started", expanded=True):
        st.markdown("""
        #### What is the AEGIS Habitat Layout Creator?
        
        AEGIS is an interactive design tool for creating and validating space habitat layouts 
        following **NASA Human Integration Design Handbook (HIDH)** standards. 
        
        #### Who should use it?
        - Aerospace engineers
        - Space systems designers
        - Space architecture researchers
        - Engineering and space science students
        - Space exploration enthusiasts
        
        #### Requirements
        - Modern web browser (Chrome, Firefox, Edge, Safari)
        - Internet connection (for interactive Plotly graphics)
        - Basic knowledge of space concepts (optional but recommended)
        
        #### First Steps
        1. Navigate to the **Home** page to understand the tool
        2. Read the terms glossary to familiarize yourself with terminology
        3. Choose between **2D Layout** or **3D Layout** to start your design
        4. Configure basic habitat parameters
        5. Visualize and validate your design in **NASA Metrics**
        """)
    
    # Section 2: Fundamental Concepts
    with st.expander("### 2. Fundamental Concepts"):
        st.markdown("""
        #### Net Habitable Volume (NHV)
        - **What it is:** Interior volume usable by astronauts, excluding equipment and structures
        - **Formula:** NHV = Total Volume × Usability Factor
        - **Importance:** Directly related to crew psychological comfort and performance
        - **NASA Standards:** Ranges from 12.7 m³/person (30 days) to 27.9 m³/person (1+ year)
        
        #### Habitat Shapes
        
        **Cylindrical:**
        - More efficient for pressurization (uniform stress distribution)
        - Better for launch (fits in cylindrical payloads)
        - Volume = π × (Diameter/2)² × Height
        - Example: ISS modules, SpaceX Starship
        
        **Rectangular (Box):**
        - More flexible for interior layouts
        - Better floor area utilization (right corners)
        - Volume = Length × Width × Height
        - Example: TransHab concept, B330 modules
        
        #### Structure Types
        
        **Rigid:**
        - Permanent metallic structure
        - Greater protection against radiation and micrometeoroids
        - More integrated equipment = lower usability factor (70-80%)
        - Example: ISS, Skylab
        
        **Inflatable:**
        - Advanced fabric structure (Kevlar, Vectran)
        - Compact during launch, expands in space
        - Higher usability factor (85-90%)
        - Example: Bigelow BEAM, Sierra Space LIFE
        
        #### Gravitational Environments
        
        **Microgravity (0g):**
        - ISS, Earth orbit
        - All surfaces are usable
        - 3D volume is more critical than floor area
        
        **Lunar Gravity (0.165g):**
        - Moon surface
        - Movement still "floating" but with orientation
        - Balance between volume and floor area
        
        **Martian Gravity (0.38g):**
        - Mars surface
        - Closer to terrestrial design
        - Floor area is primary
        
        #### Functional Zones
        
        Habitat divisions by function:
        - **Sleep:** Privacy, rest
        - **Work:** Laboratories, controls
        - **Hygiene:** Bathroom, shower
        - **Food:** Kitchen, meals
        - **Exercise:** Fitness equipment
        - **Recreation:** Leisure, relaxation
        - **Storage:** Supplies, equipment
        - **Medical:** First aid, examinations
        """)
    
    # Section 3: Step-by-Step Guide
    with st.expander("### 3. Step-by-Step Guide"):
        st.markdown("""
        #### Step 1: Define Mission Parameters
        
        1. **Choose habitat shape:**
           - Cylindrical for structural efficiency
           - Rectangular for layout flexibility
        
        2. **Select structure type:**
           - Rigid for critical missions with many systems
           - Inflatable to maximize volume with minimal mass
        
        3. **Configure dimensions:**
           - **Cylinder:** Diameter (3-8m typical) and Height (4-10m typical)
           - **Rectangle:** Length, Width, Height (4-10m each)
           - Tip: Start with standard dimensions and adjust as needed
        
        4. **Define crew and mission:**
           - Crew size: 4-6 people typical
           - Duration: 30 days (short) to 360+ days (long)
           - Tip: Duration drastically affects NHV requirements
        
        5. **Choose gravitational environment:**
           - Microgravity: ISS, orbit
           - Lunar: Lunar base
           - Martian: Martian base
        
        #### Step 2: Select Functional Zones
        
        1. **Select necessary zones:**
           - Recommended minimum: Sleep, Work, Hygiene
           - Ideal: 5-7 zones for complete functionality
        
        2. **Adjust custom areas (optional):**
           - Leave blank for automatic balanced distribution
           - Or enter specific m² for precise control
           - Tip: Sleep and Work are usually the largest zones
        
        3. **Validate the sum:**
           - Tool warns if custom areas exceed available area
           - Adjust values or remove zones if necessary
        
        #### Step 3: Visualize the Design
        
        1. **2D Layout (Floor Plan):**
           - See zone distribution from top view
           - Cylinders: circular sectors
           - Rectangles: optimized grid
           - Interaction: Hover for details of each zone
        
        2. **3D Layout (Three-Dimensional Model):**
           - Visualize complete habitat volume
           - Interaction: Click and drag to rotate
           - Use mouse wheel for zoom
           - Double click to reset view
        
        #### Step 4: Analyze the Metrics
        
        1. **Access NASA Metrics:**
           - Complete dashboard with all quantitative metrics
        
        2. **Verify compliance:**
           - NHV per person vs. NASA standard
           - Floor area per person vs. 10 m² minimum
           - Adequate zone distribution
        
        3. **Identify problems:**
           - Red metrics indicate non-compliance
           - Read detailed explanations of each metric
           - Adjust configurations as needed
        
        #### Step 5: Iterate and Refine
        
        1. **Experiment with variations:**
           - Test different shapes and dimensions
           - Compare rigid vs. inflatable structures
           - Vary number and size of zones
        
        2. **Optimize for your objectives:**
           - Maximize NHV for long missions
           - Minimize area for mass efficiency
           - Balance functionality vs. resources
        
        3. **Document your design:**
           - Use JSON export to save configurations
           - Capture screenshots of visualizations
           - Note design decisions and trade-offs
        """)
    
    # Section 4: Configuration Parameters
    with st.expander("### 4. Configuration Parameters"):
        st.markdown("""
        #### Habitat Shape
        - **Options:** Cylinder, Rectangular
        - **Impact:** Determines volume and area formulas
        - **Recommendation:** Cylinder for efficient pressurization
        
        #### Structure Type
        - **Options:** Rigid, Inflatable
        - **Impact:** Affects usability factor (70-90%)
        - **Recommendation:** Rigid for durability, Inflatable for volume
        
        #### Dimensions
        
        **Cylinder:**
        - **Diameter:** 3-8 meters typical
          - Smaller: easier launch
          - Larger: more interior space
        - **Height:** 4-10 meters typical
          - Affects volume proportionally
          - Consider ceiling height (2-2.5m minimum)
        
        **Rectangle:**
        - **Length/Width/Height:** 4-10 meters typical
        - Consider aspect ratio (L:W:H)
        - Avoid very disproportionate dimensions
        
        #### Crew Size
        - **Range:** 1-12 people
        - **Typical:** 4-6 people
        - **Impact:** Divisor for per capita metrics
        - **Consideration:** More people = more resources, more social complexity
        
        #### Mission Duration
        - **Range:** 1-1000+ days
        - **Categories:**
          - Short: ≤30 days
          - Medium: 31-180 days
          - Long: 181-360 days
          - Very long: 360+ days
        - **Impact:** Determines required NHV per person
        - **Consideration:** Long missions require more space for mental health
        
        #### Gravitational Environment
        - **Options:** 
          - Microgravity (0g)
          - Lunar Gravity (0.165g)
          - Martian Gravity (0.38g)
        - **Impact:** Influences space usage and equipment orientation
        - **Consideration:** Microgravity uses 3D volume; gravity uses floor area
        
        #### Usability Factor
        - **Range:** 0.60-0.95 (60%-95%)
        - **Rigid:** 0.70-0.80 typical
        - **Inflatable:** 0.85-0.90 typical
        - **Impact:** Direct NHV multiplier
        - **Recommendation:** Use conservative values (0.70-0.75) for preliminary designs
        
        #### Zone Selection
        - **Minimum:** 1 zone
        - **Recommended:** 3-7 zones
        - **Custom Areas:** Optional, in m²
        - **Auto-distribution:** Tool automatically calculates if not specified
        """)
    
    # Section 5: Interpreting Visualizations
    with st.expander("### 5. Interpreting Visualizations"):
        st.markdown("""
        #### 2D Visualization (Floor Plan)
        
        **Cylindrical Habitats:**
        - Zones appear as circular sectors (slices)
        - Central circle = common corridor
        - Slice size = zone area
        - Unique colors identify each zone
        
        **Rectangular Habitats:**
        - Zones organized in optimized grid
        - Grid lines for spatial reference
        - Each rectangle = one zone
        - Proportions approximate real areas
        
        **Interactivity:**
        - Hover: See name, area, percentage
        - Legends: Colors and zones identified
        - Responsive: Adapts to screen size
        
        **What to look for:**
        - Balanced zone distribution
        - Zones large enough for function
        - Logical separation (e.g., sleep far from exercise)
        
        #### 3D Visualization (Three-Dimensional Model)
        
        **Model Elements:**
        - Outer contour = habitat shape
        - Colored planes = zone divisions
        - Colors = legend correspondence
        - Axes = spatial reference (X, Y, Z)
        
        **Interactive Controls:**
        - **Rotation:** Click and drag
        - **Zoom:** Mouse wheel or pinch on touch
        - **Pan:** Right click and drag (or Shift + click)
        - **Reset:** Double click on visualization
        - **Legend:** Click items to show/hide zones
        
        **Viewing Angles:**
        - Front view: See height and width
        - Side view: See depth
        - Top view: See floor plan in 3D
        - Isometric: See general proportions
        
        **What to look for:**
        - Realistic habitat proportions
        - Apparent volume of each zone
        - Spatial relationships between zones
        - Suitability for crew number
        """)
    
    # Section 6: Understanding NASA Metrics
    with st.expander("### 6. Understanding NASA Metrics"):
        st.markdown("""
        #### Total Volume
        - Complete geometric volume of habitat
        - Includes equipment and structure space
        - Basis for NHV calculation
        - **Formulas:**
          - Cylinder: π × r² × h
          - Rectangle: L × W × H
        
        #### Net Habitable Volume (NHV)
        - Volume usable by crew
        - NHV = Total Volume × Usability Factor
        - Most important metric for comfort
        - **NASA Standards by duration:**
          - ≤30 days: 12.7 m³/person
          - 31-90 days: 16.7 m³/person
          - 91-180 days: 20.0 m³/person
          - 181-360 days: 22.5 m³/person
          - &gt;360 days: 27.9 m³/person
        
        #### NHV per Person
        - Total NHV divided by crew size
        - Directly compares to NASA standards
        - Key indicator of design adequacy
        - **Interpretation:**
          - Above standard: Excellent
          - At standard: Adequate
          - Below standard: Requires revision
        
        #### Floor Area
        - Horizontal area for circulation and work
        - Critical for partial or full gravity
        - **NASA Standard:** Minimum 10 m²/person
        - **Formulas:**
          - Cylinder: π × r²
          - Rectangle: L × W
        
        #### Floor Area per Person
        - Total area divided by crew size
        - Important for density and mobility
        - **Interpretation:**
          - &gt;15 m²/person: Spacious
          - 10-15 m²/person: Adequate
          - &lt;10 m²/person: Congested
        
        #### Zone Distribution
        - Number and size of functional zones
        - Diversity indicates functionality
        - Areas per zone should be appropriate
        - **Recommendations per zone:**
          - Sleep: 2-4 m²/person
          - Work: 3-5 m²/person
          - Hygiene: 1.5-2 m²/person
          - Food: 1-2 m²/person
          - Exercise: 3-4 m²/person
          - Recreation: 2-3 m²/person
          - Storage: 1-2 m²/person
          - Medical: 2-3 m²/person
        
        #### Overall Compliance
        - Summary of all validations
        - Green: Meets standards
        - Red: Requires attention
        - Deficits quantified for correction
        """)
    
    # Section 6.5: Resource Requirements and Life Support
    with st.expander("### 6.5. Resource Requirements and Life Support"):
        st.markdown(r"""
        #### Water Requirements
        
        **Potable Water (Hydration/Consumption):**
        - Minimum of $\mathbf{2.0 \text{ kg}}$ of potable water per crew member per mission day for ingestion
        - Essential for hydration and bodily functions
        - Must be potable and contaminant-free
        
        **Water for Food Rehydration:**
        - Approximately $\mathbf{0.5 \text{ kg}}$ per crew member per mission day
        - Necessary for preparing freeze-dried foods
        - Temperature and quality controlled
        
        **Water for Extravehicular Activities (EVA):**
        - Additionally, $\mathbf{0.24 \text{ kg}}$ of water per hour of EVA
        - Above nominal water provision
        - Recommended to avoid dehydration during intense activities
        
        **Total Water per Person/Day:**
        - **Nominal:** 2.5 kg/day (2.0 + 0.5)
        - **With EVAs:** Add 0.24 kg per hour of EVA
        
        #### Oxygen Requirements
        
        **Oxygen Production via Plants:**
        - About $\mathbf{20-25 \text{ m}^2}$ of crops are needed to provide $\text{O}_2$ for one human
        - Bioregenerative systems can reduce resupply dependency
        - Plants also provide psychological benefits
        
        **Human Consumption:**
        - Approximately 0.82 kg of $\text{O}_2$ per person per day
        - Production of 1.0 kg of $\text{CO}_2$ per person per day
        
        #### Food Requirements
        
        **Food Production (Calories):**
        - About $\mathbf{50 \text{ m}^2}$ are needed to provide dietary calories for one human
        - Based on 2500 kcal/person/day
        - Vertical farming systems can optimize space
        
        **Food Mass:**
        - Approximately 1.8 kg of food per person per day
        - Freeze-dried foods reduce mass and volume
        
        #### Crew Health
        
        **Body Mass Loss:**
        - In long-duration ISS missions, an average loss of $\mathbf{2.4\%}$ of body weight was observed every 100 days
        - Related to: loss of appetite, insufficient exercise, stress
        - Countermeasures: daily exercise (2h), adequate nutrition, medical monitoring
        
        **Design Implications:**
        - Exercise zone is **critical** for long missions
        - Recommended minimum area: 3-4 m²/person
        - Equipment: treadmill, ergometric bike, resistance
        
        #### Resource Summary per Person/Day
        
        | Resource | Quantity | Unit |
        |---------|----------|------|
        | Water (potable) | 2.0 | kg |
        | Water (food) | 0.5 | kg |
        | Water (EVA) | 0.24 | kg/hour EVA |
        | Oxygen | 0.82 | kg |
        | Food | 1.8 | kg |
        | CO₂ produced | 1.0 | kg |
        | O₂ crop area | 20-25 | m² |
        | Food crop area | 50 | m² |
        
        **Note:** These values are for missions without advanced recycling systems. 
        ECLSS (Environmental Control and Life Support System) can significantly reduce 
        resupply needs through water and air recycling.
        """)
    
    # Section 7: Tips and Best Practices
    with st.expander("### 7. Tips and Best Practices"):
        st.markdown("""
        #### General Design
        
        **Do:**
        - Start with NASA standards and adjust as needed
        - Iterate multiple times before finalizing
        - Consider trade-offs (volume vs. mass vs. cost)
        - Document design decisions
        - Use conservative values for usability factor
        
        **Avoid:**
        - Minimizing space too much (comfort matters!)
        - Ignoring NASA standards without justification
        - Designs with only 1-2 zones (insufficient)
        - Extreme dimensions without structural validation
        - Overestimating usability factor (&gt;90%)
        
        #### Shape Selection
        
        **Use Cylinder when:**
        - Pressurization is critical
        - Launching in cylindrical payloads
        - Structural efficiency is priority
        - Mass must be minimized
        
        **Use Rectangle when:**
        - Layout flexibility is important
        - Connection with other modules
        - Corner utilization is advantageous
        - Modular design is necessary
        
        #### Sizing
        
        **For Small Crews (2-3 people):**
        - Cylinder: ⌀4-5m × H5-7m
        - Rectangle: 5×4×5m typical
        - Focus on zone multifunctionality
        
        **For Medium Crews (4-6 people):**
        - Cylinder: ⌀6-7m × H8-10m
        - Rectangle: 8×6×6m typical
        - Specialized zones important
        
        **For Large Crews (7+ people):**
        - Cylinder: ⌀8m × H10+m or multiple modules
        - Rectangle: 10×8×8m or multiple modules
        - Consider connected modular habitats
        
        #### Zone Allocation
        
        **Priorities by Duration:**
        
        **Short Missions (≤30 days):**
        1. Work (40%)
        2. Sleep (25%)
        3. Hygiene (15%)
        4. Food (10%)
        5. Storage (10%)
        
        **Medium Missions (31-180 days):**
        1. Work (30%)
        2. Sleep (25%)
        3. Exercise (15%)
        4. Food (10%)
        5. Hygiene (10%)
        6. Recreation (5%)
        7. Storage (5%)
        
        **Long Missions (&gt;180 days):**
        1. Work (25%)
        2. Sleep (25%)
        3. Exercise (15%)
        4. Recreation (10%)
        5. Food (10%)
        6. Hygiene (10%)
        7. Storage (3%)
        8. Medical (2%)
        
        #### Iterative Optimization
        
        **Recommended process:**
        1. Start with standard dimensions
        2. Check NASA compliance
        3. Identify largest deficit
        4. Adjust relevant parameter
        5. Revalidate metrics
        6. Repeat until compliance
        7. Refine for optimization
        
        **Quick adjustment parameters:**
        - Increase NHV: ↑ dimensions or ↑ usability factor
        - Increase floor area: ↑ diameter/length/width
        - Improve distribution: Adjust zone areas
        - Reduce mass: ↓ dimensions or use inflatable
        """)
    
    # Section 8: Data Export
    with st.expander("### 8. Data Export"):
        st.markdown("""
        #### Export Formats
        
        **JSON (JavaScript Object Notation):**
        - Machine-readable structured format
        - Contains all configurations and metrics
        - Ideal for archiving and sharing
        - Can be reimported (future feature)
        
        **JSON File Content:**
        ```json
        {
          "configuration": {
            "shape": "Cylinder",
            "structure": "Rigid",
            "dimensions": {...},
            "crew_size": 4,
            "mission_duration": 180,
            "gravity": "Microgravity",
            "usable_factor": 0.75
          },
          "metrics": {
            "total_volume": 123.45,
            "nhv": 92.59,
            "nhv_per_person": 23.15,
            "floor_area": 50.27,
            "floor_area_per_person": 12.57,
            ...
          },
          "zones": {
            "Sleep": 15.5,
            "Work": 20.3,
            ...
          },
          "validation": {
            "nhv_compliant": true,
            "floor_area_compliant": true
          }
        }
        ```
        
        #### How to Export
        
        1. Fully configure your habitat
        2. Validate all metrics
        3. Navigate to the export section (usually at the end of each page)
        4. Click the "Export Configuration (JSON)" button
        5. File will be downloaded automatically
        
        #### Using Exported Data
        
        **Documentation:**
        - Attach to design reports
        - Include in mission proposals
        - Use as baseline for iterations
        
        **Analysis:**
        - Import into analysis tools (Excel, Python, MATLAB)
        - Compare multiple designs
        - Generate trade-off charts
        
        **Sharing:**
        - Send to team members
        - Submit for reviews
        - Archive in project repositories
        
        **Traceability:**
        - Automatic timestamp
        - All design decisions captured
        - Reproducible for auditing
        
        #### Screenshots
        
        **2D/3D Visualizations:**
        - Use browser screenshot tool
        - Or operating system screenshot tool
        - High resolution recommended for presentations
        
        **Metrics:**
        - Capture complete dashboard
        - Include compliance validations
        - Use in reports and presentations
        """)
    
    # Section 9: Troubleshooting
    with st.expander("### 9. Troubleshooting"):
        st.markdown("""
        #### Common Problems and Solutions
        
        #### "NHV per person is below NASA standard"
        
        **Possible causes:**
        - Habitat dimensions too small
        - Usability factor too low
        - Crew too large for the volume
        - Mission duration too long for current NHV
        
        **Solutions:**
        1. Increase dimensions (diameter, height, length, width)
        2. Increase usability factor (if justifiable)
        3. Reduce crew size (if possible)
        4. Consider inflatable structure (higher usability factor)
        5. Use multiple connected modules
        
        #### "Floor area per person below minimum"
        
        **Possible causes:**
        - Insufficient diameter/length/width
        - Crew too large
        - Cylindrical shape with small diameter
        
        **Solutions:**
        1. Increase diameter (cylinder) or length/width (rectangle)
        2. Consider rectangular shape (more floor area per volume)
        3. Reduce crew size
        4. Check if excessive height is "wasting" volume
        
        #### "Sum of zone areas exceeds available area"
        
        **Possible causes:**
        - Custom areas sum more than total floor area
        - Data entry errors
        
        **Solutions:**
        1. Leave areas blank for automatic distribution
        2. Reduce custom area values
        3. Remove some zones
        4. Increase habitat dimensions for more floor area
        
        #### "2D or 3D visualization does not appear"
        
        **Possible causes:**
        - No zone selected
        - Connection error (Plotly requires internet)
        - Browser does not support WebGL (for 3D)
        
        **Solutions:**
        1. Select at least one functional zone
        2. Check internet connection
        3. Use modern browser (Chrome, Firefox, Edge updated)
        4. Enable WebGL in browser settings
        5. Disable extensions that block scripts
        
        #### "Metrics seem incorrect"
        
        **Possible causes:**
        - Inconsistent configuration
        - Outdated browser cache
        - Invalid input values
        
        **Solutions:**
        1. Reload page (F5 or Ctrl+R)
        2. Clear browser cache
        3. Check all input values
        4. Review formulas on metrics page
        5. Export JSON and check raw values
        
        #### "Interface is slow or freezing"
        
        **Possible causes:**
        - Too many zones selected (8+)
        - Slow internet connection
        - Browser with many open tabs
        - Limited hardware
        
        **Solutions:**
        1. Reduce number of zones to 5-7
        2. Close unnecessary browser tabs
        3. Temporarily disable browser extensions
        4. Use incognito mode
        5. Try different browser
        
        #### "Cannot export JSON"
        
        **Possible causes:**
        - Download blocker
        - Browser permissions
        - Downloads folder full
        
        **Solutions:**
        1. Allow downloads from site in browser settings
        2. Check disk space
        3. Try different browser
        4. Check default downloads folder
        
        #### Still Having Problems?
        
        If you continue to face difficulties:
        1. Check the **ℹ️ About** page for contact information
        2. Document the problem (screenshots, error messages)
        3. Note configurations that cause the problem
        4. Report through support channels
        """)
    
    st.markdown("---")
    
    # NASA Documentation
    with st.expander("### 10. NASA Documentation"):
        st.markdown("""
        #### Official Standards and References
        
        **NASA HIDH Standards**
        
        The Human Integration Design Handbook is the main reference for space habitat design:
        - [NASA HIDH Standards](https://www.nasa.gov/wp-content/uploads/2023/03/human-integration-design-handbook-revision-1.pdf?emrc=68e269191aa6f)
        - Covers volume requirements, ergonomics, human factors, and habitability
        - Foundation for all NHV and minimum area calculations in this tool
        
        **ISS Research Publications**
        
        Research and operational data from the International Space Station:
        - [ISS Research Publications](https://issnationallab.org/publications/)
        - Lessons learned from over 20 years of continuous operation
        - Real habitability data in microgravity
        
        **Human Spaceflight Standards**
        
        NASA technical standards for crewed spaceflight:
        - [Human Spaceflight Standards](https://www.nasa.gov/ochmo/human-spaceflight-and-aviation-standards/)
        - Safety, health, and crew performance requirements
        - Standards for space systems design
        
        #### How to Use This Documentation
        
        1. **For Validation:** Compare this tool's results with official values
        2. **For Deep Dive:** Read complete documents for additional context
        3. **For Research:** Use as starting point for more advanced studies
        4. **For Compliance:** Verify that your design meets NASA standards
        
        #### Related Scientific Publications
        
        - "Volume and Surface Area Allocations for Crew Habitability"
        - "Psychological and Human Factors in Long Duration Spaceflight"
        - "Architectural Approaches to Space Habitat Design"
        - "Defining the Net Habitable Volume for Long Duration Exploration Missions"
        """)
    
    st.markdown("---")
    
    st.markdown("---")
    
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: rgba(59, 130, 246, 0.1); border-radius: 10px;'>
        <p style='color: #3b82f6; font-size: 1.1rem;'>
            💡 <strong>Final Tip:</strong> Practice makes perfect! Experiment with different configurations 
            and learn how each parameter affects the overall design.
        </p>
    </div>
    """, unsafe_allow_html=True)
