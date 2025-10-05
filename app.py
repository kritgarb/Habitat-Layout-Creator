import base64
from pathlib import Path

import streamlit as st
from src.config.styles import CUSTOM_CSS
from src.pages.home import render_home_page
from src.pages.layout_2d import render_layout_2d_page
from src.pages.layout_3d import render_layout_3d_page
from src.pages.metrics import render_metrics_page
from src.pages.documentation import render_documentation_page
from src.pages.about import render_about_page
def _svg_to_data_uri(file_path: str) -> str:
    svg_path = Path(file_path)
    svg_content = svg_path.read_text(encoding="utf-8")
    encoded = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{encoded}"
st.set_page_config(
    page_title="AEGIS - NASA Space Apps 2025",
    page_icon="src/logo/AEGIS LOGO ICONE BRANCO OUTLINE.svg",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Header com Logo
encoded_logo = _svg_to_data_uri("src/logo/AEGIS LOGO BRANCO.svg")
st.markdown(f"""
<div style='text-align: center; padding: 0;'>
    <img src='{encoded_logo}' style='height: 100px; max-width: 100%;'/>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 0.5rem 0 0.5rem 0;'>
    <p style='font-size: 1.2rem; color: #A0AEC0; font-weight: 500;'>Toolbox for you to create and validate space habitat layouts</p>
</div>
""", unsafe_allow_html=True)

# Menu de Navegação Horizontal
st.markdown("---")
menu_col1, menu_col2, menu_col3, menu_col4, menu_col5, menu_col6, menu_col7 = st.columns(7)

with menu_col1:
    if st.button("Home", width="stretch", type="primary" if st.session_state.page == 'Home' else "secondary"):
        st.session_state.page = 'Home'
        st.rerun()

with menu_col2:
    if st.button("2D Layout", width="stretch", type="primary" if st.session_state.page == '2D Layout' else "secondary"):
        st.session_state.page = '2D Layout'
        st.rerun()

with menu_col3:
    if st.button("3D Layout", width="stretch", type="primary" if st.session_state.page == '3D Layout' else "secondary"):
        st.session_state.page = '3D Layout'
        st.rerun()

with menu_col4:
    if st.button("NASA Metrics", width="stretch", type="primary" if st.session_state.page == 'NASA Metrics' else "secondary"):
        st.session_state.page = 'NASA Metrics'
        st.rerun()

with menu_col5:
    if st.button("Documentation", width="stretch", type="primary" if st.session_state.page == 'Documentation' else "secondary"):
        st.session_state.page = 'Documentation'
        st.rerun()

with menu_col6:
    if st.button("About", width="stretch", type="primary" if st.session_state.page == 'About' else "secondary"):
        st.session_state.page = 'About'
        st.rerun()

with menu_col7:
    st.markdown("""
    <a href='https://www.figma.com/proto/PkdgT9qSERxvKzIaCu8QRi/Pessoal?node-id=364-1098&t=X75kdhaIlOCyGrVk-0&scaling=contain&content-scaling=fixed&starting-point-node-id=364%3A1098' target='_blank' style='text-decoration: none;'>
        <button style='
            width: 100%;
            padding: 0.375rem 0.75rem;
            background-color: transparent;
            color: rgb(250, 250, 250);
            border: 1px solid rgb(77, 77, 77);
            border-radius: 0.375rem;
            font-family: "Source Sans Pro", sans-serif;
            font-size: 14px;
            font-weight: 400;
            cursor: pointer;
            transition: all 0.15s ease;
        ' onmouseover='this.style.borderColor="rgb(167, 130, 240)"' onmouseout='this.style.borderColor="rgb(77, 77, 77)"'>
            Game Prototype
        </button>
    </a>
    """, unsafe_allow_html=True)

st.markdown("---")

# Page routing
if st.session_state.page == 'Home':
    render_home_page()

elif st.session_state.page == '2D Layout':
    render_layout_2d_page()

elif st.session_state.page == '3D Layout':
    render_layout_3d_page()

elif st.session_state.page == 'NASA Metrics':
    render_metrics_page()

elif st.session_state.page == 'Documentation':
    render_documentation_page()

elif st.session_state.page == 'About':
    render_about_page()

# Footer (on all pages)
st.markdown("---")
logo_assets = [
    ("src/img/LOGO_TIC.svg", "TIC"),
    ("src/img/LOGO_NSA.svg", "NSA"),
    ("src/img/LOGO_ENTERPRISE.svg", "Enterprise"),
]
logos_inline = "".join(
    f"<img src='{_svg_to_data_uri(path)}' alt='{alt}' style='height:48px; margin:0 10px;'/>"
    for path, alt in logo_assets
)

st.markdown(
    f"""
    <div style='text-align:center; padding: 1.5rem 0;'>
        <div style='display:flex; justify-content:center; align-items:center; gap:12px; flex-wrap:wrap;'>
            {logos_inline}
        </div>
        <p style='font-size: 1.1rem; font-weight: 600; color: #718096; margin: 1rem 0 0.25rem 0;'>AEGIS made by ENTERPRISE</p>
        <p style='font-size: 0.9rem; color: #718096; margin: 0;'>Your Home in Space: The Habitat Layout Creator - NASA Space Apps Challenge 2025</p>
    </div>
    """,
    unsafe_allow_html=True,
)
