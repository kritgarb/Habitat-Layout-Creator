"""
Página de visualização 3D com configurações e explicações
"""
import streamlit as st
from src.components.config_panel import render_config_panel
from src.visualizations.layout_3d import create_3d_habitat_view
from src.config.constants import ZONE_COLORS, ZONE_NAMES, MIN_FLOOR_AREA_PER_PERSON
from src.utils.calculations import (
    calculate_cylinder_volume, calculate_cylinder_floor_area,
    calculate_box_volume, calculate_box_floor_area,
    calculate_nhv, allocate_zones
)
from src.utils.nasa_calculations import calculate_nhv_per_person


def render_layout_3d_page():
    """Renderiza a página de Layout 3D"""
    
    st.markdown("# Layout 3D - Visualização Tridimensional")
    
    # Explicação da visualização 3D
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(168, 85, 247, 0.1)); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #8b5cf6; margin-bottom: 2rem;'>
        <h3 style='color: #8b5cf6; margin-top: 0;'>O que é a Visualização 3D?</h3>
        <p style='color: #E2E8F0; line-height: 1.8;'>
            A visualização 3D mostra o <strong>volume completo</strong> do seu habitat espacial, 
            permitindo que você veja as <strong>dimensões reais</strong> e a <strong>distribuição das zonas</strong> 
            em três dimensões.
        </p>
        <ul style='color: #E2E8F0; line-height: 1.8;'>
            <li><strong>Interatividade:</strong> Clique e arraste para rotacionar o modelo. Use a roda do mouse 
            para zoom. Explore todos os ângulos do seu habitat.</li>
            <li><strong>Zonas Divididas:</strong> Planos coloridos dividem o habitat nas zonas funcionais. 
            Cada cor corresponde a uma zona específica (veja a legenda).</li>
            <li><strong>Perspectiva Real:</strong> A visualização mantém as proporções exatas do seu design, 
            dando uma noção clara do espaço interno disponível.</li>
            <li><strong>Estrutura:</strong> O contorno externo mostra a forma do habitat (cilindro ou caixa retangular) 
            e suas dimensões totais.</li>
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
        st.metric("Volume Total", f"{total_volume:.1f} m³")
        st.caption(f"NHV: {nhv:.1f} m³")
    
    with metric_col2:
        st.metric("NHV/Pessoa", f"{nhv_per_person:.1f} m³")
        delta_nhv = nhv_per_person - nhv_required_per_person
        st.caption(f"NASA: {nhv_required_per_person:.1f} m³")
    
    with metric_col3:
        if config["shape"] == "Cylinder":
            st.metric("Dimensões", f"D{config['dimensions']['diameter']}m x H{config['dimensions']['height']}m")
            st.caption("Cilindro")
        else:
            st.metric("Dimensões", f"{config['dimensions']['length']}m × {config['dimensions']['width']}m × {config['dimensions']['height']}m")
            st.caption("Retângulo")
    
    with metric_col4:
        st.metric("Estrutura", config['structure_type'])
        st.caption(f"Gravidade: {config['gravity_env']}")
    
    st.markdown("---")
    
    # Visualização 3D
    st.markdown("### Modelo 3D Interativo")
    
    st.info("Dica: Clique e arraste para rotacionar. Use a roda do mouse para zoom. Clique duas vezes para resetar a visualização.")
    
    fig_3d = create_3d_habitat_view(
        config["shape"], config["dimensions"], zones,
        ZONE_COLORS, ZONE_NAMES
    )
    st.plotly_chart(fig_3d, width="stretch")
    
    # Legenda e explicação das zonas
    st.markdown("---")
    st.markdown("### Legenda de Zonas")
    
    legend_cols = st.columns(3)
    for idx, (zone_id, area) in enumerate(zones.items()):
        with legend_cols[idx % 3]:
            percentage = (area / total_zone_area) * 100
            volume_per_zone = (total_volume / len(zones))  # Simplificação
            st.markdown(f"""
            <div style='background: {ZONE_COLORS[zone_id]}20; padding: 1rem; border-radius: 8px; 
                        border-left: 4px solid {ZONE_COLORS[zone_id]}; margin-bottom: 1rem;'>
                <div style='color: {ZONE_COLORS[zone_id]}; font-weight: 700; font-size: 1.1rem;'>
                    {ZONE_NAMES[zone_id]}
                </div>
                <div style='color: #E2E8F0; font-size: 1.1rem; margin: 0.5rem 0;'>
                    Área: {area:.1f} m² ({percentage:.1f}%)
                </div>
                <div style='color: #A0AEC0;'>
                    Volume estimado: ~{volume_per_zone:.1f} m³
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Dicas de interpretação
    st.markdown("---")
    st.markdown("### Como Interpretar o Modelo 3D")
    
    tip_col1, tip_col2 = st.columns(2)
    
    with tip_col1:
        st.markdown("""
        **Análise Volumétrica:**
        - O volume 3D é crítico para ambientes pressurizados
        - NHV (Net Habitable Volume) exclui equipamentos e estruturas
        - Maior volume = mais conforto psicológico para tripulação
        - NASA recomenda mínimos baseados em duração da missão
        """)
        
        st.markdown("""
        **Referências NASA:**
        - Missões curtas (30 dias): 12.7 m³/pessoa
        - Missões médias (90 dias): 16.7 m³/pessoa  
        - Missões longas (360+ dias): 22.5 m³/pessoa
        """)
    
    with tip_col2:
        st.markdown("""
        **Rotação e Exploração:**
        - Visualize o habitat de todos os ângulos
        - Verifique proporções e distribuição espacial
        - Considere fluxo de movimento entre zonas
        - Avalie adequação para atividades específicas
        """)
        
        st.markdown("""
        **Fatores de Usabilidade:**
        - Fator de usabilidade reduz volume total para NHV
        - Estruturas rígidas: 70-80% (mais equipamento)
        - Estruturas infláveis: 85-90% (menos equipamento)
        """)
    
    # Validações
    st.markdown("---")
    st.markdown("### Validações NASA")
    
    val_col1, val_col2 = st.columns(2)
    
    with val_col1:
        if nhv_per_person >= nhv_required_per_person:
            st.success(f"NHV por pessoa ({nhv_per_person:.1f} m³) atende ao padrão NASA ({nhv_required_per_person:.1f} m³)")
        else:
            st.error(f"NHV por pessoa ({nhv_per_person:.1f} m³) está abaixo do mínimo NASA ({nhv_required_per_person:.1f} m³)")
            st.caption(f"Déficit: {nhv_required_per_person - nhv_per_person:.1f} m³/pessoa")
    
    with val_col2:
        if floor_area_per_person >= MIN_FLOOR_AREA_PER_PERSON:
            st.success(f"Área de piso por pessoa ({floor_area_per_person:.1f} m²) atende ao padrão NASA ({MIN_FLOOR_AREA_PER_PERSON} m²)")
        else:
            st.error(f"Área de piso por pessoa ({floor_area_per_person:.1f} m²) está abaixo do mínimo NASA ({MIN_FLOOR_AREA_PER_PERSON} m²)")
            st.caption(f"Déficit: {MIN_FLOOR_AREA_PER_PERSON - floor_area_per_person:.1f} m²/pessoa")
