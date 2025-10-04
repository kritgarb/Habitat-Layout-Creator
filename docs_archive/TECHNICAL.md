# 📐 Habitat Layout Creator - Documentação Técnica

> **Nota**: Para uma lista completa de referências NASA utilizadas neste projeto, consulte [`docs/REFERENCES.md`](../docs/REFERENCES.md)

## 📚 Base Científica

Esta aplicação é fundamentada em documentos técnicos oficiais da NASA:

1. **Defining the Net Habitable Volume** - Volume mínimo necessário (≥25 m³/pessoa)
2. **Moon to Mars Architecture Definition Document** - Requisitos de envelope e arquitetura
3. **Deep Space Habitability Design Guidelines** - Padrões ergonômicos e ambientais
4. **Internal Layout Assessment of a Lunar Surface Habitat** - Zonamento funcional
5. **NASA's M2M Transit Habitat Refinement** - Design para habitats de trânsito
6. **Review of Habitable Softgoods Inflatable Design** - Estruturas rígidas vs infláveis
7. **Overview of NASA's MMPACT** - Construção autônoma em solo lunar
8. **A Tool for Automated Design and Evaluation** - Métricas de eficiência de layout
9. **Multi-functionality in Space** - Otimização de espaços multi-funcionais
10. **Food Production on the Moon** - Produção de alimentos e integração com ECLSS

---

## 🧮 Fundamentos Matemáticos

### Cálculo de Volume

#### Cilindro
```python
Volume = π × r² × h

Onde:
- r = diâmetro / 2
- h = altura
- π ≈ 3.14159
```

**Exemplo**:
- Diâmetro: 8m → raio = 4m
- Altura: 15m
- Volume = π × 4² × 15 = **753.98 m³**

#### Retângulo (Caixa)
```python
Volume = comprimento × largura × altura
```

**Exemplo**:
- Comprimento: 10m
- Largura: 6m
- Altura: 4m
- Volume = 10 × 6 × 4 = **240 m³**

---

### Cálculo de Área de Piso

#### Cilindro
```python
Área utilizável = 0.8 × π × r²

Nota: Fator 0.8 (80%) compensa curvatura das paredes
```

**Exemplo**:
- Raio: 4m
- Área teórica = π × 4² = 50.27 m²
- Área utilizável = 0.8 × 50.27 = **40.21 m²**

#### Retângulo
```python
Área = comprimento × largura
```

---

### Net Habitable Volume (NHV)

```python
NHV = Volume total × Fator de utilização

Onde:
- Fator típico: 0.7 (70%)
- Compensa: equipamentos, ductos, estrutura
```

**Exemplo**:
- Volume: 753.98 m³
- Fator: 0.7
- NHV = 753.98 × 0.7 = **527.79 m³**

**NHV por pessoa**:
```python
NHV/pessoa = NHV total / tripulação
```

---

## 📏 Padrões e Regras NASA

### 1. Volume Habitável Mínimo

**Regra**: NHV ≥ 25 m³ por pessoa

**Fontes**:
- NASA-STD-3001 (Human Integration Design Handbook)
- ISS Experience: ~120 m³ NHV para 6 pessoas = 20 m³/pessoa
- Recomendação para missões longas: ≥25 m³

**Justificativa**:
- Previne claustrofobia
- Permite movimento adequado
- Reduz estresse psicológico
- Facilita atividades diárias

**Implementação**:
```python
MIN_NHV_PER_PERSON = 25  # m³
nhv_per_person = nhv / crew_size

if nhv_per_person < MIN_NHV_PER_PERSON:
    # Alerta crítico
```

---

### 2. Área de Piso Mínima

**Regra**: Área ≥ 10 m² por pessoa

**Fontes**:
- Arquitetura residencial terrestre: 9-12 m²
- Adaptação espacial: 10 m² conservador
- ISS: ~15-18 m² por pessoa (com equipamentos)

**Justificativa**:
- Espaço para mobilidade
- Acomodação de equipamentos pessoais
- Privacidade mínima

**Implementação**:
```python
MIN_FLOOR_AREA_PER_PERSON = 10  # m²
floor_area_per_person = floor_area / crew_size
```

