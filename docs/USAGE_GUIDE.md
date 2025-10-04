# 🚀 Guia de Uso - Habitat Layout Creator

## Visão Geral

Este guia mostra como utilizar as funcionalidades baseadas nas referências técnicas da NASA implementadas na aplicação.

---

## 📋 Referências Implementadas

### ✅ Atualmente Disponível

1. **Volume Habitável Líquido (NHV)**
   - Validação de NHV ≥ 25 m³/pessoa
   - Baseado em: "Defining the Net Habitable Volume"

2. **Envelope de Lançamento**
   - Verificação de compatibilidade com SLS (8.4m) e Starship (9.0m)
   - Baseado em: "Moon to Mars Architecture Definition Document"

3. **Zonamento Funcional**
   - 6 zonas principais: Sleep, Hygiene, Kitchen, Exercise, Storage, Work/Leisure
   - Áreas mínimas por zona
   - Zonas incompatíveis identificadas
   - Baseado em: "Internal Layout Assessment"

4. **Visualizações 3D e 2D**
   - Plotly interativo com controles de zoom, pan e rotação

---

## Funcionalidades Expandidas

### Novas Constantes Disponíveis

No arquivo `src/config/constants.py`, você encontrará:

```python
# Recursos de Suporte à Vida
WATER_PER_DAY_PER_PERSON = 2.5  # litros (consumo)
WATER_HYGIENE_PER_DAY_PER_PERSON = 23.0  # litros (higiene)
OXYGEN_PER_DAY_PER_PERSON = 0.84  # kg
FOOD_PER_DAY_PER_PERSON = 0.62  # kg

# Dimensões Ergonômicas
MIN_CEILING_HEIGHT = 2.1  # metros
MIN_CORRIDOR_WIDTH = 0.8  # metros
MIN_DOOR_WIDTH = 0.7  # metros

# Padrões Ambientais
TEMP_MIN = 18  # °C
TEMP_MAX = 27  # °C
MAX_NOISE_SLEEP = 60  # dB
MAX_NOISE_WORK = 70  # dB

# Tipos de Missão
MISSION_TYPES = {
    "transit": {...},      # Habitat de trânsito Terra-Marte
    "lunar_surface": {...}, # Habitat de superfície lunar
    "mars_surface": {...}   # Habitat de superfície marciana
}

# Tipos de Estrutura
HABITAT_TYPES = {
    "rigid": {...},        # Estrutura rígida (alumínio)
    "inflatable": {...}    # Estrutura inflável (softgoods)
}
```

### Novas Validações

No arquivo `src/utils/validators.py`:

#### 1. Validação de Dimensões Ergonômicas

```python
from src.utils.validators import validate_dimensions

# Validar altura do teto
is_valid, issues = validate_dimensions(
    ceiling_height=2.3,
    corridor_width=1.0,
    door_dimensions=(0.8, 2.0)
)

print(f"Válido: {is_valid}")
for issue in issues:
    print(issue)
```

#### 2. Validação de Condições Ambientais

```python
from src.utils.validators import validate_environmental_conditions

# Validar temperatura, umidade, CO₂ e ruído
is_valid, issues = validate_environmental_conditions(
    temperature=22,
    humidity=50,
    co2_level=4.0,
    noise_level=55,
    zone_type="sleep"
)
```

#### 3. Validação de Incompatibilidades de Zonas

```python
from src.utils.validators import validate_zone_incompatibilities
from src.config.constants import INCOMPATIBLE_ZONES

zones = ["sleep", "exercise", "kitchen"]
warnings = validate_zone_incompatibilities(zones, INCOMPATIBLE_ZONES)

for warning in warnings:
    print(warning)
```

#### 4. Métricas de Eficiência de Layout

```python
from src.utils.validators import calculate_layout_efficiency

zones = {
    "sleep": {"area": 20},
    "hygiene": {"area": 10},
    "kitchen": {"area": 15},
    "work_leisure": {"area": 25}
}

metrics = calculate_layout_efficiency(zones, floor_area=100)

print(f"Eficiência de espaço: {metrics['space_efficiency']['value']:.1f}%")
print(f"Área de circulação: {metrics['circulation_index']['value']:.1f}%")
```

