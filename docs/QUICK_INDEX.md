# 🔍 Índice Rápido - Onde Encontrar Cada Conceito

Este é um índice rápido para localizar rapidamente onde cada conceito NASA está implementado no código.

---

## 📐 Por Conceito NASA

### Volume Habitável Líquido (NHV)
- **Valor**: 25 m³/pessoa (superfície), 27 m³/pessoa (trânsito)
- **Constante**: `MIN_NHV_PER_PERSON`, `MIN_NHV_PER_PERSON_TRANSIT`
- **Arquivo**: `src/config/constants.py`
- **Validação**: `validate_nasa_standards()` em `src/utils/validators.py`
- **Cálculo**: `calculate_nhv()` em `src/utils/calculations.py`
- **Referência**: "Defining the Net Habitable Volume for Long Duration Exploration Missions"

### Envelope de Lançamento
- **Valores**: SLS (8.4m × 27.4m), Starship (9.0m × 17.24m)
- **Constantes**: `SLS_MAX_DIAMETER`, `SLS_MAX_HEIGHT`, `STARSHIP_MAX_DIAMETER`, `STARSHIP_MAX_HEIGHT`
- **Arquivo**: `src/config/constants.py`
- **Validação**: `check_launch_vehicle_compatibility()` em `src/utils/validators.py`
- **Referência**: "Moon to Mars Architecture Definition Document"

### Dimensões Ergonômicas
- **Valores**: Teto (2.1m), Corredor (0.8m), Porta (0.7m × 1.9m)
- **Constantes**: `MIN_CEILING_HEIGHT`, `MIN_CORRIDOR_WIDTH`, `MIN_DOOR_WIDTH`, `MIN_DOOR_HEIGHT`
- **Arquivo**: `src/config/constants.py`
- **Dicionário**: `HABITABILITY_DIMENSIONS` em `src/config/design_guidelines.py`
- **Validação**: `validate_dimensions()` em `src/utils/validators.py`
- **Referência**: "Deep Space Habitability Design Guidelines (NASA NextSTEP Phase 2)"

### Padrões Ambientais
- **Valores**: Temp (18-27°C), Umidade (30-70%), CO₂ (<5.3 mmHg), Ruído (60-70 dB)
- **Constantes**: `TEMP_MIN/MAX`, `HUMIDITY_MIN/MAX`, `MAX_CO2`, `MAX_NOISE_SLEEP/WORK`
- **Arquivo**: `src/config/constants.py`
- **Dicionário**: `ENVIRONMENTAL_STANDARDS` em `src/config/design_guidelines.py`
- **Validação**: `validate_environmental_conditions()` em `src/utils/validators.py`
- **Referência**: "Deep Space Habitability Design Guidelines"

### Zonamento Funcional
- **Zonas**: Sleep, Hygiene, Kitchen, Exercise, Storage, Work/Leisure
- **Constantes**: `ZONE_MIN_AREA`, `ZONE_COLORS`, `ZONE_NAMES`
- **Arquivo**: `src/config/constants.py`
- **Alocação**: `allocate_zones()` em `src/utils/calculations.py`
- **Referência**: "Internal Layout Assessment of a Lunar Surface Habitat"

### Zonas Incompatíveis
- **Pares**: (sleep, exercise), (sleep, kitchen), (sleep, hygiene)
- **Constante**: `INCOMPATIBLE_ZONES`
- **Arquivo**: `src/config/constants.py`
- **Dicionário**: `RECOMMENDED_ADJACENCIES` em `src/config/design_guidelines.py`
- **Validação**: `validate_zone_incompatibilities()` em `src/utils/validators.py`
- **Referência**: "Internal Layout Assessment of a Lunar Surface Habitat"

### Tipos de Missão
- **Tipos**: Transit, Lunar Surface, Mars Surface
- **Constante**: `MISSION_TYPES` (dict completo)
- **Arquivo**: `src/config/constants.py`
- **Referências**: "M2M Transit Habitat", "Moon to Mars Architecture"

### Tipos de Estrutura
- **Tipos**: Rigid (150 kg/m³), Inflatable (40 kg/m³, 3.5× eficiência)
- **Constante**: `HABITAT_TYPES` (dict completo)
- **Arquivo**: `src/config/constants.py`
- **Referência**: "Review of Habitable Softgoods Inflatable Design"

### Produção de Alimentos
- **Valores**: Hidroponia (6 m²/pessoa, 0.5 kg O₂/dia)
- **Constantes**: `FOOD_PRODUCTION_AREA_PER_PERSON`, `FOOD_O2_PRODUCTION`
- **Arquivo**: `src/config/constants.py`
- **Dicionário**: `FOOD_PRODUCTION_CONFIG` em `src/config/design_guidelines.py`
- **Referência**: "Food Production on the Moon and in Remote Areas"