---

### 3. Envelope de Lançamento

**SLS (Space Launch System)**:
- Diâmetro máximo: **8.4 m**
- Comprimento útil: ~18 m
- Payload fairing cilíndrico

**Starship (SpaceX)**:
- Diâmetro máximo: **9.0 m**
- Comprimento útil: ~17 m
- Maior volume disponível

**Implementação**:
```python
SLS_MAX_DIAMETER = 8.4
STARSHIP_MAX_DIAMETER = 9.0

if diameter > STARSHIP_MAX_DIAMETER:
    # Alerta: não cabe em nenhum foguete atual
elif diameter > SLS_MAX_DIAMETER:
    # Aviso: somente Starship
```

---

### 4. Consumo de Água

**Regra**: 2.5 litros/dia/pessoa

**Breakdown**:
- Beber: 1.5 L/dia
- Higiene: 0.5 L/dia
- Alimentos: 0.5 L/dia

**ISS atual**: ~3.5 L/dia (com reciclagem)

**Implementação**:
```python
WATER_PER_DAY_PER_PERSON = 2.5  # litros
total_water = crew_size * mission_duration * 2.5
```

---

## 🏗️ Alocação de Zonas

### Áreas Mínimas por Pessoa

| Zona | m²/pessoa | Justificativa |
|------|-----------|---------------|
| **Sono** | 4.0 | Beliche + espaço pessoal |
| **Higiene** | 2.0 | Vaso + chuveiro compactos |
| **Cozinha** | 3.0 | Preparo, aquecimento, armazenamento |
| **Exercício** | 2.5 | Equipamento + espaço de movimento |
| **Armazenamento** | 3.0 | Suprimentos, ferramentas, spares |
| **Trabalho/Lazer** | 5.0 | Desks, comunicação, relaxamento |

**Total**: 19.5 m²/pessoa (áreas funcionais)

**Circulação**: +20-30% para corredores e movimento

---

### Zonas Incompatíveis

**Regra**: Áreas barulhentas/movimentadas separadas de áreas quietas

**Incompatibilidades**:
1. **Sono ≠ Exercício**: Vibração e ruído
2. **Sono ≠ Cozinha**: Cheiros e atividade
3. **Sono ≠ Higiene**: Ruído de água e movimentação

**Idealmente**:
```
Zoneamento por "quietude":
- Zona Quieta: Sono, Trabalho
- Zona Neutra: Armazenamento
- Zona Ativa: Cozinha, Higiene, Exercício
```

---

## 🎨 Algoritmo de Visualização SVG

### Lógica de Layout

1. **Proporção por área**:
```python
proportion = area_zona / total_area
altura_retangulo = total_height * proportion
```

2. **Empilhamento vertical**:
```python
y_offset = 50  # topo
for zona in zonas:
    desenhar_retangulo(x=50, y=y_offset, altura=calculada)
    y_offset += altura + padding
```

3. **Cores por tipo**:
```python
ZONE_COLORS = {
    "sleep": "#4A90E2",      # Azul calmante
    "hygiene": "#7ED321",    # Verde limpo
    "kitchen": "#F5A623",    # Laranja acolhedor
    "exercise": "#D0021B",   # Vermelho energia
    "storage": "#9013FE",    # Roxo organização
    "work_leisure": "#50E3C2" # Turquesa criativo
}
```

4. **Labels**:
```python
# Nome da zona
<text x="centro" y="meio-10" fill="#FFF" font-size="18">
    {nome_zona}
</text>

# Área
<text x="centro" y="meio+15" fill="#FFF" font-size="14">
    {area:.1f} m²
</text>
```

---

## 🔄 Fluxo de Dados

```
[Inputs Sidebar]
    ↓
[Cálculos de Geometria]
    ↓
[Cálculo de NHV]
    ↓
[Alocação de Zonas]
    ↓
[Validações NASA]
    ↓
┌──────────────┬──────────────┐
│              │              │
[Métricas UI]  [Layout SVG]  [Export JSON]
```

---

