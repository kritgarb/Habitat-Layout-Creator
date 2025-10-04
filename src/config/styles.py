"""
CSS customizado para a interface Streamlit
"""

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    .main {
        background: linear-gradient(135deg, #0F1419 0%, #1a1f2e 100%);
        color: #E8EAED;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1f2e 0%, #0F1419 100%);
        border-right: 1px solid #2d3748;
    }
    
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
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
