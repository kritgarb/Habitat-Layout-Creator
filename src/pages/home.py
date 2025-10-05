"""
Página inicial com explicação da ferramenta e glossário
"""
import streamlit as st


def render_home_page():
    """Renderiza a página inicial"""
    
    st.markdown("# Bem-vindo ao AEGIS Habitat Creator")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15)); 
                padding: 2rem; border-radius: 10px; border-left: 4px solid #A68CFF; margin: 1rem 0;'>
        <h2 style='color: #A68CFF; margin-top: 0;'>O que é esta ferramenta?</h2>
        <p style='font-size: 1.1rem; line-height: 1.8; color: #E2E8F0;'>
            O <strong>AEGIS Habitat Creator</strong> é uma ferramenta interativa desenvolvida para o 
            <strong>NASA Space Apps Challenge 2025</strong> que permite projetar e validar habitats espaciais 
            seguindo os padrões quantitativos da NASA.
        </p>
        <p style='font-size: 1.1rem; line-height: 1.8; color: #E2E8F0;'>
            Com esta ferramenta, você pode criar layouts personalizados para habitats em diferentes ambientes 
            (órbita, Lua, Marte), visualizar em 2D e 3D, e validar se seu design atende aos requisitos críticos 
            de volume habitável, área de piso, e distribuição de zonas funcionais.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Seção ODS
    st.markdown("---")
    st.markdown("## Objetivos de Desenvolvimento Sustentável (ODS) da ONU")
    
    st.markdown("""
    <p style='font-size: 1.1rem; line-height: 1.8; color: #E2E8F0; text-align: center; margin-bottom: 2rem;'>
        O projeto AEGIS Habitat Creator se alinha com os Objetivos de Desenvolvimento Sustentável da ONU, 
        contribuindo para um futuro mais sustentável tanto na Terra quanto no espaço.
    </p>
    """, unsafe_allow_html=True)
    
    # Cards dos ODS
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Carregar e exibir SVG do ODS 4
        svg_img = ""
        try:
            with open("src/selos/SDG-4- Educação de qualidade.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            # Modificar o SVG para limitar tamanho
            svg_img = svg_content.replace('<svg', '<svg width="80" height="80"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(196, 32, 50, 0.1); padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #C42032; height: 100%; min-height: 400px;'>
            <div style="text-align: center; margin-bottom: 1rem;">{svg_img}</div>
            <h4 style='color: #C42032; margin-top: 1rem;'>Educação de Qualidade</h4>
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                Nossa ferramenta serve como <strong>recurso educacional</strong> para estudantes e profissionais 
                aprenderem sobre design de habitats espaciais, engenharia aeroespacial e os desafios da 
                exploração espacial através de uma interface interativa e baseada em padrões científicos reais.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Carregar e exibir SVG do ODS 9
        svg_img = ""
        try:
            with open("src/selos/SDG-9-Indústria, inovação e infraestrutura.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            # Modificar o SVG para limitar tamanho
            svg_img = svg_content.replace('<svg', '<svg width="80" height="80"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(253, 105, 37, 0.1); padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #FD6925; height: 100%; min-height: 400px;'>
            <div style="text-align: center; margin-bottom: 1rem;">{svg_img}</div>
            <h4 style='color: #FD6925; margin-top: 1rem;'>Indústria, Inovação e Infraestrutura</h4>
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                Promovemos <strong>inovação em infraestrutura espacial</strong> através de ferramentas de 
                simulação e design que permitem o desenvolvimento de habitats seguros e eficientes. 
                A visualização 3D impulsiona o avanço tecnológico.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Carregar e exibir SVG do ODS 11
        svg_img = ""
        try:
            with open("src/selos/SDG-11 -  Cidades e comunidades sustentáveis.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            # Modificar o SVG para limitar tamanho
            svg_img = svg_content.replace('<svg', '<svg width="80" height="80"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(253, 157, 36, 0.1); padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #FD9D24; height: 100%; min-height: 400px;'>
            <div style="text-align: center; margin-bottom: 1rem;">{svg_img}</div>
            <h4 style='color: #FD9D24; margin-top: 1rem;'>Cidades e Comunidades Sustentáveis</h4>
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                Desenvolvemos conceitos de <strong>comunidades sustentáveis no espaço</strong> através do 
                planejamento otimizado de recursos, gestão eficiente de volume habitável e considerações 
                de sustentabilidade a longo prazo para missões espaciais prolongadas.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        # Carregar e exibir SVG do ODS 17
        svg_img = ""
        try:
            with open("src/selos/SDG-17 Parcerias e meios de implementação.svg", "r", encoding="utf-8") as f:
                svg_content = f.read()
            # Modificar o SVG para limitar tamanho
            svg_img = svg_content.replace('<svg', '<svg width="80" height="80"')
        except:
            pass
        
        st.markdown(f"""
        <div style='background: rgba(25, 72, 106, 0.1); padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #19486A; height: 100%; min-height: 400px;'>
            <div style="text-align: center; margin-bottom: 1rem;">{svg_img}</div>
            <h4 style='color: #19486A; margin-top: 1rem;'>Parcerias e Meios de Implementação</h4>
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                Criado para o <strong>NASA Space Apps Challenge</strong>, este projeto exemplifica a 
                colaboração global em desafios espaciais. A ferramenta open-source promove parcerias 
                entre educadores, engenheiros e entusiastas do espaço em todo o mundo.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Como usar
    st.markdown("## Como Usar")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 1 Configure
        Nas páginas de **Layout 2D** ou **3D**, configure:
        - Forma do habitat (Cilindro/Retangular)
        - Dimensões físicas
        - Tamanho da tripulação
        - Duração da missão
        - Zonas funcionais desejadas
        """)
    
    with col2:
        st.markdown("""
        ### 2 Visualize
        Veja seu habitat em:
        - **Planta Baixa 2D**: Layout das zonas com proporções reais
        - **Modelo 3D**: Visualização tridimensional interativa
        - Cores indicam diferentes zonas funcionais
        """)
    
    with col3:
        st.markdown("""
        ### 3 Valide
        Na página de **Métricas NASA**:
        - Verifique se atende padrões NASA
        - Analise NHV (Volume Habitável Líquido)
        - Confira requisitos de água e recursos
        - Exporte os dados em JSON
        """)
    
    st.markdown("---")
    
    # Glossário
    st.markdown("## Glossário de Termos")
    
    glossary = {
        "NHV (Net Habitable Volume)": {
            "desc": "Volume Habitável Líquido - o espaço interior utilizável do habitat, excluindo equipamentos, paredes e áreas inacessíveis.",
            "formula": "NHV = Volume Total × Fator de Usabilidade (tipicamente 0.7)",
            "ref": "Fórmula NASA: NHV (m³/pessoa) = 6.67 × ln(duração_dias) - 7.79"
        },
        "Habitat Cilíndrico": {
            "desc": "Formato circular otimizado para pressurização uniforme e eficiência estrutural em ambientes de baixa gravidade, como em órbitas.",
            "formula": "Volume = π × (diâmetro/2)² × altura",
            "ref": "Baseado no design da ISS e TransHab da NASA"
        },
        "Habitat Retangular": {
            "desc": "Formato modular que facilita conexão entre módulos e maximiza área de piso utilizável.",
            "formula": "Volume = comprimento × largura × altura",
            "ref": "Usado em habitats de superfície lunar/marciana"
        },
        "Zonas Funcionais": {
            "desc": "Áreas designadas para atividades específicas da tripulação.",
            "formula": "Área da Zona = m²/pessoa × número de tripulantes",
            "ref": "6 zonas principais: Dormir, Higiene, Cozinha, Exercício, Armazenamento, Trabalho/Lazer"
        },
        "Estrutura Rígida": {
            "desc": "Construção de alumínio ou compósitos com alta resistência e proteção contra micrometeoritos.",
            "formula": "Massa ≈ 150 kg/m³ de volume",
            "ref": "Exemplo: Módulos da Estação Espacial Internacional"
        },
        "Estrutura Inflável": {
            "desc": "Softgoods expansíveis que oferecem 3-4x mais volume com menor massa de lançamento.",
            "formula": "Massa ≈ 40 kg/m³ de volume",
            "ref": "Exemplo: BEAM (Bigelow Expandable Activity Module) na ISS"
        },
        "Microgravidade (0g)": {
            "desc": "Ambiente orbital onde a gravidade é negligível. Tripulação pode usar paredes e teto.",
            "formula": "Métrica principal: Volume (m³) | Faixa: 10⁻⁶g a 10⁻¹g",
            "ref": "ISS, habitats de trânsito Terra-Marte"
        },
        "Gravidade Lunar (1/6g)": {
            "desc": "16.7% da gravidade terrestre. Requer área de piso funcional.",
            "formula": "Métrica principal: Área horizontal (m²) | g ≈ 0.17g ou 1/6g",
            "ref": "Habitats de superfície lunar"
        },
        "Gravidade Marciana (3/8g)": {
            "desc": "37.5% da gravidade terrestre. Comportamento mais próximo da Terra.",
            "formula": "Métrica principal: Área horizontal (m²) | g ≈ 0.38g",
            "ref": "Habitats de superfície marciana"
        },
        "Recursos de Missão": {
            "desc": "Suprimentos críticos para sustentação da vida durante a missão.",
            "formula": "Água potável: 2.0 kg/pessoa/dia<br>Água alimentação: 0.5 kg/pessoa/dia<br>Oxigênio: 0.82 kg/pessoa/dia",
            "ref": "NASA-STD-3001 Human Integration Design Handbook"
        }
    }
    
    # Exibir glossário em cards
    for idx, (term, info) in enumerate(glossary.items()):
        if idx % 2 == 0:
            col1, col2 = st.columns(2)
        
        with col1 if idx % 2 == 0 else col2:
            with st.expander(f"**{term}**", expanded=False):
                st.markdown(f"**Descrição:**")
                st.write(info["desc"])
                st.markdown(f"**Cálculo/Fórmula:**")
                st.code(info["formula"], language=None)
                st.caption(f"Ref: {info['ref']}")
    
    st.markdown("---")
    
    # Guia rápido de navegação
    st.markdown("## Navegação")
    
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)
    
    with nav_col1:
        st.markdown("""
        ### Layout 2D
        - Planta baixa do habitat
        - Distribuição de zonas
        - Visão superior
        - Proporções em escala
        """)
    
    with nav_col2:
        st.markdown("""
        ### Layout 3D
        - Modelo tridimensional
        - Visualização interativa
        - Divisões de zonas
        - Câmera rotacional
        """)
    
    with nav_col3:
        st.markdown("""
        ### Métricas NASA
        - Validação de padrões
        - NHV calculado
        - Recursos necessários
        - Status de conformidade
        """)
    
    with nav_col4:
        st.markdown("""
        ### Documentação
        - Guia completo de uso
        - Padrões NASA detalhados
        - Referências técnicas
        - Exemplos práticos
        """)
    
    with nav_col5:
        st.markdown("""
        ### Sobre
        - Informações do projeto
        - Equipe AEGIS
        - NASA Space Apps 2025
        - Contato e créditos
        """)
    
    st.markdown("---")
    
    # Call to action
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2)); 
                border-radius: 10px; margin: 2rem 0;'>
        <h2 style='color: #A68CFF;'>Pronto para Começar?</h2>
        <p style='font-size: 1.2rem; color: #E2E8F0;'>
            Vá para <strong>Layout 2D</strong> ou <strong>Layout 3D</strong> para começar a projetar seu habitat espacial!
        </p>
    </div>
    """, unsafe_allow_html=True)
