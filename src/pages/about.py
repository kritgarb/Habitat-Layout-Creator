"""
Página Sobre com informações do projeto
"""
import streamlit as st


def render_about_page():
    """Renderiza a página Sobre"""
    
    st.markdown("# Sobre o AEGIS Habitat Layout Creator")
    
    # Hero section
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(79, 70, 229, 0.1)); 
                padding: 2rem; border-radius: 10px; border-left: 4px solid #6366f1; margin-bottom: 2rem; text-align: center;'>
        <h2 style='color: #6366f1; margin-top: 0;'>AEGIS Habitat Layout Creator</h2>
        <p style='color: #E2E8F0; font-size: 1.2rem; line-height: 1.8;'>
            Ferramenta interativa de design para habitats espaciais seguindo padrões NASA HIDH
        </p>
        <p style='color: #A0AEC0; font-size: 1rem;'>
            Versão 1.0.0 | Desenvolvido com Streamlit + Plotly
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Missão e Visão
    st.markdown("### Missão e Visão")
    
    mission_col1, mission_col2 = st.columns(2)
    
    with mission_col1:
        st.markdown("""
        <div style='background: rgba(72, 187, 120, 0.1); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #48bb78; height: 100%;'>
            <h4 style='color: #48bb78;'>Nossa Missão</h4>
            <p style='color: #E2E8F0; line-height: 1.8;'>
                Democratizar o acesso a ferramentas profissionais de design espacial, permitindo que 
                engenheiros, pesquisadores e entusiastas criem e validem layouts de habitats espaciais 
                seguindo os rigorosos padrões da NASA.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with mission_col2:
        st.markdown("""
        <div style='background: rgba(139, 92, 246, 0.1); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #8b5cf6; height: 100%;'>
            <h4 style='color: #8b5cf6;'>Nossa Visão</h4>
            <p style='color: #E2E8F0; line-height: 1.8;'>
                Ser a ferramenta de referência para design conceitual de habitats espaciais, 
                acelerando o desenvolvimento da arquitetura espacial e contribuindo para a 
                expansão sustentável da humanidade além da Terra.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sobre o projeto
    st.markdown("### Sobre o Projeto")
    
    st.markdown("""
    O **AEGIS Habitat Layout Creator** nasceu da necessidade de uma ferramenta acessível e intuitiva 
    para o design de habitats espaciais. Enquanto softwares profissionais de CAD e análise estrutural 
    são essenciais para projetos finais, há uma lacuna no estágio conceitual - onde ideias precisam 
    ser rapidamente testadas e validadas contra padrões NASA.
    
    Nossa ferramenta preenche essa lacuna, oferecendo:
    
    - **Validação Instantânea:** Métricas NASA calculadas em tempo real
    - **Visualizações Interativas:** Compreenda seu design em 2D e 3D
    - **Educação:** Explicações didáticas de conceitos e padrões espaciais
    - **Acessibilidade:** Interface web sem necessidade de instalação
    - **Open Standards:** Baseado em documentação pública da NASA HIDH
    """)
    
    st.markdown("---")
    
    # Recursos principais
    st.markdown("### Recursos Principais")
    
    feature_col1, feature_col2, feature_col3 = st.columns(3)
    
    with feature_col1:
        st.markdown("""
        **Design Interativo**
        - Configuração intuitiva de parâmetros
        - Feedback visual imediato
        - Múltiplas formas e estruturas
        - Customização completa de zonas
        """)
        
        st.markdown("""
        **Métricas NASA**
        - Cálculos conforme HIDH
        - Validação automática
        - Explicações detalhadas
        - Dashboard completo
        """)
    
    with feature_col2:
        st.markdown("""
        **Visualizações**
        - Plantas baixas 2D profissionais
        - Modelos 3D interativos
        - Rotação e zoom
        - Legendas e anotações
        """)
        
        st.markdown("""
        **Documentação**
        - Guia completo de uso
        - Glossário de termos
        - Dicas e melhores práticas
        - Referências NASA
        """)
    
    with feature_col3:
        st.markdown("""
        **Exportação**
        - Formato JSON estruturado
        - Todas as métricas incluídas
        - Timestamp automático
        - Fácil compartilhamento
        """)
        
        st.markdown("""
        **Acessibilidade**
        - Interface web responsiva
        - Sem instalação necessária
        - Suporte multi-idioma
        - Gratuito e open-source
        """)
    
    st.markdown("---")
    
    # Stack tecnológico
    st.markdown("### Stack Tecnológico")
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.markdown("""
        **Frontend:**
        - **Streamlit** - Framework de aplicações web interativas
        - **Plotly** - Gráficos e visualizações 3D interativas
        - **HTML/CSS** - Estilização customizada
        
        **Backend:**
        - **Python 3.11+** - Linguagem principal
        - **NumPy** - Cálculos numéricos eficientes
        - **Matemática Python** - Cálculos geométricos precisos
        """)
    
    with tech_col2:
        st.markdown("""
        **Arquitetura:**
        - Modular e escalável
        - Separação clara de responsabilidades
        - Componentes reutilizáveis
        - Fácil manutenção
        
        **Deployment:**
        - Docker containerizado
        - Cloud-ready (Google Cloud Run)
        - CI/CD pipeline
        - Escalabilidade horizontal
        """)
    
    st.markdown("---")
    
    # Padrões e referências
    st.markdown("### Padrões e Referências")
    
    st.markdown("""
    Esta ferramenta implementa cálculos e validações baseados em:
    
    **NASA Human Integration Design Handbook (HIDH):**
    - NASA/SP-2010-3407 - Volume habitável e requisitos espaciais
    - NASA-STD-3001 - Human Systems Integration Requirements
    - NASA Technical Standards - Habitability and Human Factors
    
    **Missões de Referência:**
    - **International Space Station (ISS)** - Dados operacionais de longa duração
    - **Skylab** - Primeiros estudos de volume habitável
    - **Mir Space Station** - Experiências soviéticas/russas
    - **Apollo/Gemini** - Missões de curta duração
    
    **Programas Futuros:**
    - **Artemis Gateway** - Estação lunar orbital
    - **Mars Design Reference Architectures** - Missões marcianas
    - **Commercial LEO Destinations** - Estações espaciais comerciais
    
    **Publicações Científicas:**
    - "Volume and Surface Area Allocations for Crew Habitability"
    - "Psychological and Human Factors in Long Duration Spaceflight"
    - "Architectural Approaches to Space Habitat Design"
    """)
    
    st.markdown("---")
    
    # Roadmap
    st.markdown("### Roadmap de Desenvolvimento")
    
    st.markdown("""
    **Versão Atual (1.0.0):**
    - Configuração completa de habitats cilíndricos e retangulares
    - Validação de métricas NASA HIDH
    - Visualizações 2D e 3D interativas
    - Customização de zonas funcionais
    - Exportação JSON
    - Documentação completa em português
    
    **Próximas Versões:**
    
    **v1.1.0 - Recursos Avançados:**
    - Importação de configurações JSON
    - Comparação lado a lado de múltiplos designs
    - Calculadora de massa estrutural
    - Análise de custos estimados
    
    **v1.2.0 - Colaboração:**
    - Compartilhamento de designs via URL
    - Galeria de designs comunitários
    - Comentários e feedback em designs
    - Sistema de versionamento de designs
    
    **v1.3.0 - Análises Avançadas:**
    - Simulação de fluxo de tripulação
    - Análise de compatibilidade de zonas
    - Otimização automática de layouts
    - Geração de relatórios PDF
    
    **v2.0.0 - Expansão:**
    - Habitats modulares conectados (multi-módulo)
    - Formas complexas (toroidais, em L, etc.)
    - Integração com CAD (exportação STEP/IGES)
    - API para integração com outras ferramentas
    """)
    
    st.markdown("---")
    
    # Contribuições
    st.markdown("### Como Contribuir")
    
    contribute_col1, contribute_col2 = st.columns(2)
    
    with contribute_col1:
        st.markdown("""
        **Para Desenvolvedores:**
        - Contribua com código no GitHub
        - Reporte bugs e issues
        - Sugira novos recursos
        - Melhore a documentação
        - Adicione testes automatizados
        
        **Tecnologias Necessárias:**
        - Python 3.11+
        - Streamlit
        - Git/GitHub
        - Docker (opcional)
        """)
    
    with contribute_col2:
        st.markdown("""
        **Para Não-Desenvolvedores:**
        - Compartilhe seus designs
        - Dê feedback sobre usabilidade
        - Contribua com documentação
        - Sugira melhorias de UI/UX
        - Divulgue a ferramenta
        
        **Áreas de Contribuição:**
        - Validação de cálculos
        - Casos de uso reais
        - Tutoriais e guias
        - Traduções
        """)
    
    st.markdown("---")
    
    # Licença
    st.markdown("### Licença e Uso")
    
    st.markdown("""
    **Licença:** MIT License
    
    Este projeto é **open-source** e livre para uso, modificação e distribuição, desde que 
    mantidos os créditos originais.
    
    **Você pode:**
    - Usar comercialmente
    - Modificar o código
    - Distribuir cópias
    - Uso privado
    - Criar trabalhos derivados
    
    **Você deve:**
    - Incluir a licença original
    - Manter créditos de copyright
    - Documentar mudanças significativas
    
    **Isenção de Responsabilidade:**
    
    Esta ferramenta é fornecida "como está" para fins educacionais e de design conceitual. 
    **Não substitui análises estruturais, térmicas ou de sistemas profissionais** necessárias 
    para projetos de voo real. Sempre consulte engenheiros qualificados e siga regulamentações 
    aeroespaciais aplicáveis para designs de produção.
    """)
    
    st.markdown("---")
    
    # Contato e suporte
    st.markdown("### Contato e Suporte")
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        **Repositório do Projeto:**
        - GitHub: [AEGIS-Habitat-Layout-Creator](#)
        - Documentação: [Wiki do GitHub](#)
        - Issues: [GitHub Issues](#)
        
        **Comunidade:**
        - Discussions: [GitHub Discussions](#)
        - Updates: [Releases](#)
        """)
    
    with contact_col2:
        st.markdown("""
        **Redes Sociais:**
        - Twitter: [@AEGIS_Tools](#)
        - LinkedIn: [AEGIS Space Tools](#)
        
        **Suporte:**
        - Email: support@aegis-tools.com
        - FAQ: [Perguntas Frequentes](#)
        - Tutoriais: [YouTube Channel](#)
        """)
    
    st.markdown("---")
    
    # Agradecimentos
    st.markdown("### Agradecimentos")
    
    st.markdown("""
    Este projeto não seria possível sem:
    
    **NASA** - Por décadas de pesquisa em habitabilidade espacial e por disponibilizar publicamente 
    os padrões HIDH que formam a base desta ferramenta.
    
    **Comunidade Open-Source** - Streamlit, Plotly, e inúmeras bibliotecas Python que tornam 
    desenvolvimento rápido e acessível.
    
    **Pesquisadores e Engenheiros** - Cujo trabalho em arquitetura espacial, fatores humanos e 
    sistemas de suporte de vida informam os algoritmos e validações desta ferramenta.
    
    **Primeiros Usuários** - Pela paciência, feedback e sugestões que melhoraram significativamente 
    a usabilidade e precisão da ferramenta.
    
    **Você** - Por usar esta ferramenta e contribuir para o futuro da exploração espacial!
    """)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: rgba(99, 102, 241, 0.1); border-radius: 10px; margin-top: 2rem;'>
        <h3 style='color: #6366f1;'>Vamos Construir o Futuro Espacial Juntos!</h3>
        <p style='color: #E2E8F0; font-size: 1.1rem; line-height: 1.8;'>
            Cada grande jornada começa com um pequeno passo. Seu design pode ser o próximo habitat 
            a abrigar a humanidade entre as estrelas.
        </p>
        <p style='color: #A0AEC0; margin-top: 1rem;'>
            Made with love for the space community | © 2024 AEGIS Tools
        </p>
    </div>
    """, unsafe_allow_html=True)
