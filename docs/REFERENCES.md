# 📚 Referências Técnicas NASA - Habitat Layout Creator

Este documento lista todas as referências técnicas da NASA utilizadas no desenvolvimento do Habitat Layout Creator, organizadas por categoria e aplicação no projeto.

---

## 🎯 Referências Principais

### 1. Defining the Net Habitable Volume for Long Duration Exploration Missions

**Aplicação no Projeto**: Volume mínimo necessário para uma rede habitável de um habitat de trânsito à Marte.

**Conceitos Implementados**:
- Volume Habitável Líquido (NHV - Net Habitable Volume)
- Padrão mínimo: **25 m³ por pessoa** para missões de longa duração
- Fator de utilização: tipicamente 70% do volume total
- Diferenciação entre volume bruto e volume utilizável

**Localização no Código**:
```python
# src/config/constants.py
MIN_NHV_PER_PERSON = 25  # m³ por pessoa

# src/utils/calculations.py
def calculate_nhv(total_volume, usable_factor):
    return total_volume * usable_factor
```

**Critérios de Validação**:
- ✓ NHV/pessoa ≥ 25 m³ → Adequado para missões longas
- ⚠ NHV/pessoa < 25 m³ → Risco psicológico e operacional

---

### 2. Moon to Mars Architecture Definition Document

**Aplicação no Projeto**: Planos da NASA para missões futuras e arquitetura de sistemas.

**Conceitos Implementados**:
- Requisitos de envelope de lançamento (SLS, Starship)
- Fases de missão: Trânsito, Superfície Lunar, Superfície Marciana
- Integração de sistemas de suporte à vida
- Modularidade e expansibilidade de habitats

**Localização no Código**:
```python
# src/config/constants.py
SLS_MAX_DIAMETER = 8.4  # metros (Space Launch System)
STARSHIP_MAX_DIAMETER = 9.0  # metros (SpaceX Starship)
```

**Considerações de Design**:
- Habitats devem caber no envelope de lançamento
- Possibilidade de expansão modular
- Compatibilidade com diferentes destinos (Lua, Marte)

---

### 3. Habitats and Surface Construction Technology and Development Roadmap

**Aplicação no Projeto**: Tecnologias para construção de habitat e lista de componentes necessários.

**Conceitos Implementados**:
- Materiais estruturais para construção espacial
- Tecnologias de construção in-situ (ISRU)
- Sistemas de proteção contra radiação
- Sistemas de controle ambiental

**Zonas Funcionais Identificadas**:
```python
# src/config/constants.py
ZONE_MIN_AREA = {
    "sleep": 4.0,          # Quartos de dormir
    "hygiene": 2.0,        # Módulo de higiene
    "kitchen": 3.0,        # Galley/cozinha
    "exercise": 2.5,       # Área de exercício
    "storage": 3.0,        # Armazenamento
    "work_leisure": 5.0    # Trabalho e lazer
}
```

**Tecnologias Consideradas**:
- Estruturas rígidas vs infláveis
- Sistemas de blindagem contra radiação
- Sistemas ECLSS (Environmental Control and Life Support System)
- Integração de energia e comunicações

---

### 4. Review of Habitable Softgoods Inflatable Design, Analysis, Testing, and Potential Space Applications

**Aplicação no Projeto**: Aprofundamento de habitats infláveis e suas características.

**Conceitos de Design Inflável**:
- Maior volume por massa de lançamento
- Flexibilidade de configuração
- Desafios de rigidez estrutural
- Proteção contra micrometeoritos (MMOD)

**Vantagens dos Infláveis**:
- ✓ Volume 3-4x maior que estruturas rígidas
- ✓ Peso reduzido de lançamento
- ✓ Facilidade de empacotamento

**Desvantagens**:
- ⚠ Complexidade de vedação
- ⚠ Necessidade de camadas de proteção
- ⚠ Rigidez limitada para montagem de equipamentos

**Futuras Implementações**:
- Opção de seleção de tipo de habitat (rígido vs inflável)
- Cálculos específicos de massa por tipo
- Análise de custo-benefício

---

### 5. Overview of NASA's Moon to Mars Planetary Autonomous Construction Technology (MMPACT)

**Aplicação no Projeto**: Planos de arquitetura de habitat em solo lunar.

**Conceitos MMPACT**:
- Construção autônoma de habitats
- Uso de regolito lunar para construção
- Robótica e automação
- Pré-posicionamento de infraestrutura

**Requisitos de Solo Lunar**:
- Proteção contra radiação (regolito > 2m de cobertura)
- Estabilidade térmica
- Proteção contra micrometeoritos
- Integração com recursos locais (ISRU)

**Aplicações Futuras**:
- Modo "Habitat de Superfície Lunar"
- Cálculos de massa de regolito necessário
- Análise de estabilidade estrutural

---

### 6. Internal Layout Assessment of a Lunar Surface Habitat

**Aplicação no Projeto**: Modelo detalhado de layout em solo lunar.

