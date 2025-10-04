# 📝 Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [1.1.0] - 2025-10-04

### 🎉 Adicionado

#### Documentação
- **`docs/REFERENCES.md`**: Documentação completa de 11 referências técnicas NASA
  - Conceitos implementados de cada documento
  - Localização no código com exemplos
  - Funcionalidades planejadas vs implementadas
  - Tabelas de comparação e status
  - Links para NASA NTRS e recursos oficiais
  
- **`docs/USAGE_GUIDE.md`**: Guia completo de uso
  - Exemplos de código para todas as funcionalidades
  - 3 casos de uso completos
  - Dashboard de métricas avançadas
  - Roadmap de funcionalidades futuras
  
- **`docs/IMPLEMENTATION_SUMMARY.md`**: Resumo técnico da implementação
  - Estatísticas detalhadas (~2,150 linhas adicionadas)
  - Lista de arquivos criados/modificados
  - Checklist de qualidade
  - Rastreabilidade código ↔ fonte NASA
  
- **`docs/QUICK_INDEX.md`**: Índice rápido de referência
  - Busca por conceito NASA
  - Busca por arquivo
  - Busca por funcionalidade
  - Busca por referência

#### Código - Constantes (`src/config/constants.py`)
- `MIN_NHV_PER_PERSON_TRANSIT`: 27 m³/pessoa para habitats de trânsito
- `MIN_PRIVACY_VOLUME_PER_PERSON`: 5.0 m³ de volume privado
- `WATER_HYGIENE_PER_DAY_PER_PERSON`: 23.0 L/dia (reciclável)
- `OXYGEN_PER_DAY_PER_PERSON`: 0.84 kg/dia
- `FOOD_PER_DAY_PER_PERSON`: 0.62 kg/dia
- `POWER_PER_PERSON`: 2000 W
- `SLS_MAX_HEIGHT`: 27.4 metros
- `STARSHIP_MAX_HEIGHT`: 17.24 metros
- Dimensões ergonômicas completas:
  - `MIN_CEILING_HEIGHT`: 2.1m
  - `MIN_CORRIDOR_WIDTH`: 0.8m
  - `MIN_DOOR_WIDTH`: 0.7m
  - `MIN_DOOR_HEIGHT`: 1.9m
  - `MIN_WORKSTATION_AREA`: 1.5 m²
- Padrões ambientais completos:
  - Temperatura: 18-27°C
  - Umidade: 30-70%
  - CO₂ máximo: 5.3 mmHg
  - Ruído: 60 dB (sleep), 70 dB (work)
- Iluminação circadiana:
  - Intensidade: 200-500 lux
  - Temperatura de cor: 2700-6500K
- Produção de alimentos:
  - `FOOD_PRODUCTION_AREA_PER_PERSON`: 6.0 m²
  - `FOOD_PRODUCTION_HEIGHT`: 2.0m
  - `FOOD_O2_PRODUCTION`: 0.5 kg/dia/pessoa
- `MISSION_TYPES`: Dicionário completo com 3 tipos de missão
  - Transit (Terra-Marte)
  - Lunar Surface
  - Mars Surface
- `HABITAT_TYPES`: Dicionário com 2 tipos de estrutura
  - Rigid (150 kg/m³, eficiência 1.0×)
  - Inflatable (40 kg/m³, eficiência 3.5×)

#### Código - Design Guidelines (`src/config/design_guidelines.py`) ⭐ NOVO
- Classe `LayoutMetrics` com 4 métodos:
  - `calculate_space_efficiency()`: Eficiência de espaço (target ≥75%)
  - `calculate_circulation_index()`: Índice de circulação (target 15-25%)
  - `calculate_privacy_index()`: Índice de privacidade (target 100%)
  - `evaluate_layout_quality()`: Avaliação geral do layout