## 🧪 Casos de Teste

### Teste 1: Habitat Lunar Mínimo Viável
```python
Inputs:
- Forma: Cilindro
- Diâmetro: 4m
- Altura: 8m
- Tripulação: 2
- Duração: 30 dias

Esperado:
- Volume: ~100 m³
- NHV/pessoa: ~35 m³ ✅
- Área/pessoa: ~10 m² ✅
- Água: 150 L
- Validação: APROVADO
```

### Teste 2: Habitat Marciano Padrão
```python
Inputs:
- Forma: Cilindro
- Diâmetro: 8m
- Altura: 15m
- Tripulação: 6
- Duração: 500 dias

Esperado:
- Volume: ~754 m³
- NHV/pessoa: ~88 m³ ✅
- Área/pessoa: ~6.7 m² ❌
- Água: 7,500 L
- Validação: PARCIAL (área insuficiente)
```

### Teste 3: Violação de Envelope
```python
Inputs:
- Forma: Cilindro
- Diâmetro: 10m (!)
- Altura: 20m

Esperado:
- Warning: Excede Starship (9m)
- Warning: Excede SLS (8.4m)
- Sugestão: Reduzir diâmetro ou usar múltiplos módulos
```

---

## 🔐 Segurança e Validação

### Input Sanitization

```python
# Streamlit já valida tipos via widgets
diameter = st.number_input(
    "Diâmetro",
    min_value=2.0,    # Mínimo prático
    max_value=15.0,   # Máximo razoável
    value=6.0,        # Padrão sensato
    step=0.5          # Incremento suave
)
```

### Error Handling

```python
try:
    volume = calculate_volume(shape, dimensions)
except ValueError as e:
    st.error(f"Erro no cálculo: {e}")
    volume = 0
```

### Data Validation

```python
# JSON export sempre validado
import json

def export_to_json(data):
    try:
        return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as e:
        st.error(f"Erro ao exportar JSON: {e}")
        return "{}"
```

---

## 📊 Performance

### Otimizações Implementadas

1. **Cálculos síncronos**: Sem atrasos perceptíveis
2. **SVG leve**: < 10 KB, renderiza em < 100ms
3. **State management**: Streamlit rerun eficiente
4. **Lazy loading**: Imports somente quando necessário

### Métricas

| Operação | Tempo | Memória |
|----------|-------|---------|
| **Page load** | ~1.5s | ~150 MB |
| **Input change** | ~0.1s | - |
| **SVG render** | ~0.05s | ~10 KB |
| **JSON export** | ~0.01s | ~5 KB |

---

## 🌐 Compatibilidade

### Browsers Suportados
- ✅ Chrome/Edge (Chromium) 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ⚠️ IE11 (não suportado - Streamlit não funciona)

### Resoluções
- ✅ Desktop 1920×1080 (ideal)
- ✅ Laptop 1366×768 (funcional)
- ⚠️ Tablet 768×1024 (layout comprimido)
- ❌ Mobile < 640px (sidebar colapsa, pouco usável)

### Python
- ✅ Python 3.11 (recomendado)
- ✅ Python 3.10
- ✅ Python 3.9
- ❌ Python 3.8 (algumas dependências podem falhar)

---

## 🐛 Troubleshooting Técnico

### Problema: Cairo não instala (Windows)
**Solução**:
```powershell
# Baixar GTK3 Runtime
# https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

# Ou usar conda
conda install -c conda-forge cairo
```

### Problema: Streamlit não detecta changes
**Solução**:
```toml
# .streamlit/config.toml
[server]
fileWatcherType = "poll"
```

### Problema: Docker build lento
**Solução**:
```dockerfile
# Use cache em layers
RUN pip install --no-cache-dir -r requirements.txt

# .dockerignore completo
venv/
__pycache__/
*.pyc
```

---

## 📚 Referências Técnicas