**Princípios de Layout Implementados**:
- Zonamento funcional eficiente
- Separação de áreas incompatíveis
- Fluxo de movimento otimizado
- Acessibilidade e ergonomia

**Zonas Incompatíveis**:
```python
# src/config/constants.py
INCOMPATIBLE_ZONES = [
    ("sleep", "exercise"),   # Ruído
    ("sleep", "kitchen"),    # Odores e atividade
    ("sleep", "hygiene")     # Umidade e ruído
]
```

**Critérios de Avaliação**:
- Distância entre zonas
- Privacidade acústica
- Controle de contaminação
- Eficiência de circulação

---

### 7. NASA's Moon to Mars (M2M) Transit Habitat Refinement Point of Departure Design

**Aplicação no Projeto**: Modelo de layout fora de solo (habitat de trânsito).

**Características de Habitats de Trânsito**:
- Duração: 180-300 dias (viagem Terra-Marte)
- Gravidade zero ou artificial
- Espaço limitado
- Restrições psicológicas severas

**Requisitos Específicos**:
```python
# Exemplo de implementação futura
TRANSIT_HABITAT_REQUIREMENTS = {
    "min_nhv_per_person": 27,  # m³ (maior que superfície)
    "min_exercise_area": 4.0,  # m² (crítico em microgravidade)
    "min_privacy_volume": 5.0, # m³ (área privada por pessoa)
    "window_area": 0.5         # m² (importante para saúde mental)
}
```

**Considerações Psicológicas**:
- Janelas/visores externos (conexão com espaço)
- Áreas privadas para cada tripulante
- Espaços de socialização
- Variação visual e cores

---

### 8. Deep Space Habitability Design Guidelines Based on the NASA NextSTEP Phase 2 Ground Program

**Aplicação no Projeto**: Guia completo para design de habitat espacial.

**Diretrizes Principais**:

#### A. Dimensionamento Humano
- Altura mínima do teto: **2.1m**
- Largura mínima de corredor: **0.8m**
- Porta mínima: **0.7m largura × 1.9m altura**
- Área de trabalho: **1.5m²** por estação

#### B. Iluminação
- Iluminação circadiana (variável 200-500 lux)
- Controle individual de intensidade
- Temperatura de cor ajustável (2700K-6500K)

#### C. Acústica
- Nível máximo de ruído: **60 dB** (área de sono)
- Nível máximo de ruído: **70 dB** (áreas de trabalho)

#### D. Qualidade do Ar
- Temperatura: **18-27°C**
- Umidade relativa: **30-70%**
- CO₂ máximo: **5.3 mmHg** (0.7 kPa)

**Implementação Futura**:
```python
# src/config/design_guidelines.py
HABITABILITY_STANDARDS = {
    "dimensions": {
        "min_ceiling_height": 2.1,    # metros
        "min_corridor_width": 0.8,    # metros
        "min_door_width": 0.7,        # metros
        "min_door_height": 1.9,       # metros
        "workstation_area": 1.5       # m²
    },
    "environmental": {
        "temp_range": (18, 27),       # °C
        "humidity_range": (30, 70),   # %
        "max_co2": 5.3,               # mmHg
        "noise_sleep": 60,            # dB
        "noise_work": 70              # dB
    },
    "lighting": {
        "min_lux": 200,
        "max_lux": 500,
        "color_temp_range": (2700, 6500)  # Kelvin
    }
}
```

---

### 9. A Tool for Automated Design and Evaluation of Habitat Interior Layouts

**Aplicação no Projeto**: Método para medir a efetividade do design de interior do habitat.

**Métricas de Avaliação**:

#### A. Eficiência de Espaço
```python
Space_Efficiency = (Área_Utilizável / Área_Total) × 100%
```
Meta: ≥ 75%

#### B. Índice de Adjacência
Mede o quão bem as zonas relacionadas estão posicionadas:
```python
Adjacency_Score = Σ(Peso_Relação × Proximidade) / Total_Relações
```

#### C. Índice de Circulação
```python
Circulation_Index = Área_Circulação / Área_Total
```
Meta: 15-25% (equilíbrio entre acesso e desperdício)

#### D. Índice de Privacidade
```python
Privacy_Index = (Zonas_Privadas_Adequadas / Total_Tripulantes) × 100%
```
Meta: 100% (cada tripulante com espaço privado)

**Implementação no Projeto**:
```python
# src/utils/calculations.py
def calculate_layout_efficiency(zones, floor_area):
    """Calcula métricas de eficiência do layout"""
    usable_area = sum(zone['area'] for zone in zones.values())
    efficiency = (usable_area / floor_area) * 100
    return efficiency
```

---

### 10. Multi-functionality in Space

**Aplicação no Projeto**: Desafios de design e logística de habitação multi-funcional.

**Princípios de Multi-funcionalidade**:

#### A. Móveis Transformáveis
- Mesa que vira cama
- Estação de trabalho que vira área de exercício
- Armazenamento integrado em múltiplas superfícies

#### B. Espaços Compartilhados
- Área de jantar = Área de reunião = Área de lazer
- Reduz área necessária em 30-40%

