# 🗺️ Mapa Visual do Projeto - Habitat Layout Creator

```
📦 Habitat-Layout-Creator
│
├─── 📱 INTERFACE DO USUÁRIO
│    └─── app.py
│         ├─ Inputs (sidebar)
│         ├─ Cálculos principais
│         ├─ Métricas visuais
│         └─ Visualizações 3D/2D
│
├─── 🔧 LÓGICA DE NEGÓCIO
│    │
│    ├─── src/config/
│    │    ├─ constants.py          🔵 EXPANDIDO
│    │    │  ├─ Padrões NASA (NHV, áreas)
│    │    │  ├─ Recursos (água, O₂, comida)
│    │    │  ├─ Envelope de lançamento
│    │    │  ├─ Dimensões ergonômicas
│    │    │  ├─ Padrões ambientais
│    │    │  ├─ Iluminação
│    │    │  ├─ Zonas funcionais
│    │    │  ├─ Produção de alimentos
│    │    │  ├─ Tipos de missão
│    │    │  └─ Tipos de habitat
│    │    │
│    │    ├─ design_guidelines.py  🟢 NOVO
│    │    │  ├─ Classe LayoutMetrics
│    │    │  ├─ HABITABILITY_DIMENSIONS
│    │    │  ├─ ENVIRONMENTAL_STANDARDS
│    │    │  ├─ MULTIFUNCTIONAL_SPACES
│    │    │  ├─ RECOMMENDED_ADJACENCIES
│    │    │  ├─ FOOD_PRODUCTION_CONFIG
│    │    │  ├─ DESIGN_VALIDATION_RULES
│    │    │  └─ Funções de validação
│    │    │
│    │    └─ styles.py
│    │
│    ├─── src/utils/
│    │    ├─ calculations.py
│    │    │  ├─ calculate_cylinder_volume()
│    │    │  ├─ calculate_box_volume()
│    │    │  ├─ calculate_nhv()
│    │    │  └─ allocate_zones()
│    │    │
│    │    └─ validators.py         🔵 EXPANDIDO
│    │       ├─ validate_nasa_standards()      (expandida)
│    │       ├─ validate_dimensions()          (nova)
│    │       ├─ validate_environmental_conditions() (nova)
│    │       ├─ validate_zone_incompatibilities()  (nova)
│    │       ├─ calculate_layout_efficiency()      (nova)
│    │       ├─ validate_privacy_requirements()    (nova)
│    │       └─ check_launch_vehicle_compatibility()
│    │
│    ├─── src/components/
│    │    ├─ sidebar.py
│    │    ├─ metrics.py
│    │    └─ export.py
│    │
│    └─── src/visualizations/
│         ├─ layout_3d.py
│         └─ layout_2d.py
│
└─── 📚 DOCUMENTAÇÃO
     │
     ├─── docs/                    🟢 PASTA NOVA
     │    ├─ REFERENCES.md         🟢 NOVO (720 linhas)
     │    │  └─ 11 referências NASA completas
     │    │     ├─ Conceitos implementados
     │    │     ├─ Localização no código
     │    │     ├─ Exemplos de uso
     │    │     └─ Status de implementação
     │    │
     │    ├─ USAGE_GUIDE.md        🟢 NOVO (400 linhas)
     │    │  └─ Guia completo de uso
     │    │     ├─ Como usar constantes
     │    │     ├─ Como usar validações
     │    │     ├─ Como usar guidelines
     │    │     ├─ 3 exemplos completos
     │    │     └─ Dashboard de métricas
     │    │
     │    ├─ IMPLEMENTATION_SUMMARY.md  🟢 NOVO (430 linhas)
     │    │  └─ Resumo técnico
     │    │     ├─ Trabalho concluído
     │    │     ├─ Estatísticas
     │    │     ├─ Checklist de qualidade
     │    │     └─ Rastreabilidade
     │    │
     │    └─ QUICK_INDEX.md        🟢 NOVO (280 linhas)
     │       └─ Índice rápido
     │          ├─ Por conceito NASA
     │          ├─ Por arquivo
     │          ├─ Por funcionalidade
     │          └─ Por referência
     │
     ├─── docs_archive/
     │    └─ TECHNICAL.md           🔵 EXPANDIDO (+250 linhas)
     │       ├─ Base científica (nova seção)
     │       ├─ Fundamentos matemáticos
     │       ├─ Padrões NASA
     │       ├─ Métricas avançadas (nova seção)
     │       ├─ Produção de alimentos (nova seção)
     │       ├─ Tipos de estrutura (nova seção)
     │       ├─ Tipos de missão (nova seção)
     │       ├─ Padrões ambientais (nova seção)
     │       ├─ Dimensões ergonômicas (nova seção)
     │       └─ Multi-funcionalidade (nova seção)
     │
     ├─── README.md                 🔵 ATUALIZADO
     │    └─ + Seção "Scientific Foundation"
     │
     └─── CHANGELOG.md              🟢 NOVO
          └─ Histórico de versões
```

---

