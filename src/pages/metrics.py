"""
Página de métricas NASA com configurações e explicações didáticas
"""
import streamlit as st
from src.components.config_panel import render_config_panel
from src.components.metrics import render_metrics
from src.config.constants import MIN_FLOOR_AREA_PER_PERSON
from src.utils.calculations import (
    calculate_cylinder_volume, calculate_cylinder_floor_area,
    calculate_box_volume, calculate_box_floor_area,
    calculate_nhv, allocate_zones
)
from src.utils.nasa_calculations import calculate_nhv_per_person


def render_metrics_page():
    """Renderiza a página de Métricas NASA"""
    
    st.markdown("# Métricas NASA - Análise Quantitativa")
    
    # Explicação das métricas NASA
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(236, 72, 153, 0.1), rgba(219, 39, 119, 0.1)); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #ec4899; margin-bottom: 2rem;'>
        <h3 style='color: #ec4899; margin-top: 0;'>O que são as Métricas NASA?</h3>
        <p style='color: #E2E8F0; line-height: 1.8;'>
            As métricas quantitativas da <strong>NASA Human Integration Design Handbook (HIDH)</strong> são 
            padrões científicos estabelecidos através de décadas de pesquisa em missões espaciais. 
            Elas garantem que o habitat seja <strong>seguro, funcional e psicologicamente saudável</strong> 
            para a tripulação.
        </p>
        <h4 style='color: #ec4899; margin-top: 1.5rem;'>Por que essas métricas importam?</h4>
        <ul style='color: #E2E8F0; line-height: 1.8;'>
            <li><strong>Saúde Física:</strong> Espaço insuficiente causa problemas de mobilidade, fadiga e 
            aumento de risco de acidentes.</li>
            <li><strong>Bem-estar Psicológico:</strong> Ambientes confinados demais aumentam estresse, conflitos 
            interpessoais e deterioração do desempenho da equipe.</li>
            <li><strong>Eficiência Operacional:</strong> Layouts mal dimensionados reduzem produtividade e 
            dificultam atividades diárias críticas.</li>
            <li><strong>Segurança de Missão:</strong> Padrões NASA são baseados em dados de ISS, Skylab, Mir 
            e outras missões reais.</li>
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
    
    # Calcular água necessária
    total_water = config["crew_size"] * config["mission_duration"] * 2.5  # 2.5 kg/pessoa/dia
    
    # Alocar zonas
    zones = allocate_zones(floor_area, config["crew_size"], config["zone_areas"])
    
    # Dashboard de métricas
    st.markdown("### Dashboard Completo de Métricas")
    render_metrics(
        total_volume=total_volume,
        floor_area=floor_area,
        nhv=nhv,
        nhv_per_person=nhv_per_person,
        floor_area_per_person=floor_area_per_person,
        crew_size=config["crew_size"],
        total_water=total_water,
        mission_duration=config["mission_duration"],
        min_nhv=nhv_required_per_person,
        min_floor_area=MIN_FLOOR_AREA_PER_PERSON
    )
    
    st.markdown("---")
    
    # Explicações didáticas das métricas principais
    st.markdown("### Guia de Interpretação das Métricas")
    
    # NHV
    with st.expander("Net Habitable Volume (NHV) - Volume Habitável Líquido", expanded=True):
        st.markdown(f"""
        **Definição:**  
        O NHV é o volume interno **realmente utilizável** pelos astronautas, excluindo espaço ocupado 
        por equipamentos, sistemas de suporte de vida, armazenamento e estruturas.
        
        **Fórmula:**
        ```
        NHV = Volume Total × Fator de Usabilidade
        ```
        
        **Seu Habitat:**
        - Volume Total: **{total_volume:.1f} m³**
        - Fator de Usabilidade: **{config['usable_factor']*100:.0f}%**
        - NHV Resultante: **{nhv:.1f} m³**
        - NHV por Pessoa: **{nhv_per_person:.1f} m³/pessoa**
        
        **Padrões NASA (baseados na duração da missão):**
        - ≤30 dias: 12.7 m³/pessoa
        - 31-90 dias: 16.7 m³/pessoa
        - 91-180 dias: 20.0 m³/pessoa
        - 181-360 dias: 22.5 m³/pessoa
        - &gt;360 dias: 27.9 m³/pessoa
        
        **Para sua missão de {config['mission_duration']} dias:**
        - NHV Requerido: **{nhv_required_per_person:.1f} m³/pessoa**
        - Seu NHV: **{nhv_per_person:.1f} m³/pessoa**
        - Status: {'ADEQUADO' if nhv_per_person >= nhv_required_per_person else f'ABAIXO DO PADRÃO (déficit de {nhv_required_per_person - nhv_per_person:.1f} m³/pessoa)'}
        
        **Por que isso importa:**  
        Estudos da NASA mostram que NHV insuficiente está correlacionado com aumento de estresse, 
        conflitos interpessoais, problemas de sono e queda no desempenho cognitivo. O NHV adequado 
        proporciona espaço para movimento, privacidade e atividades recreacionais essenciais para 
        missões de longa duração.
        """)
    
    # Área de piso
    with st.expander("Floor Area - Área de Piso"):
        st.markdown(f"""
        **Definição:**  
        A área de piso é o espaço horizontal disponível para circulação, trabalho e atividades diárias.
        
        **Fórmula:**
        - **Cilindro:** Área = π × (Diâmetro/2)²
        - **Retângulo:** Área = Comprimento × Largura
        
        **Seu Habitat:**
        - Área Total de Piso: **{floor_area:.1f} m²**
        - Área por Pessoa: **{floor_area_per_person:.1f} m²/pessoa**
        
        **Padrão NASA Mínimo:**
        - Requerido: **{MIN_FLOOR_AREA_PER_PERSON} m²/pessoa**
        - Status: {'ATENDE AO PADRÃO' if floor_area_per_person >= MIN_FLOOR_AREA_PER_PERSON else f'ABAIXO DO MÍNIMO (déficit de {MIN_FLOOR_AREA_PER_PERSON - floor_area_per_person:.1f} m²/pessoa)'}
        
        **Por que isso importa:**  
        A área de piso impacta diretamente a mobilidade, especialmente em ambientes de microgravidade 
        onde os astronautas usam as paredes e teto para se movimentar. Área insuficiente aumenta o 
        risco de colisões, dificulta o trabalho simultâneo de múltiplos tripulantes e reduz a 
        eficiência operacional.
        """)
    
    # Distribuição de zonas
    with st.expander("Zone Distribution - Distribuição de Zonas"):
        st.markdown(f"""
        **Definição:**  
        As zonas funcionais dividem o habitat em áreas especializadas para diferentes atividades 
        (dormir, trabalhar, higiene, alimentação, etc.).
        
        **Seu Habitat:**
        - Número de Zonas: **{len(zones)}**
        - Área Total Alocada: **{sum(zones.values()):.1f} m²**
        
        **Distribuição Detalhada:**
        """)
        
        from ..config.constants import ZONE_NAMES
        for zone_id, area in zones.items():
            percentage = (area / sum(zones.values())) * 100
            area_per_person = area / config["crew_size"]
            st.markdown(f"""
            - **{ZONE_NAMES[zone_id]}:** {area:.1f} m² ({percentage:.1f}%) = {area_per_person:.1f} m²/pessoa
            """)
        
        st.markdown("""
        **Recomendações NASA por Zona:**
        - **Dormir:** 2-4 m²/pessoa (privacidade essencial)
        - **Trabalho:** 3-5 m²/pessoa (espaço para equipamentos)
        - **Higiene:** 1.5-2 m²/pessoa (banheiro + higiene pessoal)
        - **Alimentação:** 1-2 m²/pessoa (preparação + consumo)
        - **Exercício:** 3-4 m²/pessoa (equipamentos + movimentação)
        - **Recreação:** 2-3 m²/pessoa (bem-estar psicológico)
        - **Armazenamento:** 1-2 m²/pessoa (suprimentos + equipamentos)
        
        **Por que isso importa:**  
        A distribuição adequada de zonas é crítica para separar atividades incompatíveis (ex: dormir 
        e exercícios), manter higiene (separação de áreas úmidas/secas) e otimizar o fluxo de trabalho 
        da tripulação.
        """)
    
    # Fator de usabilidade
    with st.expander("Usability Factor - Fator de Usabilidade"):
        st.markdown(f"""
        **Definição:**  
        O fator de usabilidade representa a porcentagem do volume total que é realmente utilizável 
        pelos tripulantes, descontando espaço ocupado por sistemas e equipamentos.
        
        **Seu Habitat:**
        - Fator de Usabilidade: **{config['usable_factor']*100:.0f}%**
        - Estrutura: **{config['structure_type']}**
        
        **Faixas Típicas por Tipo de Estrutura:**
        - **Estruturas Rígidas (Metálicas):** 70-80%
          - Mais equipamentos integrados (HVAC, energia, comunicação)
          - Painéis de controle e sistemas ocupam paredes
          - Estrutura mais robusta = mais espaço perdido
        
        - **Estruturas Infláveis (Soft Goods):** 85-90%
          - Menos equipamento estrutural fixo
          - Paredes flexíveis permitem melhor uso do espaço
          - Sistemas mais compactos ou externos
        
        **Exemplos Históricos:**
        - ISS: ~75% (estrutura rígida complexa)
        - Bigelow BEAM: ~88% (módulo inflável)
        - Skylab: ~72% (estrutura rígida)
        
        **Por que isso importa:**  
        Um fator de usabilidade superestimado resulta em NHV irreal, levando a designs que parecem 
        adequados no papel mas são claustrofóbicos na prática. Valores conservadores (70-75%) são 
        mais seguros para designs preliminares.
        """)
    
    # Gravidade e recursos
    with st.expander("Gravity & Resources - Gravidade e Recursos"):
        st.markdown(f"""
        **Seu Habitat:**
        - Ambiente de Gravidade: **{config['gravity_env']}**
        - Duração da Missão: **{config['mission_duration']} dias**
        - Tamanho da Tripulação: **{config['crew_size']} pessoas**
        
        **Impacto da Gravidade no Design:**
        
        **Microgravidade (0g):**
        - Astronautas usam todas as superfícies (paredes, teto, piso)
        - Volume 3D é mais importante que área de piso
        - Necessidade de pontos de ancoragem e restraints
        - Maior risco de colisões e desorientação espacial
        
        **Gravidade Lunar (1/6g = 0.165g):**
        - Movimento ainda é "flutuante" mas com direção preferencial
        - Piso é mais importante mas teto/paredes ainda usáveis
        - Equipamentos podem ter orientação gravitacional
        - Adaptação mais fácil que microgravidade
        
        **Gravidade Marciana (3/8g = 0.38g):**
        - Comportamento mais próximo à Terra
        - Piso é superfície primária de trabalho
        - Design mais tradicional com "up/down" claro
        - Menos restrições de orientação de equipamentos
        
        **Impacto da Duração:**
        - **Curta (&lt;30 dias):** Foco em funcionalidade, conforto secundário
        - **Média (30-180 dias):** Necessidade de espaços recreacionais e privacidade
        - **Longa (&gt;180 dias):** Bem-estar psicológico crítico, variedade de ambientes essencial
        
        **Por que isso importa:**  
        O ambiente gravitacional e a duração da missão influenciam dramaticamente os requisitos de 
        volume, layout e amenidades. Missões longas em microgravidade requerem os maiores volumes 
        por pessoa para manter a saúde mental da tripulação.
        """)
    
    st.markdown("---")
    
    # Resumo de validação
    st.markdown("### Resumo de Conformidade NASA")
    
    validations = []
    
    # Validar NHV
    if nhv_per_person >= nhv_required_per_person:
        validations.append(("NHV por Pessoa", True, f"{nhv_per_person:.1f} m³ (requerido: {nhv_required_per_person:.1f} m³)"))
    else:
        validations.append(("NHV por Pessoa", False, f"{nhv_per_person:.1f} m³ (requerido: {nhv_required_per_person:.1f} m³) - Déficit: {nhv_required_per_person - nhv_per_person:.1f} m³"))
    
    # Validar área de piso
    if floor_area_per_person >= MIN_FLOOR_AREA_PER_PERSON:
        validations.append(("Área de Piso", True, f"{floor_area_per_person:.1f} m²/pessoa (mínimo: {MIN_FLOOR_AREA_PER_PERSON} m²)"))
    else:
        validations.append(("Área de Piso", False, f"{floor_area_per_person:.1f} m²/pessoa (mínimo: {MIN_FLOOR_AREA_PER_PERSON} m²) - Déficit: {MIN_FLOOR_AREA_PER_PERSON - floor_area_per_person:.1f} m²"))
    
    # Validar zonas mínimas
    if len(zones) >= 3:
        validations.append(("Diversidade de Zonas", True, f"{len(zones)} zonas funcionais"))
    else:
        validations.append(("Diversidade de Zonas", False, f"{len(zones)} zonas (recomendado: mínimo 3 para funcionalidade básica)"))
    
    # Exibir validações
    for metric_name, is_valid, description in validations:
        if is_valid:
            st.success(f"**{metric_name}:** {description}")
        else:
            st.error(f"**{metric_name}:** {description}")
    
    # Conclusão
    all_valid = all(v[1] for v in validations)
    if all_valid:
        st.success("Parabéns! Seu habitat atende a todos os padrões NASA HIDH analisados.")
    else:
        st.warning("Atenção: Seu habitat não atende a todos os padrões NASA. Revise as métricas em vermelho e ajuste as configurações.")