- Dicionários de padrões:
  - `HABITABILITY_DIMENSIONS`: Dimensões ergonômicas detalhadas
  - `ENVIRONMENTAL_STANDARDS`: Padrões ambientais completos
  - `MULTIFUNCTIONAL_SPACES`: 4 tipos de espaços multi-funcionais
  - `RECOMMENDED_ADJACENCIES`: Adjacências recomendadas e incompatíveis
  - `FOOD_PRODUCTION_CONFIG`: Configuração de hidroponia e aeroponia
  - `DESIGN_VALIDATION_RULES`: Regras críticas, recomendadas e opcionais
- Funções de validação:
  - `validate_habitability_standards()`: Valida dimensões e ambiente
  - `calculate_adjacency_score()`: Pontuação de adjacência (0-100)
  - `are_zones_adjacent()`: Verifica adjacência de zonas

#### Código - Validadores (`src/utils/validators.py`)
- `validate_dimensions()`: Valida dimensões ergonômicas (NOVA)
  - Altura do teto (≥2.1m) - CRÍTICO
  - Largura de corredor (≥0.8m)
  - Dimensões de porta (≥0.7m × 1.9m)
- `validate_environmental_conditions()`: Valida condições ambientais (NOVA)
  - Temperatura (18-27°C)
  - Umidade (30-70%)
  - CO₂ (<5.3 mmHg) - CRÍTICO
  - Ruído (60/70 dB dependendo da zona)
- `validate_zone_incompatibilities()`: Verifica zonas incompatíveis (NOVA)
- `calculate_layout_efficiency()`: Calcula métricas de eficiência (NOVA)
  - Space efficiency (target ≥75%)
  - Circulation index (target 15-25%)
- `validate_privacy_requirements()`: Valida privacidade (NOVA)
  - Verifica quartos privados por tripulante

### ✏️ Modificado

#### `README.md`
- Adicionada seção "Scientific Foundation" no topo
- Lista de 10 referências técnicas NASA
- Link para documentação completa de referências

#### `docs_archive/TECHNICAL.md`
- Adicionada seção "Base Científica" com lista de documentos
- Seção "Métricas Avançadas de Avaliação":
  - Eficiência de Espaço
  - Índice de Circulação
  - Índice de Privacidade
  - Pontuação de Adjacência
- Seção "Produção de Alimentos":
  - Hidroponia vs Aeroponia
  - Tabela de culturas e rendimentos
  - Benefícios psicológicos
- Seção "Tipos de Estrutura de Habitat"
- Seção "Tipos de Missão"
- Seção "Padrões Ambientais Detalhados"
- Seção "Dimensões Ergonômicas" (tabelas)
- Seção "Multi-funcionalidade"
- Link para `docs/REFERENCES.md`

#### `src/utils/validators.py`
- `validate_nasa_standards()`: Expandida
  - Novo parâmetro `mission_type`
  - Ajusta NHV mínimo para habitats de trânsito (27 m³)
  - Emojis para melhor visualização (⚠️, 🔴, ✅)
  - Mensagens mais descritivas

#### `src/config/constants.py`
- Adicionado docstring com lista de referências NASA
- Organizado em seções com comentários de referência
- +80 linhas de constantes novas

### 📚 Referências NASA Implementadas

1. **Defining the Net Habitable Volume for Long Duration Exploration Missions**
   - Volume mínimo: 25 m³/pessoa (superfície), 27 m³/pessoa (trânsito)
   
2. **Moon to Mars Architecture Definition Document**
   - Envelope de lançamento: SLS (8.4m × 27.4m), Starship (9.0m × 17.24m)
   - Tipos de missão: Trânsito, Lunar, Marciana
   
3. **Habitats and Surface Construction Technology and Development Roadmap**
   - Recursos de suporte à vida: Água, O₂, Comida, Energia
   - Zonas funcionais: 6 tipos com áreas mínimas
   
4. **Review of Habitable Softgoods Inflatable Design**
   - Tipos de estrutura: Rígida vs Inflável
   - Eficiência de volume e massa
   
5. **Overview of NASA's MMPACT**
   - Documentado para implementação futura
   
6. **Internal Layout Assessment of a Lunar Surface Habitat**
   - Zonamento funcional
   - Zonas incompatíveis
   - Adjacências recomendadas
   
