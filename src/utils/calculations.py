"""
Funções de cálculo para geometria e métricas de habitats espaciais
"""
import math


def calculate_cylinder_volume(diameter: float, height: float) -> float:
    """
    Calcula o volume de um cilindro.
    
    Args:
        diameter: Diâmetro do cilindro (metros)
        height: Altura do cilindro (metros)
    
    Returns:
        Volume em metros cúbicos
    """
    radius = diameter / 2
    return math.pi * radius ** 2 * height


def calculate_cylinder_floor_area(diameter: float, height: float) -> float:
    """
    Calcula a área de piso utilizável de um cilindro.
    Usa fator de 0.8 para áreas utilizáveis (desconta curvatura).
    
    Args:
        diameter: Diâmetro do cilindro (metros)
        height: Altura do cilindro (metros)
    
    Returns:
        Área de piso em metros quadrados
    """
    radius = diameter / 2
    return 0.8 * math.pi * radius ** 2


def calculate_box_volume(length: float, width: float, height: float) -> float:
    """
    Calcula o volume de uma caixa retangular.
    
    Args:
        length: Comprimento (metros)
        width: Largura (metros)
        height: Altura (metros)
    
    Returns:
        Volume em metros cúbicos
    """
    return length * width * height


def calculate_box_floor_area(length: float, width: float) -> float:
    """
    Calcula a área de piso de uma caixa retangular.
    
    Args:
        length: Comprimento (metros)
        width: Largura (metros)
    
    Returns:
        Área de piso em metros quadrados
    """
    return length * width


def calculate_nhv(total_volume: float, usable_factor: float = 0.7) -> float:
    """
    Calcula o Net Habitable Volume (NHV).
    
    Args:
        total_volume: Volume total pressurizado (m³)
        usable_factor: Fator de volume utilizável (0.5-0.9)
    
    Returns:
        NHV em metros cúbicos
    """
    return total_volume * usable_factor


def allocate_zones(floor_area: float, crew_size: int, zone_min_area: dict) -> dict:
    """
    Aloca área de piso para cada zona funcional baseada no tamanho da tripulação.
    
    Args:
        floor_area: Área total de piso disponível (m²)
        crew_size: Número de tripulantes
        zone_min_area: Dicionário com área mínima por pessoa para cada zona
    
    Returns:
        Dicionário com área alocada para cada zona
    """
    zones = {}
    for zone, min_area in zone_min_area.items():
        zones[zone] = min_area * crew_size
    return zones