## 🔄 Fluxo de Dados

```
┌─────────────────┐
│   USUÁRIO       │
│  (Streamlit UI) │
└────────┬────────┘
         │ inputs (dimensões, tripulação, etc.)
         ▼
┌─────────────────────────────────────┐
│         app.py                      │
│  ┌─────────────────────────────┐   │
│  │  1. Renderiza Sidebar        │   │
│  │     └─ src/components/       │   │
│  │        sidebar.py            │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │  2. Cálculos Principais      │   │
│  │     └─ src/utils/            │   │
│  │        calculations.py       │   │
│  │        ├─ calculate_volume() │   │
│  │        ├─ calculate_nhv()    │   │
│  │        └─ allocate_zones()   │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │  3. Validações               │   │
│  │     └─ src/utils/            │   │
│  │        validators.py         │   │
│  │        ├─ validate_nasa_*()  │   │
│  │        ├─ validate_dims()    │   │
│  │        └─ calculate_eff()    │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │  4. Renderiza Métricas       │   │
│  │     └─ src/components/       │   │
│  │        metrics.py            │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │  5. Visualizações            │   │
│  │     └─ src/visualizations/   │   │
│  │        ├─ layout_2d.py       │   │
│  │        └─ layout_3d.py       │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│  VISUALIZAÇÃO   │
│  (Plotly 3D/2D) │
└─────────────────┘
```

---

## 📋 Dependências entre Módulos

```
app.py
  ├─── src/config/constants.py
  │    └─ Fornece: Constantes NASA, zonas, cores
  │
  ├─── src/config/styles.py
  │    └─ Fornece: CSS customizado
  │
  ├─── src/utils/calculations.py
  │    ├─ Usa: constants.py
  │    └─ Fornece: Cálculos de volume, NHV, áreas
  │
  ├─── src/utils/validators.py
  │    ├─ Usa: constants.py
  │    └─ Fornece: Validações NASA, métricas
  │
  ├─── src/components/sidebar.py
  │    ├─ Usa: constants.py
  │    └─ Fornece: Interface de entrada
  │
  ├─── src/components/metrics.py
  │    ├─ Usa: constants.py
  │    └─ Fornece: Exibição de métricas
  │
  ├─── src/components/export.py
  │    └─ Fornece: Exportação JSON
  │
  └─── src/visualizations/
       ├─ layout_2d.py
       │  ├─ Usa: constants.py (cores, nomes)
       │  └─ Fornece: Visualização 2D Plotly
       │
       └─ layout_3d.py
          ├─ Usa: constants.py (cores, nomes)
          └─ Fornece: Visualização 3D Plotly
```

---

## 🎯 Referências NASA → Código

```
NASA DOCUMENTS
     │
     ├─── Defining Net Habitable Volume
     │    └─→ constants.py (MIN_NHV_PER_PERSON)
     │        └─→ validators.py (validate_nasa_standards)
     │            └─→ app.py (validação principal)
     │
     ├─── Moon to Mars Architecture
     │    └─→ constants.py (SLS_*, STARSHIP_*, MISSION_TYPES)
     │        └─→ validators.py (check_launch_vehicle_compatibility)
     │
     ├─── Deep Space Habitability Guidelines
     │    ├─→ constants.py (MIN_CEILING_HEIGHT, TEMP_*, etc.)
     │    ├─→ design_guidelines.py (HABITABILITY_DIMENSIONS, ENVIRONMENTAL_STANDARDS)
     │    └─→ validators.py (validate_dimensions, validate_environmental_conditions)
     │
     ├─── Internal Layout Assessment
     │    └─→ constants.py (ZONE_MIN_AREA, INCOMPATIBLE_ZONES)
     │        ├─→ calculations.py (allocate_zones)
     │        └─→ validators.py (validate_zone_incompatibilities)
     │
     ├─── M2M Transit Habitat
     │    └─→ constants.py (MIN_NHV_PER_PERSON_TRANSIT, MISSION_TYPES['transit'])
     │        └─→ validators.py (validate_privacy_requirements)
     │
     ├─── Softgoods Inflatable Design
     │    └─→ constants.py (HABITAT_TYPES)
     │
     ├─── Automated Design Tool
     │    └─→ design_guidelines.py (LayoutMetrics class)
     │        └─→ validators.py (calculate_layout_efficiency)
     │
     ├─── Multi-functionality in Space
     │    └─→ design_guidelines.py (MULTIFUNCTIONAL_SPACES)
     │
     └─── Food Production on the Moon
          └─→ constants.py (FOOD_PRODUCTION_*)
              └─→ design_guidelines.py (FOOD_PRODUCTION_CONFIG)
```

---

## 🔍 Como Navegar no Projeto

### 1. Quero Entender as Referências NASA
```
START → docs/REFERENCES.md
        ├─ Ver conceitos implementados
        ├─ Ver localização no código
        └─ Ver status de implementação
```

### 2. Quero Usar as Funcionalidades
```
START → docs/USAGE_GUIDE.md
        ├─ Ver exemplos de código
        ├─ Ver casos de uso
        └─ Ver como integrar
```