### Métricas de Eficiência
- **Métricas**: Space Efficiency (≥75%), Circulation (15-25%), Privacy (100%)
- **Classe**: `LayoutMetrics` em `src/config/design_guidelines.py`
- **Funções**: 
  - `calculate_space_efficiency()`
  - `calculate_circulation_index()`
  - `calculate_privacy_index()`
  - `evaluate_layout_quality()`
- **Validação**: `calculate_layout_efficiency()` em `src/utils/validators.py`
- **Referência**: "A Tool for Automated Design and Evaluation of Habitat Interior Layouts"

### Multi-funcionalidade
- **Espaços**: Dining+Meeting+Recreation, Exercise+Medical, etc.
- **Dicionário**: `MULTIFUNCTIONAL_SPACES` em `src/config/design_guidelines.py`
- **Referência**: "Multi-functionality in Space"

### Recursos de Suporte à Vida
- **Valores**: Água (2.5 L/dia), O₂ (0.84 kg/dia), Comida (0.62 kg/dia)
- **Constantes**: `WATER_PER_DAY_PER_PERSON`, `OXYGEN_PER_DAY_PER_PERSON`, `FOOD_PER_DAY_PER_PERSON`
- **Arquivo**: `src/config/constants.py`
- **Referência**: "NASA-STD-3001" e "Habitats and Surface Construction Technology"

---

## 📁 Por Arquivo

### `src/config/constants.py`
Constantes numéricas e configurações básicas:
- Padrões NASA (NHV, área)
- Recursos de suporte à vida
- Envelope de lançamento
- Dimensões ergonômicas
- Padrões ambientais
- Iluminação
- Cores e nomes de zonas
- Áreas mínimas por zona
- Zonas incompatíveis
- Produção de alimentos
- Tipos de missão
- Tipos de habitat

### `src/config/design_guidelines.py`
Diretrizes avançadas e classes:
- Classe `LayoutMetrics` (métricas de eficiência)
- `HABITABILITY_DIMENSIONS` (dimensões detalhadas)
- `ENVIRONMENTAL_STANDARDS` (padrões ambientais detalhados)
- `MULTIFUNCTIONAL_SPACES` (espaços multi-funcionais)
- `RECOMMENDED_ADJACENCIES` (adjacências recomendadas/incompatíveis)
- `FOOD_PRODUCTION_CONFIG` (hidroponia e aeroponia)
- `DESIGN_VALIDATION_RULES` (regras de validação)
- Funções de validação de habitabilidade
- Função de cálculo de adjacência

### `src/utils/validators.py`
Funções de validação:
- `validate_nasa_standards()` - Valida NHV e área (expandida)
- `validate_dimensions()` - Valida dimensões ergonômicas (nova)
- `validate_environmental_conditions()` - Valida temperatura, umidade, etc. (nova)
- `validate_zone_incompatibilities()` - Verifica zonas incompatíveis (nova)
- `calculate_layout_efficiency()` - Calcula eficiência e circulação (nova)
- `validate_privacy_requirements()` - Valida privacidade (nova)
- `check_launch_vehicle_compatibility()` - Verifica envelope (existente)

### `src/utils/calculations.py`
Cálculos matemáticos:
- `calculate_cylinder_volume()`
- `calculate_box_volume()`
- `calculate_nhv()`
- `allocate_zones()`
- (Não modificado, mas usado pelas validações)

---

## 🎯 Por Funcionalidade

### Criar Novo Habitat
**Fluxo**:
1. Usuário define dimensões → `app.py`
2. Calcula volume → `src/utils/calculations.py`
3. Calcula NHV → `src/utils/calculations.py`
4. Valida padrões → `src/utils/validators.py`
5. Aloca zonas → `src/utils/calculations.py`
6. Visualiza → `src/visualizations/layout_3d.py`, `layout_2d.py`

**Constantes usadas**:
- `MIN_NHV_PER_PERSON` (constants.py)
- `MIN_FLOOR_AREA_PER_PERSON` (constants.py)
- `ZONE_MIN_AREA` (constants.py)

### Validar Habitat
**Validações disponíveis**:
1. NHV e área → `validate_nasa_standards()`
2. Dimensões → `validate_dimensions()`
3. Ambiente → `validate_environmental_conditions()`
4. Zonas → `validate_zone_incompatibilities()`
5. Eficiência → `calculate_layout_efficiency()`
6. Privacidade → `validate_privacy_requirements()`

### Calcular Métricas
**Métricas disponíveis**:
1. Space Efficiency → `LayoutMetrics.calculate_space_efficiency()`
2. Circulation Index → `LayoutMetrics.calculate_circulation_index()`
3. Privacy Index → `LayoutMetrics.calculate_privacy_index()`
4. Layout Quality → `LayoutMetrics.evaluate_layout_quality()`

---

## 🔗 Por Referência NASA