7. **NASA's M2M Transit Habitat Refinement Point of Departure Design**
   - Requisitos de habitats de trânsito
   - Volume privado mínimo
   - Validação de privacidade
   
8. **Deep Space Habitability Design Guidelines (NASA NextSTEP Phase 2)**
   - Dimensões ergonômicas completas
   - Padrões ambientais (temperatura, umidade, CO₂, ruído)
   - Iluminação circadiana
   
9. **A Tool for Automated Design and Evaluation of Habitat Interior Layouts**
   - Métricas de eficiência de layout
   - Índices de circulação e privacidade
   - Pontuação de adjacência
   
10. **Multi-functionality in Space**
    - Conceitos de espaços multi-funcionais
    - Templates de zonas combinadas
    
11. **Food Production on the Moon and in Remote Areas**
    - Requisitos de hidroponia e aeroponia
    - Produção de O₂ via fotossíntese
    - Benefícios psicológicos e nutricionais

### 📊 Estatísticas

- **Arquivos Criados**: 4
  - `docs/REFERENCES.md` (720 linhas)
  - `docs/USAGE_GUIDE.md` (400 linhas)
  - `docs/IMPLEMENTATION_SUMMARY.md` (430 linhas)
  - `docs/QUICK_INDEX.md` (280 linhas)
  - `src/config/design_guidelines.py` (420 linhas)
  
- **Arquivos Modificados**: 4
  - `src/config/constants.py` (+80 linhas)
  - `src/utils/validators.py` (+180 linhas)
  - `docs_archive/TECHNICAL.md` (+250 linhas)
  - `README.md` (+20 linhas)
  
- **Total**: ~2,780 linhas de código e documentação adicionadas

---

## [1.0.0] - 2025-10-03

### 🎉 Lançamento Inicial

#### Funcionalidades Principais
- Design de habitats cilíndricos e retangulares
- Cálculo automático de volume, NHV e área de piso
- Alocação de zonas funcionais (6 tipos)
- Validação de padrões NASA (NHV ≥ 25 m³/pessoa)
- Verificação de envelope de lançamento (SLS/Starship)
- Visualização 3D interativa (Plotly)
- Visualização 2D de planta baixa
- Exportação para JSON
- Interface Streamlit moderna (dark theme, purple gradient)

#### Estrutura Inicial
- Arquitetura modular organizada
- Separação de conceitos (MVC-like)
- Documentação técnica completa
- Docker/Docker Compose configurado
- Testes básicos

#### Padrões NASA Implementados
- NHV mínimo: 25 m³/pessoa
- Área de piso mínima: 10 m²/pessoa
- Zonas funcionais básicas
- Envelope de lançamento (SLS, Starship)

---

## Tipos de Mudanças

- **🎉 Adicionado**: Para novas funcionalidades
- **✏️ Modificado**: Para mudanças em funcionalidades existentes
- **🗑️ Removido**: Para funcionalidades removidas
- **🐛 Corrigido**: Para correções de bugs
- **🔒 Segurança**: Para vulnerabilidades corrigidas
- **📚 Documentação**: Para mudanças apenas na documentação
- **⚡ Performance**: Para melhorias de performance

---

## [Não Lançado]

### 🔄 Em Planejamento (Alta Prioridade)
- UI para seleção de tipo de missão
- Dashboard de métricas avançadas na interface
- Validação automática de dimensões ergonômicas na UI
- Visualização de adjacências incompatíveis

### 🔄 Em Planejamento (Média Prioridade)
- Seleção de tipo de estrutura (rígida/inflável) na UI
- Cálculo de massa estrutural
- Templates de espaços multi-funcionais
- Zona de produção de alimentos (interface)

### 🔄 Em Planejamento (Baixa Prioridade)
- Construção autônoma (MMPACT)
- Simulação térmica
- Auto-otimização de layout com algoritmo genético

---

**Formato de versão**: MAJOR.MINOR.PATCH
- **MAJOR**: Mudanças incompatíveis na API
- **MINOR**: Novas funcionalidades compatíveis
- **PATCH**: Correções de bugs compatíveis
