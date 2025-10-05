"""
Página de visualização 2D com configurações e explicações
"""
import streamlit as st
from src.components.config_panel import render_config_panel
from src.visualizations.layout_2d import create_2d_layout_plotly
from src.config.constants import ZONE_COLORS, ZONE_NAMES, MIN_FLOOR_AREA_PER_PERSON
from src.utils.calculations import (
    calculate_cylinder_volume, calculate_cylinder_floor_area,
    calculate_box_volume, calculate_box_floor_area,
    calculate_nhv, allocate_zones
)
from src.utils.nasa_calculations import calculate_nhv_per_person


def render_layout_2d_page():
    """Renderiza a página de Layout 2D"""
    
    st.markdown("# Layout 2D - Planta Baixa do Habitat")
    
    # Explicação da visualização 2D
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(72, 187, 120, 0.1), rgba(56, 178, 172, 0.1)); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #48bb78; margin-bottom: 2rem;'>
        <h3 style='color: #48bb78; margin-top: 0;'>O que é a Planta Baixa 2D?</h3>
        <p style='color: #E2E8F0; line-height: 1.8;'>
            A visualização 2D mostra a <strong>planta baixa</strong> do seu habitat - uma visão de cima que 
            revela como as <strong>zonas funcionais</strong> estão distribuídas no espaço disponível.
        </p>
        <ul style='color: #E2E8F0; line-height: 1.8;'>
            <li><strong>Habitats Cilíndricos:</strong> As zonas são exibidas como setores circulares (fatias de pizza), 
            proporcionais às suas áreas. O círculo central representa o corredor comum.</li>
            <li><strong>Habitats Retangulares:</strong> As zonas são organizadas em um grid otimizado automaticamente, 
            com linhas de grade para referência espacial.</li>
            <li><strong>Cores:</strong> Cada zona tem uma cor única para fácil identificação. Passe o mouse sobre 
            qualquer zona para ver detalhes (nome, área, porcentagem).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Painel de configuração
    with st.expander("Configurar Habitat", expanded=True):
        config = render_config_panel()
    
    # Validar se há zonas selecionadas
    if not config["zone_areas"]:
        st.warning("Por favor, selecione pelo menos uma zona funcional na configuração acima.")
        st.stop()
    
    st.markdown("---")
    
    # Calcular métricas
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
    
    # Alocar zonas
    zones = allocate_zones(floor_area, config["crew_size"], config["zone_areas"])
    total_zone_area = sum(zones.values())
    
    # Resumo rápido
    st.markdown("### Resumo do Design")
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        forma_traduzida = "Cilíndrico" if config['shape'] == 'Cylinder' else "Retangular"
        st.metric("Forma", forma_traduzida)
    
    with metric_col2:
        st.metric("Área de Piso", f"{floor_area:.1f} m²")
        delta_floor = floor_area_per_person - MIN_FLOOR_AREA_PER_PERSON
        st.caption(f"{floor_area_per_person:.1f} m²/pessoa")
    
    with metric_col3:
        st.metric("Zonas", f"{len(zones)}")
        st.caption(f"{total_zone_area:.1f} m² total")
    
    with metric_col4:
        st.metric("Tripulação", f"{config['crew_size']} pessoas")
        st.caption(f"{config['mission_duration']} dias de missão")
    
    st.markdown("---")
    
    # Visualização 2D
    st.markdown("### Planta Baixa Interativa")
    
    fig_2d = create_2d_layout_plotly(
        zones, floor_area, config["shape"], config["dimensions"],
        ZONE_COLORS, ZONE_NAMES
    )
    st.plotly_chart(fig_2d, use_container_width=True)
    
    # Legenda e explicação das zonas
    st.markdown("---")
    st.markdown("### Legenda de Zonas")
    
    legend_cols = st.columns(3)
    for idx, (zone_id, area) in enumerate(zones.items()):
        with legend_cols[idx % 3]:
            percentage = (area / total_zone_area) * 100
            st.markdown(f"""
            <div style='background: {ZONE_COLORS[zone_id]}20; padding: 1rem; border-radius: 8px; 
                        border-left: 4px solid {ZONE_COLORS[zone_id]}; margin-bottom: 1rem;'>
                <div style='color: {ZONE_COLORS[zone_id]}; font-weight: 700; font-size: 1.1rem;'>
                    {ZONE_NAMES[zone_id]}
                </div>
                <div style='color: #E2E8F0; font-size: 1.3rem; font-weight: 700; margin: 0.5rem 0;'>
                    {area:.1f} m²
                </div>
                <div style='color: #A0AEC0;'>
                    {percentage:.1f}% do total | {area/config['crew_size']:.1f} m²/pessoa
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Dicas de interpretação
    st.markdown("---")
    st.markdown("### Como Interpretar a Planta Baixa")
    
    tip_col1, tip_col2 = st.columns(2)
    
    with tip_col1:
        st.markdown("""
        **Análise Espacial:**
        - Zonas maiores = mais área alocada para essa função
        - Distribuição equilibrada indica design balanceado
        - Verifique se há espaço suficiente para cada atividade
        - Compare com referências NASA (10 m²/pessoa mínimo)
        """)
    
    with tip_col2:
        st.markdown("""
        **Considerações Importantes:**
        - Zonas incompatíveis (ex: dormir + exercício) devem estar separadas
        - Higiene deve estar próxima aos quartos de dormir
        - Cozinha deve ser central para acesso fácil
        - Armazenamento deve ser distribuído estrategicamente
        """)
    
    # Validação básica
    if floor_area_per_person < MIN_FLOOR_AREA_PER_PERSON:
        st.error(f"Área de piso por pessoa ({floor_area_per_person:.1f} m²) está abaixo do mínimo NASA ({MIN_FLOOR_AREA_PER_PERSON} m²)")
    else:
        st.success(f"Área de piso por pessoa ({floor_area_per_person:.1f} m²) atende ao padrão NASA")