### 1. Defining the Net Habitable Volume
- **Constantes**: `MIN_NHV_PER_PERSON`, `MIN_NHV_PER_PERSON_TRANSIT`
- **Funções**: `calculate_nhv()`, `validate_nasa_standards()`
- **Localização**: constants.py, calculations.py, validators.py

### 2. Moon to Mars Architecture Definition Document
- **Constantes**: `SLS_MAX_*`, `STARSHIP_MAX_*`, `MISSION_TYPES`
- **Funções**: `check_launch_vehicle_compatibility()`
- **Localização**: constants.py, validators.py

### 3. Habitats and Surface Construction Technology
- **Constantes**: `WATER_*`, `OXYGEN_*`, `FOOD_*`, `POWER_*`
- **Localização**: constants.py

### 4. Review of Habitable Softgoods Inflatable Design
- **Constantes**: `HABITAT_TYPES`
- **Localização**: constants.py

### 5. Overview of NASA's MMPACT
- **Status**: Documentado em REFERENCES.md
- **Implementação**: Planejada (baixa prioridade)

### 6. Internal Layout Assessment
- **Constantes**: `ZONE_MIN_AREA`, `INCOMPATIBLE_ZONES`
- **Funções**: `allocate_zones()`, `validate_zone_incompatibilities()`
- **Localização**: constants.py, calculations.py, validators.py

### 7. NASA's M2M Transit Habitat Refinement
- **Constantes**: `MIN_NHV_PER_PERSON_TRANSIT`, `MISSION_TYPES['transit']`
- **Funções**: `validate_privacy_requirements()`
- **Localização**: constants.py, validators.py

### 8. Deep Space Habitability Design Guidelines
- **Constantes**: `MIN_CEILING_HEIGHT`, `MIN_CORRIDOR_WIDTH`, etc.
- **Dicionários**: `HABITABILITY_DIMENSIONS`, `ENVIRONMENTAL_STANDARDS`
- **Funções**: `validate_dimensions()`, `validate_environmental_conditions()`
- **Localização**: constants.py, design_guidelines.py, validators.py

### 9. A Tool for Automated Design and Evaluation
- **Classe**: `LayoutMetrics`
- **Funções**: `calculate_layout_efficiency()`, todas as métricas
- **Localização**: design_guidelines.py, validators.py

### 10. Multi-functionality in Space
- **Dicionário**: `MULTIFUNCTIONAL_SPACES`
- **Localização**: design_guidelines.py

### 11. Food Production on the Moon
- **Constantes**: `FOOD_PRODUCTION_*`
- **Dicionário**: `FOOD_PRODUCTION_CONFIG`
- **Localização**: constants.py, design_guidelines.py

---

## 📖 Documentação

### Para Desenvolvedores
1. **Lista completa de referências**: `docs/REFERENCES.md`
2. **Fundamentos técnicos**: `docs_archive/TECHNICAL.md`
3. **Resumo de implementação**: `docs/IMPLEMENTATION_SUMMARY.md`

### Para Usuários
1. **Como usar**: `docs/USAGE_GUIDE.md`
2. **README geral**: `README.md`

### Para Contribuidores
1. **Este índice**: `docs/QUICK_INDEX.md`
2. **Estrutura do código**: Veja `docs/IMPLEMENTATION_SUMMARY.md`

---

## 🔍 Busca Rápida

### Preciso encontrar...

| O que | Onde |
|-------|------|
| Valor de uma constante NASA | `src/config/constants.py` |
| Como validar algo | `src/utils/validators.py` |
| Diretrizes de habitabilidade | `src/config/design_guidelines.py` |
| Fundamentos matemáticos | `docs_archive/TECHNICAL.md` |
| Lista de todas as referências | `docs/REFERENCES.md` |
| Exemplos de código | `docs/USAGE_GUIDE.md` |
| O que foi implementado | `docs/IMPLEMENTATION_SUMMARY.md` |
| Cálculos de volume/área | `src/utils/calculations.py` |
| Visualizações | `src/visualizations/` |
| UI principal | `app.py` |

---

## 🎯 Próximos Passos para Implementar

Se você quiser implementar novas funcionalidades baseadas nas referências:

### Alta Prioridade
1. **UI para tipo de missão**: Usar `MISSION_TYPES` de constants.py
2. **Dashboard de métricas**: Usar `LayoutMetrics` de design_guidelines.py
3. **Validação automática de dimensões**: Usar `validate_dimensions()` de validators.py

### Média Prioridade
4. **Seleção de estrutura**: Usar `HABITAT_TYPES` de constants.py
5. **Templates multi-funcionais**: Usar `MULTIFUNCTIONAL_SPACES` de design_guidelines.py
6. **Produção de alimentos**: Usar `FOOD_PRODUCTION_CONFIG` de design_guidelines.py

---

**Última atualização**: 4 de outubro de 2025
