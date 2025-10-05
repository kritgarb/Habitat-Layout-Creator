# AEGIS Habitat Layout Creator

Aplicação Streamlit criada para o **NASA Space Apps Challenge 2025**, oferecendo uma experiência moderna e interativa para projetar habitats espaciais de acordo com os padrões oficiais da NASA.

## Referências Científicas

O projeto é fundamentado em documentação técnica e pesquisas oficiais da NASA:

1. **Defining the Net Habitable Volume for Long Duration Exploration Missions** - Minimum volume requirements
2. **Moon to Mars Architecture Definition Document** - Launch envelope and architecture requirements
3. **Deep Space Habitability Design Guidelines** (NASA NextSTEP Phase 2) - Ergonomic and environmental standards
4. **Internal Layout Assessment of a Lunar Surface Habitat** - Functional zoning strategies
5. **NASA's M2M Transit Habitat Refinement Point of Departure Design** - Transit habitat design
6. **Review of Habitable Softgoods Inflatable Design** - Rigid vs inflatable structures
7. **Overview of NASA's MMPACT** - Autonomous construction on lunar surface
8. **A Tool for Automated Design and Evaluation of Habitat Interior Layouts** - Layout efficiency metrics
9. **Multi-functionality in Space** - Multi-functional space optimization
10. **Food Production on the Moon and in Remote Areas** - Food production and ECLSS integration

Referências detalhadas: veja `docs_archive/TECHNICAL.md`

## Funcionalidades

### Interface Moderna
- Tema escuro com gradiente roxo inspirado na identidade AEGIS
- Fundo espacial estático com estrelas e nebulosas
- Menu principal com botões responsivos e favicon personalizado
- Logo da equipe e foto do time na página “Sobre”
- Rodapé com logos da ENTERPRISE, TIC, NSA 

### Núcleo da Aplicação
- Criação de habitats cilíndricos ou retangulares
- Cálculo automático de volume, NHV e áreas úteis por zona
- Configuração de parâmetros de missão (tripulação, duração, gravidade)
- Validação em tempo real conforme diretrizes NASA HIDH
- Visualizações interativas 2D (planta baixa) e 3D (Plotly)
- Exportação de configuração completa em JSON
- Métricas didáticas com explicações e status (aprovado/atenção)

### Páginas Disponíveis
- **Início**: visão geral, guia de uso e glossário resumido
- **Layout 2D**: planta baixa interativa com métricas-chave
- **Layout 3D**: modelo tridimensional navegável do habitat
- **Métricas NASA**: dashboard detalhado com padrões e recomendações
- **Documentação**: tutoriais, troubleshooting e referências adicionais
- **Sobre**: missão do projeto, equipe AEGIS/ENTERPRISE e roadmap

## Estrutura do Projeto

```
Habitat-Layout-Creator/
├── app.py                     # Aplicação Streamlit multipáginas
├── requirements.txt           # Dependências Python
├── Dockerfile                 # Build Docker (opcional)
├── docker-compose.yml         # Execução Docker local (opcional)
├── README.md                  # Documentação principal
├── LICENSE                    # Licença MIT
├── data/
│   └── example_layout.json    # Exemplo de configuração exportada
├── docs_archive/              # Documentação legada
├── src/
│   ├── components/            # Componentes reutilizáveis (sidebar, métricas, exportação)
│   ├── config/                # Estilos e constantes do projeto
│   ├── pages/                 # Páginas Streamlit (Início, Layout 2D/3D, Métricas, Documentação, Sobre)
│   ├── utils/                 # Funções de cálculo e validação NASA
│   ├── visualizations/        # Renderizações 2D/3D com Plotly
│   ├── logo/                  # Identidade visual AEGIS
│   └── img/                   # Foto do grupo e logos de parceiros
└── venv/                      # Ambiente virtual (opcional)
```

## Stack Tecnológico

- **Python 3.11+** – linguagem principal
- **Streamlit** – framework para construção rápida de dashboards interativos
- **Plotly** – gráficos 2D/3D utilizados nas páginas de layout
- **NumPy** – cálculos geométricos e métricas de habitabilidade
- **CairoSVG & Pillow** – suporte a manipulação de SVG/PNG quando necessário
- **Docker** – execução containerizada opcional

## Guia Rápido

### Ambiente Local