#### C. Horários de Uso
- Cronograma de uso por turno
- Maximiza utilização de cada m²
- Reduz conflitos de acesso

**Implementação Futura**:
```python
# src/config/constants.py
MULTIFUNCTIONAL_ZONES = {
    "dining_meeting_recreation": {
        "functions": ["dining", "meetings", "recreation"],
        "area_per_person": 2.0,  # m² (ao invés de 3×2.0 = 6.0)
        "time_sharing": True
    },
    "work_communication": {
        "functions": ["workstation", "communication"],
        "area_per_person": 1.5,  # m²
        "time_sharing": False
    }
}
```

---

### 11. Food Production on the Moon and in Remote Areas

**Aplicação no Projeto**: Desafios, produção e consumo de alimentos no espaço.

**Requisitos de Produção de Alimentos**:

#### A. Área de Cultivo
- Hidroponia: **5-8 m²** por pessoa (vegetais)
- Aeroponia: **3-5 m²** por pessoa (mais eficiente)
- Altura necessária: **1.5-2.0m** (crescimento de plantas)

#### B. Recursos Necessários
- Água: **5-10 L/dia** (irrigação + consumo)
- Luz: **300-500 μmol/m²/s** (LEDs)
- Nutrientes: Sistema hidropônico fechado

#### C. Tipos de Cultivo
- Vegetais folhosos: 30-45 dias (alface, espinafre)
- Vegetais de raiz: 60-90 dias (batata, cenoura)
- Frutas: 90+ dias (tomate, morango)

#### D. Integração com ECLSS
- Produção de O₂ via fotossíntese
- Consumo de CO₂
- Reciclagem de água
- Processamento de resíduos orgânicos

**Zonas de Cultivo**:
```python
# Implementação futura
FOOD_PRODUCTION_ZONES = {
    "hydroponics": {
        "area_per_person": 6.0,     # m²
        "height": 2.0,               # metros
        "water_per_day": 8.0,        # litros
        "power_requirement": 200,    # W/m²
        "o2_production": 0.5,        # kg/dia/pessoa
        "food_production": 0.3       # kg/dia/pessoa (fresh produce)
    },
    "food_storage": {
        "volume_per_person_per_day": 0.002,  # m³ (2 litros)
        "min_storage_days": 90,               # 3 meses de backup
        "temperature": -20                     # °C (congelado)
    }
}
```

**Benefícios Psicológicos**:
- Conexão com a natureza (biofilia)
- Atividade terapêutica (jardinagem)
- Variedade na dieta
- Sensação de autossuficiência

---

## 🎯 Resumo de Aplicações

### Implementado Atualmente ✅

| Referência | Conceito | Localização |
|-----------|----------|-------------|
| NHV Definition | Volume mínimo 25 m³/pessoa | `constants.py` |
| M2M Architecture | Envelope de lançamento | `constants.py` |
| Internal Layout | Zonamento funcional | `constants.py` |
| Internal Layout | Zonas incompatíveis | `constants.py` |
| Layout Assessment | Alocação de áreas | `calculations.py` |
| Habitability Guidelines | Área mínima de piso | `constants.py` |

### Planejado para Implementação 🔄

| Referência | Conceito | Prioridade |
|-----------|----------|------------|
| Deep Space Guidelines | Dimensões ergonômicas | Alta |
| Layout Assessment Tool | Métricas de eficiência | Alta |
| Transit Habitat | Requisitos de trânsito vs superfície | Média |
| Inflatable Design | Tipo de estrutura (rígido/inflável) | Média |
| Multi-functionality | Espaços multi-funcionais | Média |
| Food Production | Zona de cultivo de alimentos | Baixa |
| MMPACT | Construção autônoma | Baixa |

---

## 📖 Como Usar Este Documento

### Para Desenvolvedores
1. **Consulte as referências** antes de implementar novas funcionalidades
2. **Cite a fonte** ao adicionar constantes ou validações
3. **Mantenha o código rastreável** à documentação NASA

### Para Contribuidores
1. **Adicione novas referências** seguindo o formato existente
2. **Inclua código de exemplo** sempre que possível
3. **Documente a aplicação prática** no projeto

### Para Usuários
1. **Entenda a base científica** das validações
2. **Confie nos padrões NASA** implementados
3. **Sugira melhorias** baseadas em novas publicações

---

## 🔗 Links Úteis

- [NASA Technical Reports Server (NTRS)](https://ntrs.nasa.gov/)
- [NASA Human Research Program](https://www.nasa.gov/hrp)
- [NASA Standards and Specifications](https://standards.nasa.gov/)
- [International Space Station Research](https://www.nasa.gov/mission_pages/station/research)

---

## 📅 Histórico de Revisões

| Data | Versão | Mudanças |
|------|--------|----------|
| 2025-10-04 | 1.0 | Criação inicial do documento de referências |

---

**Nota**: Este documento é vivo e deve ser atualizado conforme novas referências são incorporadas ao projeto ou novas publicações NASA se tornam disponíveis.