### Guidelines de Design

No arquivo `src/config/design_guidelines.py`:

#### 1. Classe LayoutMetrics

```python
from src.config.design_guidelines import LayoutMetrics

# Calcular eficiência de espaço
efficiency = LayoutMetrics.calculate_space_efficiency(
    usable_area=75,
    total_area=100
)
print(f"Eficiência: {efficiency}%")  # Target: ≥75%

# Calcular índice de circulação
circulation = LayoutMetrics.calculate_circulation_index(
    circulation_area=20,
    total_area=100
)
print(f"Circulação: {circulation}%")  # Target: 15-25%

# Avaliar qualidade geral do layout
quality = LayoutMetrics.evaluate_layout_quality(zones, floor_area, crew_size)
print(quality)
```

#### 2. Padrões de Habitabilidade

```python
from src.config.design_guidelines import (
    HABITABILITY_DIMENSIONS,
    ENVIRONMENTAL_STANDARDS,
    MULTIFUNCTIONAL_SPACES
)

# Acessar dimensões mínimas
min_ceiling = HABITABILITY_DIMENSIONS['ceiling']['min_height']
min_corridor = HABITABILITY_DIMENSIONS['corridors']['min_width']

# Acessar padrões ambientais
temp_range = (
    ENVIRONMENTAL_STANDARDS['temperature']['min'],
    ENVIRONMENTAL_STANDARDS['temperature']['max']
)

# Espaços multi-funcionais
dining_area = MULTIFUNCTIONAL_SPACES['dining_meeting_recreation']
print(f"Área: {dining_area['area_per_person']} m²/pessoa")
print(f"Funções: {', '.join(dining_area['functions'])}")
```

#### 3. Validação de Habitabilidade

```python
from src.config.design_guidelines import validate_habitability_standards

dimensions = {
    'ceiling_height': 2.3,
    'corridor_width': 1.0
}

environment = {
    'temperature': 22,
    'humidity': 50
}

result = validate_habitability_standards(dimensions, environment)

if result['is_valid']:
    print("✅ Habitat atende aos padrões de habitabilidade")
else:
    print("⚠️ Issues encontrados:")
    for issue in result['issues']:
        print(f"  - {issue['message']}")
```

---

## 🎯 Exemplos de Uso Completo

### Exemplo 1: Habitat de Trânsito para Marte

```python
import streamlit as st
from src.config.constants import MISSION_TYPES, MIN_NHV_PER_PERSON_TRANSIT
from src.utils.validators import validate_nasa_standards

# Configuração da missão
mission = MISSION_TYPES['transit']
crew_size = 4
duration_days = 210  # 7 meses

# Cálculos
total_volume = 500  # m³
nhv = total_volume * 0.7
nhv_per_person = nhv / crew_size

# Validação
is_valid, issues = validate_nasa_standards(
    nhv_per_person=nhv_per_person,
    floor_area_per_person=12,
    min_nhv=MIN_NHV_PER_PERSON_TRANSIT,  # 27 m³ para trânsito
    min_floor_area=10,
    mission_type="transit"
)

print(f"NHV/pessoa: {nhv_per_person:.1f} m³")
print(f"Válido para missão de trânsito: {is_valid}")
```

### Exemplo 2: Habitat Lunar com Produção de Alimentos

```python
from src.config.constants import FOOD_PRODUCTION_AREA_PER_PERSON, FOOD_O2_PRODUCTION

crew_size = 6
mission_duration_days = 180

# Área de produção de alimentos
food_area = FOOD_PRODUCTION_AREA_PER_PERSON * crew_size
print(f"Área de hidroponia necessária: {food_area} m²")

# Benefícios de O₂
o2_production = FOOD_O2_PRODUCTION * crew_size
print(f"Produção de O₂: {o2_production} kg/dia")

# Área total do habitat (incluindo produção de alimentos)
base_area = 80  # m² (áreas habitacionais)
total_area = base_area + food_area
print(f"Área total: {total_area} m²")
```

### Exemplo 3: Comparação de Estruturas (Rígida vs Inflável)