### 3. Quero Encontrar Algo Rápido
```
START → docs/QUICK_INDEX.md
        ├─ Buscar por conceito
        ├─ Buscar por arquivo
        └─ Buscar por funcionalidade
```

### 4. Quero Saber O Que Foi Feito
```
START → docs/IMPLEMENTATION_SUMMARY.md
        ├─ Ver estatísticas
        ├─ Ver checklist
        └─ Ver rastreabilidade
```

### 5. Quero Entender a Matemática
```
START → docs_archive/TECHNICAL.md
        ├─ Ver fórmulas
        ├─ Ver exemplos
        └─ Ver padrões NASA
```

### 6. Quero Contribuir
```
START → CHANGELOG.md
        ├─ Ver histórico
        ├─ Ver versões
        └─ Ver planejamento
```

---

## 📊 Estatísticas do Projeto

### Por Tipo de Arquivo

```
Python (.py)
├─ app.py                    121 linhas
├─ src/config/
│  ├─ constants.py           189 linhas (109 → 189, +80)
│  ├─ design_guidelines.py   420 linhas (NOVO)
│  └─ styles.py              ~50 linhas
├─ src/utils/
│  ├─ calculations.py        ~120 linhas
│  └─ validators.py          260 linhas (80 → 260, +180)
├─ src/components/
│  ├─ sidebar.py             ~100 linhas
│  ├─ metrics.py             ~80 linhas
│  └─ export.py              ~60 linhas
└─ src/visualizations/
   ├─ layout_2d.py           ~150 linhas
   └─ layout_3d.py           ~120 linhas

TOTAL PYTHON: ~1,670 linhas

Markdown (.md)
├─ docs/
│  ├─ REFERENCES.md          720 linhas (NOVO)
│  ├─ USAGE_GUIDE.md         400 linhas (NOVO)
│  ├─ IMPLEMENTATION_SUMMARY.md  430 linhas (NOVO)
│  └─ QUICK_INDEX.md         280 linhas (NOVO)
├─ docs_archive/
│  └─ TECHNICAL.md           915 linhas (665 → 915, +250)
├─ README.md                 182 linhas (162 → 182, +20)
├─ CHANGELOG.md              280 linhas (NOVO)
└─ PROJECT_MAP.md            290 linhas (este arquivo, NOVO)

TOTAL MARKDOWN: ~3,497 linhas
```

### Crescimento do Projeto

```
Versão 1.0.0:
- Python: ~990 linhas
- Markdown: ~827 linhas
- Total: ~1,817 linhas

Versão 1.1.0:
- Python: ~1,670 linhas (+680)
- Markdown: ~3,497 linhas (+2,670)
- Total: ~5,167 linhas (+3,350)

Crescimento: +184%
```

---

## 🎨 Legenda de Símbolos

- 🟢 **NOVO**: Arquivo criado na v1.1.0
- 🔵 **EXPANDIDO**: Arquivo modificado substancialmente na v1.1.0
- 🔄 **MODIFICADO**: Arquivo com pequenas alterações
- ⭐ **DESTAQUE**: Funcionalidade importante
- 📁 **PASTA**: Diretório
- 📄 **ARQUIVO**: Arquivo individual
- 🔗 **LINK**: Referência cruzada
- ✅ **IMPLEMENTADO**: Funcionalidade completa
- 🔄 **EM DESENVOLVIMENTO**: Funcionalidade parcial
- 📋 **PLANEJADO**: Funcionalidade futura

---

## 🚀 Próximos Passos Sugeridos

### Para Desenvolvedores

1. **Implementar UI para Métricas Avançadas**
   ```
   app.py
   ├─ Importar: LayoutMetrics from design_guidelines
   ├─ Calcular: evaluate_layout_quality()
   └─ Exibir: Dashboard com st.metric()
   ```

2. **Adicionar Seleção de Tipo de Missão**
   ```
   src/components/sidebar.py
   ├─ Adicionar: st.selectbox("Mission Type", MISSION_TYPES.keys())
   └─ Passar: mission_type para validações
   
   app.py
   └─ Usar: validate_nasa_standards(..., mission_type=selected_mission)
   ```

3. **Validação Visual de Dimensões**
   ```
   app.py
   ├─ Importar: validate_dimensions from validators
   ├─ Validar: Altura do teto, largura de corredor
   └─ Exibir: Warnings visuais com st.warning()
   ```

### Para Usuários

1. **Explorar Referências**
   - Ler `docs/REFERENCES.md` para entender a base científica
   - Ver como cada documento NASA é aplicado no código

2. **Testar Funcionalidades**
   - Seguir exemplos em `docs/USAGE_GUIDE.md`
   - Experimentar diferentes configurações de habitat

3. **Contribuir**
   - Reportar bugs via GitHub Issues
   - Sugerir novas funcionalidades baseadas em documentos NASA

---

**Última atualização**: 4 de outubro de 2025  
**Versão**: 1.1.0