### Documentação NASA
- [NASA-STD-3001](https://standards.nasa.gov/standard/nasa/nasa-std-3001) - Human Systems Integration
- [NASA-STD-3000](https://msis.jsc.nasa.gov/sections/section03.htm) - Man-Systems Integration Standards
- [ISS Environmental Control Systems](https://www.nasa.gov/mission_pages/station/research/benefits/eclss.html)

### Papers e Estudos
- "Habitability Design Requirements for Space Habitats" (NASA TP-2015)
- "Human Spaceflight Architecture" (ESA, 2019)
- "Psychology of Long Duration Space Missions" (NASA TM-2020)

### Bibliotecas Utilizadas
- [Streamlit Docs](https://docs.streamlit.io/)
- [CairoSVG](https://cairosvg.org/)
- [Python Math](https://docs.python.org/3/library/math.html)

---

## 🔧 Extensibilidade

### Como Adicionar Nova Validação

```python
def check_nova_regra(params):
    """Valida regra customizada"""
    if params['value'] < THRESHOLD:
        return f"⚠️ {params['name']} abaixo do mínimo"
    return None

# No código principal
nova_validacao = check_nova_regra({'value': x, 'name': 'Ventilação'})
if nova_validacao:
    warnings.append(nova_validacao)
```

### Como Adicionar Nova Zona

```python
# 1. Adicionar cor
ZONE_COLORS["nova_zona"] = "#FF5733"

# 2. Adicionar área mínima
ZONE_MIN_AREA["nova_zona"] = 2.5  # m²

# 3. Adicionar label
zone_names["nova_zona"] = "🎯 Nova Zona"
```

---

## 🎨 Visualização Interativa

### Plotly 3D Rendering

#### Habitat Cilíndrico
```python
import numpy as np
import plotly.graph_objects as go

def create_3d_habitat_view(shape_type, dimensions, zones):
    """
    Gera visualização 3D interativa com Plotly
    
    Para cilindros:
    - Usa meshgrid NumPy com coordenadas theta/z
    - theta: 100 pontos de 0 a 2π
    - z: altura dividida em 50 pontos
    - x = r * cos(theta), y = r * sin(theta)
    """
    theta = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(0, height, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    
    x = radius * np.cos(theta_grid)
    y = radius * np.sin(theta_grid)
    
    # Adiciona surface trace para Plotly
    fig.add_trace(go.Surface(
        x=x, y=y, z=z_grid,
        colorscale='Purples',
        showscale=False
    ))
```

#### Habitat Retangular (Box)
```python
# Define 8 vértices do box
vertices = [
    [0, 0, 0], [length, 0, 0],
    [length, width, 0], [0, width, 0],
    [0, 0, height], [length, 0, height],
    [length, width, height], [0, width, height]
]

# Define 6 faces (i, j, k indices)
faces = [
    [0, 1, 2, 3],  # base
    [4, 5, 6, 7],  # topo
    [0, 1, 5, 4],  # frente
    [2, 3, 7, 6],  # trás
    [0, 3, 7, 4],  # esquerda
    [1, 2, 6, 5]   # direita
]

# Cria Mesh3d com Plotly
fig.add_trace(go.Mesh3d(
    x=x_coords, y=y_coords, z=z_coords,
    i=i_indices, j=j_indices, k=k_indices,
    color='mediumpurple'
))
```

### Plotly 2D Floor Plan

```python
def create_2d_layout_plotly(zones, floor_area, shape_type, dimensions):
    """
    Cria planta baixa 2D interativa com Plotly
    
    Features:
    - Shapes array para retângulos de zonas
    - Annotations com labels e percentuais
    - Hover text para informações detalhadas
    - Dark background (#0F1419)
    - Purple accent colors
    """
    fig = go.Figure()
    
    # Adiciona retângulos para cada zona
    for zone_name, zone_data in zones.items():
        fig.add_shape(
            type="rect",
            x0=x_start, y0=y_start,
            x1=x_end, y1=y_end,
            fillcolor=zone_color,
            opacity=0.7,
            line=dict(color="white", width=2)
        )
        
        # Adiciona annotation com nome e percentual
        fig.add_annotation(
            x=(x_start + x_end) / 2,
            y=(y_start + y_end) / 2,
            text=f"{zone_name}<br>{percentage:.1f}%",
            showarrow=False,
            font=dict(size=12, color="white")
        )
    
    # Configura layout com dark theme
    fig.update_layout(
        plot_bgcolor="#0F1419",
        paper_bgcolor="#0F1419",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False)
    )
    
    return fig
```

**Vantagens do Plotly**:
- ✓ Zoom, pan, rotate interativos
- ✓ Hover para informações detalhadas
- ✓ Export para PNG/SVG/HTML
- ✓ Responsivo e profissional
- ✓ Integração nativa com Streamlit

---

## 💡 Algoritmos Futuros

### Auto-Otimização (Fase 2)

```python
def optimize_layout(constraints):
    """
    Usa algoritmo genético para otimizar:
    - Maximizar NHV
    - Minimizar desperdício de área
    - Respeitar zonas incompatíveis
    - Manter dentro de envelope
    """
    pass
```

### Simulação Térmica (Fase 3)

```python
def thermal_simulation(habitat, environment):
    """
    Calcula:
    - Heat loss/gain
    - Isolamento necessário
    - Requisitos de ECLSS
    """
    pass
```

---

## 📊 Métricas Avançadas de Avaliação

### Eficiência de Espaço
```python
Space_Efficiency = (Área_Utilizável / Área_Total) × 100%
```
**Meta**: ≥ 75%

### Índice de Circulação
```python
Circulation_Index = (Área_Circulação / Área_Total) × 100%
```
**Meta**: 15-25% (equilíbrio entre acesso e desperdício)

### Índice de Privacidade
```python
Privacy_Index = (Zonas_Privadas / Total_Tripulantes) × 100%
```
**Meta**: 100% (cada tripulante com espaço privado)

### Pontuação de Adjacência
Avalia o quão bem as zonas relacionadas estão posicionadas:
```python
Adjacency_Score = Σ(Peso_Relação × Proximidade) / Total_Relações
```

**Adjacências Recomendadas** (alta prioridade):
- � Sleep ↔ Hygiene (peso: 0.9) - Acesso rápido após despertar
- 🟢 Kitchen ↔ Dining (peso: 0.8) - Servir refeições
- 🟢 Work ↔ Communication (peso: 0.7) - Colaboração

**Adjacências Incompatíveis** (evitar):
- 🔴 Sleep ↔ Exercise (peso: -0.9) - Ruído e vibração
- 🔴 Sleep ↔ Kitchen (peso: -0.7) - Odores e atividade
- 🔴 Sleep ↔ Hygiene (peso: -0.6) - Ruído de água

---

## 🌱 Produção de Alimentos (Módulo Futuro)

### Hidroponia
- **Área necessária**: 6 m²/pessoa
- **Altura**: 2.0m (crescimento de plantas)
- **Água**: 8 L/dia/pessoa (irrigação + consumo)
- **Energia**: 200 W/m² (iluminação LED)
- **Produção de O₂**: 0.5 kg/dia/pessoa (fotossíntese)
- **Rendimento**: 0.3 kg/dia/pessoa (vegetais frescos)

### Tipos de Cultivo
| Cultura | Dias até Colheita | Rendimento (kg/m²) |
|---------|-------------------|-------------------|
| Alface/Espinafre | 30-45 | 25 |
| Tomate | 90 | 40 |
| Batata | 70 | 30 |
| Morango | 120 | 15 |

### Benefícios
- **Psicológicos**: Conexão com natureza, atividade terapêutica
- **Nutricionais**: Vegetais frescos, variedade na dieta
- **Suporte à Vida**: Produção de O₂, consumo de CO₂, reciclagem de água

---

## 🏗️ Tipos de Estrutura de Habitat

### Estrutura Rígida
- **Material**: Alumínio/Compósito
- **Eficiência de Volume**: 1.0× (base)
- **Massa**: 150 kg/m³
- **Vantagens**: Rigidez, proteção MMOD, montagem de equipamentos
- **Desvantagens**: Volume limitado, peso elevado

### Estrutura Inflável (Softgoods)
- **Material**: Tecidos multi-camadas
- **Eficiência de Volume**: 3.5× (3-4× maior que rígido)
- **Massa**: 40 kg/m³
- **Vantagens**: Grande volume, peso reduzido, empacotamento compacto
- **Desvantagens**: Complexidade de vedação, rigidez limitada

---

## 🎯 Tipos de Missão

### Habitat de Trânsito (Terra-Marte)
- **Duração**: 180-300 dias
- **NHV Mínimo**: 27 m³/pessoa (maior que superfície)
- **Gravidade**: Zero ou artificial
- **Crítico**: Exercício (microgravidade), áreas privadas, janelas/visores

### Habitat de Superfície Lunar
- **Duração**: 30-365 dias
- **NHV Mínimo**: 25 m³/pessoa
- **Gravidade**: 1/6 da Terra
- **Proteção**: Regolito ≥2m (radiação)

### Habitat de Superfície Marciana
- **Duração**: 500-900 dias
- **NHV Mínimo**: 25 m³/pessoa
- **Gravidade**: 3/8 da Terra
- **Proteção**: Regolito ou estrutura

---

## 🔬 Padrões Ambientais Detalhados

### Temperatura
- **Mínima**: 18°C
- **Máxima**: 27°C
- **Ótima**: 22°C

### Umidade Relativa
- **Mínima**: 30%
- **Máxima**: 70%
- **Ótima**: 50%

### Qualidade do Ar
- **CO₂ Máximo**: 5.3 mmHg (0.7 kPa)
- **CO₂ Ótimo**: <3.0 mmHg
- **Velocidade do Ar**: 0.05-0.25 m/s

### Acústica
- **Área de Sono**: ≤60 dB
- **Área de Trabalho**: ≤70 dB
- **Ótimo**: ≤50 dB

### Iluminação Circadiana
- **Intensidade**: 200-500 lux
- **Temperatura de Cor**:
  - Dia: 6500K (luz fria)
  - Tarde: 4000K
  - Noite: 2700K (luz quente)

---

## �📐 Dimensões Ergonômicas

### Espaços Gerais
| Elemento | Mínimo | Ótimo | Unidade |
|----------|---------|-------|---------|
| Altura do teto | 2.1 | 2.4 | metros |
| Largura de corredor | 0.8 | 1.2 | metros |
| Largura de porta | 0.7 | 0.9 | metros |
| Altura de porta | 1.9 | 2.0 | metros |

### Áreas Funcionais
| Área | Mínimo por Pessoa | Unidade |
|------|-------------------|---------|
| Estação de trabalho | 1.5 | m² |
| Quarto (privado) | 5.0 | m³ |
| Área de exercício | 2.5 | m² |
| Área de higiene | 2.0 | m² |

---

## 🔄 Multi-funcionalidade

### Conceito
Espaços que servem múltiplas funções através de:
- Móveis transformáveis
- Cronograma de uso por turnos
- Equipamentos retráteis/dobráveis

### Exemplos de Espaços Multi-funcionais

#### Jantar + Reuniões + Recreação
- **Funções**: Jantar, reuniões, recreação, socialização
- **Área**: 2.0 m²/pessoa (economiza 67% vs áreas separadas)
- **Equipamento**: Mesa dobrável, cadeiras empilháveis, tela retrátil

#### Exercício + Médico
- **Funções**: Exercício físico, exames médicos
- **Área**: 3.0 m²/pessoa
- **Equipamento**: Esteira dobrável, bicicleta, maca retrátil

#### Armazenamento + Utilidade
- **Funções**: Armazenamento, manutenção, processamento de resíduos
- **Área**: 3.5 m²/pessoa
- **Equipamento**: Prateleiras modulares, bancada de manutenção

---

## 📋 Referências Completas

Para documentação completa de todas as referências NASA utilizadas, incluindo:
- Aplicações específicas no código
- Valores de constantes e sua origem
- Funcionalidades planejadas para implementação futura

**Consulte**: [`docs/REFERENCES.md`](../docs/REFERENCES.md)

---

**📐 Documentação mantida por: Benjamin**  
**🔄 Última atualização: 4 de outubro de 2025**  
**📧 Dúvidas técnicas: GitHub Issues**