```python
from src.config.constants import HABITAT_TYPES

# Habitat rígido
rigid = HABITAT_TYPES['rigid']
volume_needed = 400  # m³
mass_rigid = volume_needed * rigid['mass_per_volume']

# Habitat inflável (mesmo volume habitável)
inflatable = HABITAT_TYPES['inflatable']
# Volume bruto maior devido à eficiência
volume_inflatable = volume_needed / inflatable['volume_efficiency']
mass_inflatable = volume_inflatable * inflatable['mass_per_volume']

print(f"Massa estrutura rígida: {mass_rigid} kg")
print(f"Massa estrutura inflável: {mass_inflatable} kg")
print(f"Economia de massa: {mass_rigid - mass_inflatable} kg ({(1 - mass_inflatable/mass_rigid)*100:.1f}%)")
```

---

## 📊 Dashboard de Métricas Avançadas

Você pode criar um dashboard completo usando as novas funcionalidades:

```python
import streamlit as st
from src.utils.validators import calculate_layout_efficiency, validate_privacy_requirements
from src.config.design_guidelines import LayoutMetrics

st.header("📊 Advanced Layout Metrics")

# Métricas de eficiência
metrics = calculate_layout_efficiency(zones, floor_area, crew_size)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Space Efficiency",
        f"{metrics['space_efficiency']['value']:.1f}%",
        delta=f"{metrics['space_efficiency']['value'] - 75:.1f}% vs target"
    )

with col2:
    st.metric(
        "Circulation Area",
        f"{metrics['circulation_index']['value']:.1f}%",
        delta="Optimal" if metrics['circulation_index']['status'] == 'pass' else "Review"
    )

with col3:
    is_adequate, msg = validate_privacy_requirements(crew_size, num_private_rooms)
    st.metric("Privacy Index", "100%" if is_adequate else f"{(num_private_rooms/crew_size)*100:.0f}%")
```

---

## 🔮 Funcionalidades Futuras Planejadas

Consulte [`docs/REFERENCES.md`](REFERENCES.md) para ver:

- ✅ Funcionalidades já implementadas
- 🔄 Funcionalidades em desenvolvimento
- 📋 Funcionalidades planejadas

### Alta Prioridade

1. **Seleção de Tipo de Missão**
   - Interface para escolher: Trânsito, Superfície Lunar, Superfície Marciana
   - Ajuste automático de requisitos (NHV, proteção, gravidade)

2. **Validação de Dimensões Ergonômicas**
   - Verificação automática de altura de teto, largura de corredor, portas
   - Warnings visuais no layout 3D

3. **Métricas de Eficiência na UI**
   - Dashboard com Space Efficiency, Circulation Index, Privacy Index
   - Gráficos de pontuação de adjacência

### Média Prioridade

4. **Seleção de Tipo de Estrutura**
   - Opção: Rígida vs Inflável
   - Cálculo de massa e volume empacotado
   - Análise de custo-benefício

5. **Espaços Multi-funcionais**
   - Templates de zonas multi-funcionais
   - Cálculo de economia de espaço

6. **Zona de Produção de Alimentos**
   - Opção de incluir hidroponia/aeroponia
   - Cálculo de produção de O₂ e alimentos
   - Integração com ECLSS

### Baixa Prioridade

7. **Simulação de Construção Autônoma (MMPACT)**
   - Para habitats lunares
   - Cálculo de regolito necessário

---

## 📚 Documentação Adicional

- **Referências Completas**: [`docs/REFERENCES.md`](REFERENCES.md)
- **Documentação Técnica**: [`docs_archive/TECHNICAL.md`](docs_archive/TECHNICAL.md)
- **Constantes NASA**: [`src/config/constants.py`](src/config/constants.py)
- **Guidelines de Design**: [`src/config/design_guidelines.py`](src/config/design_guidelines.py)
- **Validadores**: [`src/utils/validators.py`](src/utils/validators.py)

---

## 🤝 Contribuindo

Ao adicionar novas funcionalidades baseadas em documentos NASA:

1. **Adicione a referência** em `docs/REFERENCES.md`
2. **Documente constantes** em `src/config/constants.py` com comentários
3. **Cite a fonte** em docstrings de funções
4. **Atualize este guia** com exemplos de uso

---

**Última atualização**: 4 de outubro de 2025
