"""
Página de documentação com guia completo de uso
"""
import streamlit as st


def render_documentation_page():
    """Renderiza a página de Documentação"""
    
    st.markdown("# Documentação - Guia Completo de Uso")
    
    # Introdução
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1)); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #3b82f6; margin-bottom: 2rem;'>
        <h3 style='color: #3b82f6; margin-top: 0;'>Bem-vindo à Documentação</h3>
        <p style='color: #E2E8F0; line-height: 1.8;'>
            Este guia abrangente irá ajudá-lo a dominar o <strong>AEGIS Habitat Layout Creator</strong>, 
            desde conceitos básicos até técnicas avançadas de design espacial.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Índice
    st.markdown("## Índice")
    st.markdown("""
    1. [Começando](#1-come-ando)
    2. [Conceitos Fundamentais](#2-conceitos-fundamentais)
    3. [Guia Passo a Passo](#3-guia-passo-a-passo)
    4. [Parâmetros de Configuração](#4-par-metros-de-configura-o)
    5. [Interpretando Visualizações](#5-interpretando-visualiza-es)
    6. [Entendendo Métricas NASA](#6-entendendo-m-tricas-nasa)
    7. [Requisitos de Recursos e Suporte de Vida](#6-5-requisitos-de-recursos-e-suporte-de-vida)
    8. [Dicas e Melhores Práticas](#7-dicas-e-melhores-pr-ticas)
    9. [Exportação de Dados](#8-exporta-o-de-dados)
    10. [Solução de Problemas](#9-solu-o-de-problemas)
    11. [Documentação NASA](#10-documenta-o-nasa)
    """)
    
    st.markdown("---")
    
    # Seção 1: Começando
    with st.expander("### 1. Começando", expanded=True):
        st.markdown("""
        #### O que é o AEGIS Habitat Layout Creator?
        
        O AEGIS é uma ferramenta de design interativa para criar e validar layouts de habitats espaciais 
        seguindo os padrões da **NASA Human Integration Design Handbook (HIDH)**. 
        
        #### Quem deve usar?
        - Engenheiros aeroespaciais
        - Designers de sistemas espaciais
        - Pesquisadores de arquitetura espacial
        - Estudantes de engenharia e ciências espaciais
        - Entusiastas de exploração espacial
        
        #### Requisitos
        - Navegador web moderno (Chrome, Firefox, Edge, Safari)
        - Conexão com internet (para gráficos interativos Plotly)
        - Conhecimento básico de conceitos espaciais (opcional mas recomendado)
        
        #### Primeiros Passos
        1. Navegue até a página **Início** para entender a ferramenta
        2. Leia o glossário de termos para familiarizar-se com a terminologia
        3. Escolha entre **Layout 2D** ou **Layout 3D** para começar seu design
        4. Configure os parâmetros básicos do habitat
        5. Visualize e valide seu design nas **Métricas NASA**
        """)
    
    # Seção 2: Conceitos Fundamentais
    with st.expander("### 2. Conceitos Fundamentais"):
        st.markdown("""
        #### Net Habitable Volume (NHV)
        - **O que é:** Volume interno utilizável pelos astronautas, excluindo equipamentos e estruturas
        - **Fórmula:** NHV = Volume Total × Fator de Usabilidade
        - **Importância:** Relacionado diretamente ao conforto psicológico e desempenho da tripulação
        - **Padrões NASA:** Varia de 12.7 m³/pessoa (30 dias) até 27.9 m³/pessoa (1+ ano)
        
        #### Formas de Habitat
        
        **Cilíndrico:**
        - Mais eficiente para pressurização (distribuição uniforme de estresse)
        - Melhor para lançamento (cabe em cargas úteis cilíndricas)
        - Volume = π × (Diâmetro/2)² × Altura
        - Exemplo: ISS modules, SpaceX Starship
        
        **Retangular (Box):**
        - Mais flexível para layouts internos
        - Melhor utilização de área de piso (cantos retos)
        - Volume = Comprimento × Largura × Altura
        - Exemplo: TransHab concept, B330 modules
        
        #### Tipos de Estrutura
        
        **Rígida (Rigid):**
        - Estrutura metálica permanente
        - Maior proteção contra radiação e micrometeoritos
        - Mais equipamentos integrados = menor fator de usabilidade (70-80%)
        - Exemplo: ISS, Skylab
        
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
        - Movimento ainda "flutuante" mas com orientação
        - Equilíbrio entre volume e área de piso
        
        **Gravidade Marciana (0.38g):**
        - Superfície de Marte
        - Mais próximo de design terrestre
        - Área de piso é primária
        
        #### Zonas Funcionais
        
        Divisões do habitat por função:
        - **Dormir (Sleep):** Privacidade, descanso
        - **Trabalho (Work):** Laboratórios, controles
        - **Higiene (Hygiene):** Banheiro, chuveiro
        - **Alimentação (Food):** Cozinha, refeições
        - **Exercício (Exercise):** Equipamentos fitness
        - **Recreação (Recreation):** Lazer, relaxamento
        - **Armazenamento (Storage):** Suprimentos, equipamentos
        - **Médica (Medical):** Primeiros socorros, exames
        """)
    
    # Seção 3: Guia Passo a Passo
    with st.expander("### 3. Guia Passo a Passo"):
        st.markdown("""
        #### Passo 1: Defina os Parâmetros da Missão
        
        1. **Escolha a forma do habitat:**
           - Cilíndrico para eficiência estrutural
           - Retangular para flexibilidade de layout
        
        2. **Selecione o tipo de estrutura:**
           - Rígida para missões críticas com muitos sistemas
           - Inflável para maximizar volume com massa mínima
        
        3. **Configure dimensões:**
           - **Cilindro:** Diâmetro (3-8m típico) e Altura (4-10m típico)
           - **Retângulo:** Comprimento, Largura, Altura (4-10m cada)
           - Dica: Comece com dimensões padrão e ajuste conforme necessário
        
        4. **Defina tripulação e missão:**
           - Tamanho da tripulação: 4-6 pessoas típico
           - Duração: 30 dias (curta) até 360+ dias (longa)
           - Dica: Duração afeta drasticamente requisitos de NHV
        
        5. **Escolha o ambiente gravitacional:**
           - Microgravidade: ISS, órbita
           - Lunar: Base lunar
           - Marciana: Base marciana
        
        #### Passo 2: Configure as Zonas Funcionais
        
        1. **Selecione zonas necessárias:**
           - Mínimo recomendado: Dormir, Trabalho, Higiene
           - Ideal: 5-7 zonas para funcionalidade completa
        
        2. **Ajuste áreas personalizadas (opcional):**
           - Deixe em branco para distribuição automática balanceada
           - Ou insira m² específicos para controle preciso
           - Dica: Dormir e Trabalho geralmente são as maiores zonas
        
        3. **Valide a soma:**
           - A ferramenta avisa se áreas personalizadas excedem área disponível
           - Ajuste valores ou remova zonas se necessário
        
        #### Passo 3: Visualize o Design
        
        1. **Layout 2D (Planta Baixa):**
           - Veja distribuição de zonas vista de cima
           - Cilindros: setores circulares
           - Retângulos: grid otimizado
           - Interação: Hover para detalhes de cada zona
        
        2. **Layout 3D (Modelo Tridimensional):**
           - Visualize volume completo do habitat
           - Interação: Clique e arraste para rotacionar
           - Use roda do mouse para zoom
           - Duplo clique para resetar visualização
        
        #### Passo 4: Analise as Métricas
        
        1. **Acesse Métricas NASA:**
           - Dashboard completo com todas as métricas quantitativas
        
        2. **Verifique conformidade:**
           - NHV por pessoa vs. padrão NASA
           - Área de piso por pessoa vs. mínimo 10 m²
           - Distribuição de zonas adequada
        
        3. **Identifique problemas:**
           - Métricas em vermelho indicam não-conformidade
           - Leia explicações detalhadas de cada métrica
           - Ajuste configurações conforme necessário
        
        #### Passo 5: Itere e Refine
        
        1. **Experimente variações:**
           - Teste diferentes formas e dimensões
           - Compare estruturas rígidas vs. infláveis
           - Varie número e tamanho de zonas
        
        2. **Optimize para seus objetivos:**
           - Maximize NHV para missões longas
           - Minimize área para eficiência de massa
           - Balance funcionalidade vs. recursos
        
        3. **Documente seu design:**
           - Use exportação JSON para salvar configurações
           - Capture screenshots das visualizações
           - Anote decisões de design e trade-offs
        """)
    
    # Seção 4: Parâmetros de Configuração
    with st.expander("### 4. Parâmetros de Configuração"):
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
        
        #### Seleção de Zonas
        - **Mínimo:** 1 zona
        - **Recomendado:** 3-7 zonas
        - **Áreas Personalizadas:** Opcional, em m²
        - **Auto-distribuição:** Ferramenta calcula automaticamente se não especificado
        """)
    
    # Seção 5: Interpretando Visualizações
    with st.expander("### 5. Interpretando Visualizações"):
        st.markdown("""
        #### Visualização 2D (Planta Baixa)
        
        **Habitats Cilíndricos:**
        - Zonas aparecem como setores circulares (fatias)
        - Círculo central = corredor comum
        - Tamanho da fatia = área da zona
        - Cores únicas identificam cada zona
        
        **Habitats Retangulares:**
        - Zonas organizadas em grid otimizado
        - Linhas de grade para referência espacial
        - Cada retângulo = uma zona
        - Proporções aproximadas às áreas reais
        
        **Interatividade:**
        - Hover: Ver nome, área, porcentagem
        - Legendas: Cores e zonas identificadas
        - Responsive: Adapta-se ao tamanho da tela
        
        **O que procurar:**
        - Distribuição balanceada de zonas
        - Zonas grandes o suficiente para função
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
    
    # Seção 6: Entendendo Métricas NASA
    with st.expander("### 6. Entendendo Métricas NASA"):
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
        - Indicador chave de adequação do design
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
        - Diversidade indica funcionalidade
        - Áreas por zona devem ser apropriadas
        - **Recomendações por zona:**
          - Dormir: 2-4 m²/pessoa
          - Trabalho: 3-5 m²/pessoa
          - Higiene: 1.5-2 m²/pessoa
          - Alimentação: 1-2 m²/pessoa
          - Exercício: 3-4 m²/pessoa
          - Recreação: 2-3 m²/pessoa
          - Armazenamento: 1-2 m²/pessoa
          - Médica: 2-3 m²/pessoa
        
        #### Conformidade Geral
        - Resumo de todas as validações
        - Verde: Atende aos padrões
        - Vermelho: Requer atenção
        - Déficits quantificados para correção
        """)
    
    # Seção 6.5: Requisitos de Recursos e Suporte de Vida
    with st.expander("### 6.5. Requisitos de Recursos e Suporte de Vida"):
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
    
    # Seção 7: Dicas e Melhores Práticas
    with st.expander("### 7. Dicas e Melhores Práticas"):
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
        - Conexão com outros módulos
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
        - Cilindro: ⌀8m × H10+m ou múltiplos módulos
        - Retângulo: 10×8×8m ou múltiplos módulos
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
        8. Médica (2%)
        
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
    
    # Seção 8: Exportação de Dados
    with st.expander("### 8. Exportação de Dados"):
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
        
        #### Como Exportar
        
        1. Configure completamente seu habitat
        2. Valide todas as métricas
        3. Navegue até a seção de exportação (geralmente no final de cada página)
        4. Clique no botão "Exportar Configuração (JSON)"
        5. Arquivo será baixado automaticamente
        
        #### Usando os Dados Exportados
        
        **Documentação:**
        - Anexe a relatórios de design
        - Inclua em propostas de missão
        - Use como baseline para iterações
        
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
    with st.expander("### 9. Solução de Problemas"):
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
    with st.expander("### 10. Documentação NASA"):
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
