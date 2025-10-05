"""
CSS customizado para a interface Streamlit
"""

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * { 
        font-family: 'Inter', sans-serif;
    }
    
    /* Fundo Espacial Simples e Estático */
    .stApp {
        background: 
            radial-gradient(2px 2px at 20% 30%, white, transparent),
            radial-gradient(2px 2px at 60% 70%, white, transparent),
            radial-gradient(1px 1px at 50% 50%, white, transparent),
            radial-gradient(1px 1px at 80% 10%, white, transparent),
            radial-gradient(2px 2px at 90% 60%, white, transparent),
            radial-gradient(1px 1px at 33% 80%, white, transparent),
            radial-gradient(1px 1px at 15% 90%, white, transparent),
            radial-gradient(1px 1px at 45% 20%, white, transparent),
            radial-gradient(2px 2px at 75% 85%, white, transparent),
            radial-gradient(1px 1px at 10% 60%, white, transparent),
            radial-gradient(2px 2px at 95% 25%, white, transparent),
            radial-gradient(1px 1px at 5% 45%, white, transparent),
            radial-gradient(1px 1px at 65% 15%, rgba(166, 140, 255, 0.6), transparent),
            radial-gradient(1px 1px at 25% 40%, rgba(102, 126, 234, 0.6), transparent),
            radial-gradient(2px 2px at 88% 75%, rgba(118, 75, 162, 0.6), transparent),
            radial-gradient(ellipse at 20% 50%, rgba(102, 126, 234, 0.1), transparent 50%),
            radial-gradient(ellipse at 80% 30%, rgba(118, 75, 162, 0.1), transparent 50%),
            #0a0e1a;
    }
    
    /* Container principal */
    .main {
        color: #E8EAED;
        min-height: 100vh;
    }
    
    /* Esconder header do Streamlit (botão Deploy, etc) */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Esconder toolbar superior */
    [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* Esconder menu hamburguer */
    #MainMenu {
        display: none !important;
    }
    
    /* Esconder footer "Made with Streamlit" */
    footer {
        display: none !important;
    }
    
    /* Sidebar com fundo espacial semi-transparente */
    [data-testid="stSidebar"] {
        background: rgba(10, 14, 26, 0.85) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(102, 126, 234, 0.3);
        position: relative;
        z-index: 2;
    }
    
    /* Títulos da Sidebar em roxo */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4 {
        color: #A68CFF !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(1px 1px at 15% 25%, rgba(255,255,255,0.3), transparent),
            radial-gradient(1px 1px at 65% 55%, rgba(255,255,255,0.2), transparent),
            radial-gradient(2px 2px at 85% 75%, rgba(166, 140, 255, 0.3), transparent),
            radial-gradient(1px 1px at 35% 85%, rgba(102, 126, 234, 0.2), transparent);
        opacity: 0.5;
        pointer-events: none;
        z-index: 0;
    }
    
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Botões do Menu Principal - Forçar cores roxas */
    button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(102, 126, 234, 0.4) !important;
        background: linear-gradient(135deg, #7c8ef5 0%, #8a5bb8 100%) !important;
    }
    
    button[kind="secondary"] {
        background: rgba(102, 126, 234, 0.1) !important;
        color: #A68CFF !important;
        border: 1px solid rgba(166, 140, 255, 0.3) !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    button[kind="secondary"]:hover {
        background: rgba(102, 126, 234, 0.2) !important;
        border-color: rgba(166, 140, 255, 0.5) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Alternativa - usando classe do Streamlit */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
    }
    
    .stButton > button[kind="secondary"] {
        background: rgba(102, 126, 234, 0.1) !important;
        color: #A68CFF !important;
        border: 1px solid rgba(166, 140, 255, 0.3) !important;
    }
    
    .stDownloadButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .zone-card {
        background: rgba(45, 55, 72, 0.6);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid;
        cursor: grab;
        transition: all 0.3s ease;
    }
    
    .zone-card:hover {
        transform: translateX(5px);
        background: rgba(45, 55, 72, 0.8);
    }
</style>
"""
