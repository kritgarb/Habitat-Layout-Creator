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
        
        **Inflável (Inflatable):**
        - Estrutura de tecidos avançados (Kevlar, Vectran)
        - Compacta durante lançamento, expande no espaço
        - Maior fator de usabilidade (85-90%)
        - Exemplo: Bigelow BEAM, Sierra Space LIFE
        
        #### Ambientes Gravitacionais
        
        **Microgravidade (0g):**
        - ISS, órbita terrestre
        - Todas as superfícies são utilizáveis
        - Volume 3D é mais crítico que área de piso
        
        **Gravidade Lunar (0.165g):**
        - Superfície da Lua
        - Movement still "floating" but with orientation
        - Equilíbrio entre volume e área de piso
        
        **Gravidade Marciana (0.38g):**
        - Superfície de Marte
        - Mais próximo de design terrestre
        - Área de piso é primária
        
        #### Functional Zones
        
        Habitat divisions by function:
        - **Dormir (Sleep):** Privacidade, descanso
        - **Trabalho (Work):** Laboratórios, controles
        - **Higiene (Hygiene):** Banheiro, chuveiro
        - **Food:** Kitchen, meals
        - **Exercise:** Fitness equipment
        - **Recreation:** Leisure, relaxation
        - **Armazenamento (Storage):** Suprimentos, equipamentos
        - **Medical:** First aid, examinations
        """)
    
    # Section 3: Step-by-Step Guide
    with st.expander("### 3. Step-by-Step Guide"):
        st.markdown("""
        # Step 1
        st.subheader("Step 1: Define Mission Parameters")
        
        1. **Escolha a forma do habitat:**
           - Cilíndrico para eficiência estrutural
           - Retangular para flexibilidade de layout
        
        2. **Selecione o tipo de estrutura:**
           - Rígida para missões críticas com muitos sistemas
           - Inflável para maximizar volume com massa mínima
        
        3. **Configure dimensões:**
           - **Cilindro:** Diâmetro (3-8m típico) e Altura (4-10m típico)
           - **Retângulo:** Comprimento, Largura, Altura (4-10m cada)
           - Tip: Start with standard dimensions and adjust as needed
        
        4. **Defina tripulação e missão:**
           - Tamanho da tripulação: 4-6 pessoas típico
           - Duração: 30 dias (curta) até 360+ dias (longa)
           - Tip: Duration drastically affects NHV requirements
        
        5. **Escolha o ambiente gravitacional:**
           - Microgravidade: ISS, órbita
           - Lunar: Base lunar
           - Marciana: Base marciana
        
        # Step 2
        st.subheader("Step 2: Select Functional Zones")
        
        1. **Select necessary zones:**
           - Mínimo recomendado: Dormir, Trabalho, Higiene
           - Ideal: 5-7 zones for complete functionality
        
        2. **Ajuste áreas personalizadas (opcional):**
           - Deixe em branco para distribuição automática balanceada
           - Ou insira m² específicos para controle preciso
           - Tip: Sleep and Work are usually the largest zones
        
        3. **Valide a soma:**
           - A ferramenta avisa se áreas personalizadas excedem área disponível
           - Adjust values or remove zones if necessary
        
        #### Step 3: Visualize the Design
        
        1. **Layout 2D (Planta Baixa):**
           - See zone distribution from top view
           - Cilindros: setores circulares
           - Retângulos: grid otimizado
           - Interação: Hover para detalhes de cada zona
        
        2. **Layout 3D (Modelo Tridimensional):**
           - Visualize volume completo do habitat
           - Interação: Clique e arraste para rotacionar
           - Use roda do mouse para zoom
           - Duplo clique para resetar visualização
        
        #### Step 4: Analyze the Metrics
        
        1. **Acesse Métricas NASA:**
           - Dashboard completo com todas as métricas quantitativas
        
        2. **Verifique conformidade:**
           - NHV por pessoa vs. padrão NASA
           - Área de piso por pessoa vs. mínimo 10 m²
           - Adequate zone distribution
        
        3. **Identifique problemas:**
           - Red metrics indicate non-compliance
           - Leia explicações detalhadas de cada métrica
           - Ajuste configurações conforme necessário
        
        #### Step 5: Iterate and Refine
        
        1. **Experimente variações:**
           - Teste diferentes formas e dimensões
           - Compare estruturas rígidas vs. infláveis
           - Vary number and size of zones
        
        2. **Optimize para seus objetivos:**
           - Maximize NHV para missões longas
           - Minimize área para eficiência de massa
           - Balance funcionalidade vs. recursos
        
        3. **Documente seu design:**
           - Use exportação JSON para salvar configurações
           - Capture screenshots das visualizações
           - Anote decisões de design e trade-offs
        """)
    
    # Section 4: Configuration Parameters
    with st.expander("### 4. Configuration Parameters"):
        st.markdown("""
        #### Forma do Habitat (Shape)
        - **Opções:** Cylinder, Rectangular
        - **Impacto:** Determina fórmulas de volume e área
        - **Recomendação:** Cilindro para pressurização eficiente
        
        #### Tipo de Estrutura (Structure)
        - **Opções:** Rigid, Inflatable
        - **Impacto:** Afeta fator de usabilidade (70-90%)
        - **Recomendação:** Rígida para durabilidade, Inflável para volume
        
        #### Dimensões
        
        **Cilindro:**
        - **Diâmetro:** 3-8 metros típico
          - Menor: lançamento mais fácil
          - Maior: mais espaço interno
        - **Altura:** 4-10 metros típico
          - Afeta volume proporcionalmente
          - Considere altura de teto (2-2.5m mínimo)
        
        **Retângulo:**
        - **Comprimento/Largura/Altura:** 4-10 metros típico
        - Considere relação de aspecto (L:W:H)
        - Evite dimensões muito desproporcionais
        
        #### Tamanho da Tripulação (Crew Size)
        - **Faixa:** 4-6 pessoas
        - **Típico:** 4-6 pessoas
        - **Impacto:** Divisor para métricas per capita
        - **Consideração:** Mais pessoas = mais recursos, mais complexidade social
        
        #### Duração da Missão (Mission Duration)
        - **Faixa:** 1-1000+ dias
        - **Categorias:**
          - Curta: ≤30 dias
          - Média: 31-180 dias
          - Longa: 181-360 dias
          - Muito longa: 360+ dias
        - **Impacto:** Determina NHV requerido por pessoa
        - **Consideração:** Missões longas requerem mais espaço para saúde mental
        
        #### Ambiente Gravitacional (Gravity)
        - **Opções:** 
          - Microgravity (0g)
          - Lunar Gravity (0.165g)
          - Martian Gravity (0.38g)
        - **Impacto:** Influencia uso do espaço e orientação de equipamentos
        - **Consideração:** Microgravidade usa volume 3D; gravidade usa área de piso
        
        #### Fator de Usabilidade (Usability Factor)
        - **Faixa:** 0.60-0.95 (60%-95%)
        - **Rígida:** 0.70-0.80 típico
        - **Inflável:** 0.85-0.90 típico
        - **Impacto:** Multiplicador direto do NHV
        - **Recomendação:** Use valores conservadores (0.70-0.75) para designs preliminares
        
        #### Zone Selection
        - **Mínimo:** 1 zona
        - **Recommended:** 3-7 zones
        - **Áreas Personalizadas:** Opcional, em m²
        - **Auto-distribuição:** Ferramenta calcula automaticamente se não especificado
        """)
    
    # Section 5: Interpreting Visualizations
    with st.expander("### 5. Interpreting Visualizations"):
        st.markdown("""
        #### Visualização 2D (Planta Baixa)
        
        **Habitats Cilíndricos:**
        - Zones appear as circular sectors (slices)
        - Círculo central = corredor comum
        - Tamanho da fatia = área da zona
        - Cores únicas identificam cada zona
        
        **Habitats Retangulares:**
        - Zones organized in optimized grid
        - Linhas de grade para referência espacial
        - Cada retângulo = uma zona
        - Proporções aproximadas às áreas reais
        
        **Interatividade:**
        - Hover: Ver nome, área, porcentagem
        - Legends: Colors and zones identified
        - Responsive: Adapta-se ao tamanho da tela
        
        **O que procurar:**
        - Balanced zone distribution
        - Zones large enough for function
        - Separação lógica (ex: dormir longe de exercício)
        
        #### Visualização 3D (Modelo Tridimensional)
        
        **Elementos do Modelo:**
        - Contorno externo = forma do habitat
        - Planos coloridos = divisões de zonas
        - Cores = correspondência com legenda
        - Eixos = referência espacial (X, Y, Z)
        
        **Controles Interativos:**
        - **Rotação:** Clique e arraste
        - **Zoom:** Roda do mouse ou pinch em touch
        - **Pan:** Clique direito e arraste (ou Shift + clique)
        - **Reset:** Duplo clique na visualização
        - **Legenda:** Clique em itens para mostrar/ocultar zonas
        
        **Ângulos de Visualização:**
        - Vista frontal: Veja altura e largura
        - Vista lateral: Veja profundidade
        - Vista superior: Veja planta baixa em 3D
        - Isométrica: Veja proporções gerais
        
        **O que procurar:**
        - Proporções realistas do habitat
        - Volume aparente de cada zona
        - Relações espaciais entre zonas
        - Adequação para número de tripulantes
        """)
    
    # Section 6: Understanding NASA Metrics
    with st.expander("### 6. Understanding NASA Metrics"):
        st.markdown("""
        #### Volume Total
        - Volume geométrico completo do habitat
        - Inclui espaço de equipamentos e estruturas
        - Base para cálculo de NHV
        - **Fórmulas:**
          - Cilindro: π × r² × h
          - Retângulo: L × W × H
        
        #### Net Habitable Volume (NHV)
        - Volume utilizável pela tripulação
        - NHV = Volume Total × Fator de Usabilidade
        - Métrica mais importante para conforto
        - **Padrões NASA por duração:**
          - ≤30 dias: 12.7 m³/pessoa
          - 31-90 dias: 16.7 m³/pessoa
          - 91-180 dias: 20.0 m³/pessoa
          - 181-360 dias: 22.5 m³/pessoa
          - &gt;360 dias: 27.9 m³/pessoa
        
        #### NHV por Pessoa
        - NHV total dividido pelo tamanho da tripulação
        - Compara diretamente com padrões NASA
        - Key indicator of design adequacy
        - **Interpretação:**
          - Acima do padrão: Excelente
          - No padrão: Adequado
          - Abaixo do padrão: Requer revisão
        
        #### Área de Piso
        - Área horizontal para circulação e trabalho
        - Crítica para gravidade parcial ou total
        - **Padrão NASA:** Mínimo 10 m²/pessoa
        - **Fórmulas:**
          - Cilindro: π × r²
          - Retângulo: L × W
        
        #### Área de Piso por Pessoa
        - Área total dividida pelo tamanho da tripulação
        - Importante para densidade e mobilidade
        - **Interpretação:**
          - &gt;15 m²/pessoa: Espaçoso
          - 10-15 m²/pessoa: Adequado
          - &lt;10 m²/pessoa: Congestionado
        
        #### Distribuição de Zonas
        - Número e tamanho de zonas funcionais
        - Diversity indicates functionality
        - Áreas por zona devem ser apropriadas
        - **Recomendações por zona:**
          - Dormir: 2-4 m²/pessoa
          - Trabalho: 3-5 m²/pessoa
          - Higiene: 1.5-2 m²/pessoa
          - Alimentação: 1-2 m²/pessoa
          - Exercício: 3-4 m²/pessoa
          - Recreação: 2-3 m²/pessoa
          - Armazenamento: 1-2 m²/pessoa
          - Medical: 2-3 m²/person
        
        #### Conformidade Geral
        - Resumo de todas as validações
        - Verde: Atende aos padrões
        - Vermelho: Requer atenção
        - Déficits quantificados para correção
        """)
    
    # Section 6.5: Resource Requirements and Life Support
    with st.expander("### 6.5. Resource Requirements and Life Support"):
        st.markdown(r"""
        #### Requisitos de Água
        
        **Água Potável (Hidratação/Consumo):**
        - Mínimo de $\mathbf{2.0 \text{ kg}}$ de água potável por tripulante por dia de missão para ingestão
        - Essencial para hidratação e funções corporais
        - Deve ser potável e livre de contaminantes
        
        **Água para Reidratação de Alimentos:**
        - Aproximadamente $\mathbf{0.5 \text{ kg}}$ por tripulante por dia de missão
        - Necessária para preparação de alimentos liofilizados
        - Temperatura e qualidade controladas
        
        **Água para Atividades Extraveiculares (EVA):**
        - Adicionalmente, $\mathbf{0.24 \text{ kg}}$ de água por hora de EVA
        - Acima da provisão nominal de água
        - Recomendado para evitar a desidratação durante atividades intensas
        
        **Total de Água por Pessoa/Dia:**
        - **Nominal:** 2.5 kg/dia (2.0 + 0.5)
        - **Com EVAs:** Adicionar 0.24 kg por hora de EVA
        
        #### Requisitos de Oxigênio
        
        **Produção de Oxigênio via Plantas:**
        - Cerca de $\mathbf{20-25 \text{ m}^2}$ de colheitas são necessárias para fornecer o $\text{O}_2$ para um humano
        - Sistemas bioregenerativos podem reduzir dependência de ressuprimento
        - Plantas também fornecem benefícios psicológicos
        
        **Consumo Humano:**
        - Aproximadamente 0.82 kg de $\text{O}_2$ por pessoa por dia
        - Produção de 1.0 kg de $\text{CO}_2$ por pessoa por dia
        
        #### Requisitos de Alimentos
        
        **Produção de Alimentos (Calorias):**
        - Cerca de $\mathbf{50 \text{ m}^2}$ são necessários para fornecer as calorias dietéticas para um humano
        - Baseado em 2500 kcal/pessoa/dia
        - Sistemas de cultivo vertical podem otimizar espaço
        
        **Massa de Alimentos:**
        - Aproximadamente 1.8 kg de alimentos por pessoa por dia
        - Alimentos liofilizados reduzem massa e volume
        
        #### Saúde da Tripulação
        
        **Perda de Massa Corporal:**
        - Em missões de longa duração na ISS, observou-se uma perda média de $\mathbf{2.4\%}$ do peso corporal a cada 100 dias
        - Relacionado a: perda de apetite, exercício insuficiente, estresse
        - Contramedidas: exercício diário (2h), nutrição adequada, monitoramento médico
        
        **Implicações de Design:**
        - Zona de exercício é **crítica** para missões longas
        - Área mínima recomendada: 3-4 m²/pessoa
        - Equipamentos: esteira, bicicleta ergométrica, resistência
        
        #### Resumo de Recursos por Pessoa/Dia
        
        | Recurso | Quantidade | Unidade |
        |---------|------------|---------|
        | Água (potável) | 2.0 | kg |
        | Água (alimentos) | 0.5 | kg |
        | Água (EVA) | 0.24 | kg/hora EVA |
        | Oxigênio | 0.82 | kg |
        | Alimentos | 1.8 | kg |
        | CO₂ produzido | 1.0 | kg |
        | Área cultivo O₂ | 20-25 | m² |
        | Área cultivo alimentos | 50 | m² |
        
        **Nota:** Estes valores são para missões sem sistemas de reciclagem avançados. 
        Sistemas ECLSS (Environmental Control and Life Support System) podem reduzir 
        significativamente a necessidade de ressuprimento através de reciclagem de água e ar.
        """)
    
    # Section 7: Tips and Best Practices
    with st.expander("### 7. Tips and Best Practices"):
        st.markdown("""
        #### Design Geral
        
        **Faça:**
        - Comece com padrões NASA e ajuste conforme necessário
        - Itere múltiplas vezes antes de finalizar
        - Considere trade-offs (volume vs. massa vs. custo)
        - Documente decisões de design
        - Use valores conservadores para fator de usabilidade
        
        **Evite:**
        - Minimizar demais o espaço (conforto importa!)
        - Ignorar padrões NASA sem justificativa
        - Designs com apenas 1-2 zonas (insuficiente)
        - Dimensões extremas sem validação estrutural
        - Superestimar fator de usabilidade (&gt;90%)
        
        #### Seleção de Forma
        
        **Use Cilindro quando:**
        - Pressurização é crítica
        - Lançamento em cargas úteis cilíndricas
        - Eficiência estrutural é prioridade
        - Massa deve ser minimizada
        
        **Use Retângulo quando:**
        - Flexibilidade de layout é importante
        - Connection with other modules
        - Utilização de cantos é vantajosa
        - Design modular é necessário
        
        #### Dimensionamento
        
        **Para Tripulações Pequenas (2-3 pessoas):**
        - Cilindro: ⌀4-5m × H5-7m
        - Retângulo: 5×4×5m típico
        - Foco em multifuncionalidade de zonas
        
        **Para Tripulações Médias (4-6 pessoas):**
        - Cilindro: ⌀6-7m × H8-10m
        - Retângulo: 8×6×6m típico
        - Zonas especializadas importantes
        
        **Para Tripulações Grandes (7+ pessoas):**
        - Cylinder: ⌀8m × H10+m or multiple modules
        - Rectangle: 10×8×8m or multiple modules
        - Considere habitats modulares conectados
        
        #### Alocação de Zonas
        
        **Prioridades por Duração:**
        
        **Missões Curtas (≤30 dias):**
        1. Trabalho (40%)
        2. Dormir (25%)
        3. Higiene (15%)
        4. Alimentação (10%)
        5. Armazenamento (10%)
        
        **Missões Médias (31-180 dias):**
        1. Trabalho (30%)
        2. Dormir (25%)
        3. Exercício (15%)
        4. Alimentação (10%)
        5. Higiene (10%)
        6. Recreação (5%)
        7. Armazenamento (5%)
        
        **Missões Longas (&gt;180 dias):**
        1. Trabalho (25%)
        2. Dormir (25%)
        3. Exercício (15%)
        4. Recreação (10%)
        5. Alimentação (10%)
        6. Higiene (10%)
        7. Armazenamento (3%)
        8. Medical (2%)
        
        #### Otimização Iterativa
        
        **Processo recomendado:**
        1. Comece com dimensões padrão
        2. Verifique conformidade NASA
        3. Identifique maior déficit
        4. Ajuste parâmetro relevante
        5. Revalide métricas
        6. Repita até conformidade
        7. Refine para otimização
        
        **Parâmetros de ajuste rápido:**
        - Aumentar NHV: ↑ dimensões ou ↑ fator usabilidade
        - Aumentar área de piso: ↑ diâmetro/comprimento/largura
        - Melhorar distribuição: Ajustar áreas de zonas
        - Reduzir massa: ↓ dimensões ou use inflável
        """)
    
    # Section 8: Data Export
    with st.expander("### 8. Data Export"):
        st.markdown("""
        #### Formatos de Exportação
        
        **JSON (JavaScript Object Notation):**
        - Formato estruturado legível por máquina
        - Contém todas as configurações e métricas
        - Ideal para arquivamento e compartilhamento
        - Pode ser reimportado (futuro)
        
        **Conteúdo do Arquivo JSON:**
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
        
        1. Configure completamente seu habitat
        2. Valide todas as métricas
        3. Navigate to the export section (usually at the end of each page)
        4. Clique no botão "Exportar Configuração (JSON)"
        5. Arquivo será baixado automaticamente
        
        #### Usando os Dados Exportados
        
        **Documentação:**
        - Anexe a relatórios de design
        - Inclua em propostas de missão
        - Use as baseline for iterations
        
        **Análise:**
        - Importe em ferramentas de análise (Excel, Python, MATLAB)
        - Compare múltiplos designs
        - Gere gráficos de trade-off
        
        **Compartilhamento:**
        - Envie para colegas de equipe
        - Submeta para revisões
        - Archive em repositórios de projeto
        
        **Rastreabilidade:**
        - Timestamp automático
        - Todas as decisões de design capturadas
        - Reprodutível para auditoria
        
        #### Screenshots
        
        **Visualizações 2D/3D:**
        - Use ferramenta de captura de tela do navegador
        - Ou ferramenta de screenshot do sistema operacional
        - Alta resolução recomendada para apresentações
        
        **Métricas:**
        - Capture dashboard completo
        - Inclua validações de conformidade
        - Use em relatórios e apresentações
        """)
    
    # Seção 9: Solução de Problemas
    with st.expander("### 9. Problem Solution"):
        st.markdown("""
        #### Problemas Comuns e Soluções
        
        #### "NHV por pessoa está abaixo do padrão NASA"
        
        **Causas possíveis:**
        - Dimensões do habitat muito pequenas
        - Fator de usabilidade muito baixo
        - Tripulação muito grande para o volume
        - Duração da missão muito longa para o NHV atual
        
        **Soluções:**
        1. Aumentar dimensões (diâmetro, altura, comprimento, largura)
        2. Aumentar fator de usabilidade (se justificável)
        3. Reduzir tamanho da tripulação (se possível)
        4. Considerar estrutura inflável (maior fator de usabilidade)
        5. Usar múltiplos módulos conectados
        
        #### "Área de piso por pessoa abaixo do mínimo"
        
        **Causas possíveis:**
        - Diâmetro/comprimento/largura insuficientes
        - Tripulação muito grande
        - Forma cilíndrica com diâmetro pequeno
        
        **Soluções:**
        1. Aumentar diâmetro (cilindro) ou comprimento/largura (retângulo)
        2. Considerar forma retangular (mais área de piso por volume)
        3. Reduzir tamanho da tripulação
        4. Verificar se altura excessiva está "desperdiçando" volume
        
        #### "Soma das áreas de zonas excede área disponível"
        
        **Causas possíveis:**
        - Áreas personalizadas somam mais que área total de piso
        - Erros de entrada de dados
        
        **Soluções:**
        1. Deixe áreas em branco para distribuição automática
        2. Reduza valores de áreas personalizadas
        3. Remova algumas zonas
        4. Aumente dimensões do habitat para mais área de piso
        
        #### "Visualização 2D ou 3D não aparece"
        
        **Causas possíveis:**
        - Nenhuma zona selecionada
        - Erro de conexão (Plotly requer internet)
        - Browser não suporta WebGL (para 3D)
        
        **Soluções:**
        1. Selecione pelo menos uma zona funcional
        2. Verifique conexão com internet
        3. Use navegador moderno (Chrome, Firefox, Edge atualizados)
        4. Habilite WebGL nas configurações do navegador
        5. Desabilite extensões que bloqueiam scripts
        
        #### "Métricas parecem incorretas"
        
        **Causas possíveis:**
        - Configuração inconsistente
        - Cache do navegador desatualizado
        - Valores de entrada inválidos
        
        **Soluções:**
        1. Recarregue a página (F5 ou Ctrl+R)
        2. Limpe cache do navegador
        3. Verifique todos os valores de entrada
        4. Revise fórmulas na página de métricas
        5. Exporte JSON e verifique valores brutos
        
        #### "Interface está lenta ou travando"
        
        **Causas possíveis:**
        - Muitas zonas selecionadas (8+)
        - Conexão lenta com internet
        - Navegador com muitas abas abertas
        - Hardware limitado
        
        **Soluções:**
        1. Reduza número de zonas para 5-7
        2. Feche abas desnecessárias do navegador
        3. Desabilite extensões do navegador temporariamente
        4. Use modo de navegação anônima
        5. Tente navegador diferente
        
        #### "Não consigo exportar JSON"
        
        **Causas possíveis:**
        - Bloqueador de downloads
        - Permissões do navegador
        - Pasta de downloads cheia
        
        **Soluções:**
        1. Permita downloads do site nas configurações do navegador
        2. Verifique espaço em disco
        3. Tente navegador diferente
        4. Verifique pasta de downloads padrão
        
        #### Ainda com Problemas?
        
        Se você continua enfrentando dificuldades:
        1. Verifique a página **ℹ️ Sobre** para informações de contato
        2. Documente o problema (screenshots, mensagens de erro)
        3. Anote configurações que causam o problema
        4. Reporte através dos canais de suporte
        """)
    
    st.markdown("---")
    
    # Documentação NASA
    with st.expander("### 10. NASA Documentation"):
        st.markdown("""
        #### Padrões e Referências Oficiais
        
        **NASA HIDH Standards**
        
        O Human Integration Design Handbook é a principal referência para design de habitats espaciais:
        - [NASA HIDH Standards](https://www.nasa.gov/wp-content/uploads/2023/03/human-integration-design-handbook-revision-1.pdf?emrc=68e269191aa6f)
        - Cobre requisitos de volume, ergonomia, fatores humanos e habitabilidade
        - Base para todos os cálculos de NHV e área mínima desta ferramenta
        
        **ISS Research Publications**
        
        Pesquisas e dados operacionais da Estação Espacial Internacional:
        - [ISS Research Publications](https://issnationallab.org/publications/)
        - Lições aprendidas de mais de 20 anos de operação contínua
        - Dados reais de habitabilidade em microgravidade
        
        **Human Spaceflight Standards**
        
        Padrões técnicos da NASA para voos espaciais tripulados:
        - [Human Spaceflight Standards](https://www.nasa.gov/ochmo/human-spaceflight-and-aviation-standards/)
        - Requisitos de segurança, saúde e desempenho da tripulação
        - Normas para design de sistemas espaciais
        
        #### Como Usar Esta Documentação
        
        1. **Para Validação:** Compare resultados desta ferramenta com valores oficiais
        2. **Para Aprofundamento:** Leia documentos completos para contexto adicional
        3. **Para Pesquisa:** Use como ponto de partida para estudos mais avançados
        4. **Para Conformidade:** Verifique se seu design atende aos padrões NASA
        
        #### Publicações Científicas Relacionadas
        
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
            💡 <strong>Dica Final:</strong> A prática leva à perfeição! Experimente diferentes configurações 
            e aprenda como cada parâmetro afeta o design geral.
        </p>
    </div>
    """, unsafe_allow_html=True)