1. **Criar e ativar o ambiente virtual**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Instalar dependências**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Executar a aplicação**
   ```powershell
   streamlit run app.py
   ```

   Acesse em: **http://localhost:8501**

### Via Docker (opcional)

```powershell
docker build -t habitat-layout-creator .
docker run -p 8501:8501 habitat-layout-creator
# ou
docker-compose up
```

## Deploy em Nuvem

### Streamlit Community Cloud (mais rápido)
1. Faça fork ou torne este repositório público no GitHub.
2. Acesse [share.streamlit.io](https://share.streamlit.io) e conecte-se com sua conta GitHub.
3. Escolha o repositório, selecione a branch `main` e o arquivo `app.py`.
4. Defina variáveis de ambiente se necessário (não há obrigatórias atualmente) e clique em **Deploy**.

### Google Cloud Run (contenierizado)
Pré-requisitos:
- Google Cloud CLI instalado e autenticado (`gcloud auth login`).
- Projeto com faturamento habilitado.

Passos principais:
```bash
# 1. Build e push da imagem
gcloud builds submit --tag gcr.io/SEU_PROJETO/habitat-layout-creator:latest

# 2. Deploy no Cloud Run
gcloud run deploy habitat-layout-creator \
   --image gcr.io/SEU_PROJETO/habitat-layout-creator:latest \
   --platform managed \
   --region southamerica-east1 \
   --allow-unauthenticated \
   --port 8501
```

> **Observação:** Não conseguimos publicar diretamente a partir deste ambiente, mas os passos acima são suficientes para reproduzir o deploy em qualquer conta.

## Como Utilizar

1. **Configurar Habitat** – utilize o painel lateral para definir forma (cilíndrica ou retangular), dimensões e zonas funcionais.
2. **Ajustar Parâmetros de Missão** – informe tripulação, duração, fator de uso e ambiente gravitacional.
3. **Revisar Métricas** – acompanhe volume, NHV e área mínima em cartões coloridos e explicativos.
4. **Validar Padrões** – indicadores verdes sinalizam conformidade com NASA HIDH; amarelo/vermelho destacam itens críticos.
5. **Explorar Visualizações** – na aba Layout 2D veja planta baixa com detalhes por zona; em Layout 3D gire/zoome o habitat interativo.
6. **Estudar Documentação** – a página Documentação reúne guias, glossário e troubleshooting.
7. **Exportar Configuração** – baixe um JSON completo com parâmetros e métricas da missão.

## Padrões NASA Implementados

- **NHV mínimo**: ≥ 25 m³ por pessoa (Net Habitable Volume)
- **Área de piso mínima**: ≥ 10 m² por pessoa
- **Envelope de lançamento**: SLS (Ø ≤ 8,4 m) e Starship (Ø ≤ 9,0 m)
- **Zonas funcionais**: seis zonas com áreas mínimas recomendadas
- **Suporte de vida**: cálculo estimado de água (2,5 L/dia/pessoa)

## Arquitetura de Código

O projeto segue uma arquitetura modular para facilitar manutenção e evolução:

- **`app.py`** – orquestra as páginas, aplica o CSS customizado e controla navegação
- **`src/pages/`** – páginas independentes (Início, Layout 2D/3D, Métricas, Documentação, Sobre)
- **`src/components/`** – componentes reutilizáveis (painel de configuração, métricas, exportação)
- **`src/utils/`** – cálculos geométricos e validadores de requisitos NASA
- **`src/config/`** – estilos, constantes e schema base
- **`src/visualizations/`** – geração dos gráficos Plotly 2D/3D
- **`src/logo/` & `src/img/`** – identidade visual, foto do time e logos de parceiros

## Contribuindo

Contribuições são bem-vindas! Você pode:
- Abrir issues com bugs ou ideias
- Enviar pull requests com melhorias ou correções
- Sugerir novas métricas/padrões NASA
- Aprimorar documentação e exemplos de uso

## Licença

Licença MIT – veja o arquivo [LICENSE](LICENSE) para detalhes.

## Agradecimentos

- NASA Space Apps Challenge 2025
- NASA Human Integration Design Standards (NASA-STD-3001)
- ISS Habitat Design Experience

---

Projeto desenvolvido pela equipe ENTERPRISE para o NASA Space Apps Challenge 2025.
