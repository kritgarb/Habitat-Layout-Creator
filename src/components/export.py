"""
Componente de exportação de dados
"""
import streamlit as st
import json
from datetime import datetime


def render_export(habitat_data: dict):
    """
    Renderiza a seção de exportação de dados.
    
    Args:
        habitat_data: Dicionário completo com todos os dados do habitat
    """
    st.markdown("---")
    st.markdown("## Export Design")
    
    col1, col2 = st.columns(2)
    
    with col1:
        json_data = json.dumps(habitat_data, indent=2, ensure_ascii=False)
        st.download_button(
            label="Download JSON Data",
            data=json_data,
            file_name=f"habitat_layout_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    
    with col2:
        st.info("💡 Tip: Use browser screenshot tool to capture PNG of visualizations above!")


def create_habitat_data_dict(config: dict, total_volume: float, floor_area: float,
                             nhv: float, nhv_per_person: float, total_water: float,
                             zones: dict, issues: list, 
                             nhv_per_person_valid: bool, floor_area_valid: bool) -> dict:
    """
    Cria o dicionário de dados do habitat para exportação.
    
    Args:
        config: Configurações do habitat
        total_volume: Volume total (m³)
        floor_area: Área de piso (m²)
        nhv: Net Habitable Volume (m³)
        nhv_per_person: NHV por pessoa (m³)
        total_water: Água total (litros)
        zones: Áreas das zonas (m²)
        issues: Lista de problemas de validação
        nhv_per_person_valid: Se NHV está OK
        floor_area_valid: Se área está OK
    
    Returns:
        Dicionário com todos os dados estruturados
    """
    return {
        "metadata": {
            "created_at": datetime.now().isoformat(),
            "project": "Habitat Layout Creator - NASA Space Apps 2025"
        },
        "habitat": {
            "shape": config["shape"],
            "dimensions": config["dimensions"],
            "volume_m3": round(total_volume, 2),
            "floor_area_m2": round(floor_area, 2),
            "nhv_m3": round(nhv, 2),
            "nhv_per_person_m3": round(nhv_per_person, 2)
        },
        "mission": {
            "crew_size": config["crew_size"],
            "duration_days": config["mission_duration"],
            "destination": config["destination"],
            "total_water_liters": round(total_water, 2)
        },
        "zones": {zone: round(area, 2) for zone, area in zones.items()},
        "validation": {
            "meets_nhv_requirement": nhv_per_person_valid,
            "meets_floor_area_requirement": floor_area_valid,
            "issues": issues
        }
    }
