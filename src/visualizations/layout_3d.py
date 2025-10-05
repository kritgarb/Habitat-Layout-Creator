"""
Interactive 3D visualizations with Plotly and NumPy
"""
import plotly.graph_objects as go
import numpy as np


def create_3d_habitat_view(shape_type: str, dimensions: dict, zones: dict,
                           zone_colors: dict, zone_names: dict) -> go.Figure:
    """
    Creates interactive 3D visualization of the habitat using Plotly.
    
    Args:
        shape_type: Shape type ("Cylinder" or "Rectangular")
        dimensions: Dictionary with habitat dimensions
        zones: Dictionary with areas of each zone
        zone_colors: Dictionary with zone colors
        zone_names: Dictionary with zone names
    
    Returns:
        Plotly figure with the habitat in 3D
    """
    fig = go.Figure()
    
    if shape_type == "Cylinder":
        fig = _create_cylinder_3d(dimensions, zones, zone_colors, zone_names, fig)
    else:  # Rectangular
        fig = _create_box_3d(dimensions, zones, zone_colors, zone_names, fig)
    
    # Common layout configuration
    fig.update_layout(
        scene=dict(
            xaxis=dict(showgrid=True, gridcolor='#2d3748', showbackground=True, backgroundcolor='#0F1419'),
            yaxis=dict(showgrid=True, gridcolor='#2d3748', showbackground=True, backgroundcolor='#0F1419'),
            zaxis=dict(showgrid=True, gridcolor='#2d3748', showbackground=True, backgroundcolor='#0F1419'),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
        ),
        paper_bgcolor='rgba(15, 20, 25, 0)',
        plot_bgcolor='rgba(15, 20, 25, 0)',
        height=600,
        margin=dict(l=0, r=0, t=80, b=0),
        title=dict(
            text=f"<b>HABITAT 3D VIEW</b> · {shape_type} Configuration · {len(zones)} Zones",
            font=dict(size=18, color="#E2E8F0", family="Arial Black"),
            x=0.5,
            xanchor='center'
        ),
        legend=dict(
            bgcolor='rgba(11, 15, 26, 0.9)',
            bordercolor='#A68CFF',
            borderwidth=2,
            font=dict(color='#E2E8F0', size=11),
            orientation='v',
            x=1.02,
            y=1,
            xanchor='left',
            yanchor='top',
            title=dict(text="<b>Zones</b>", font=dict(size=13, color='#A68CFF'))
        ),
        showlegend=True
    )
    
    return fig


def _create_cylinder_3d(dimensions: dict, zones: dict, zone_colors: dict, 
                        zone_names: dict, fig: go.Figure) -> go.Figure:
    """
    Cria visualização 3D de um habitat cilíndrico.
    
    Args:
        dimensions: Dicionário com diameter e height
        zones: Dicionário com áreas de cada zona
        zone_colors: Cores das zonas
        zone_names: Nomes das zonas
        fig: Figura Plotly para adicionar traces
    
    Returns:
        Figura Plotly atualizada
    """
    diameter = dimensions["diameter"]
    height = dimensions["height"]
    
    # Criar cilindro com meshgrid NumPy
    theta = np.linspace(0, 2*np.pi, 50)
    z = np.linspace(0, height, 20)
    theta_grid, z_grid = np.meshgrid(theta, z)
    
    radius = diameter / 2
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)
    
    # Adiciona superfície do cilindro
    fig.add_trace(go.Surface(
        x=x_grid, y=y_grid, z=z_grid,
        colorscale=[[0, '#667eea'], [1, '#764ba2']],
        opacity=0.7,
        showscale=False,
        name="Habitat Structure"
    ))
    
    # Adicionar divisões para zonas
    total_zone_area = sum(zones.values())
    z_offset = 0
    
    for zone, area in zones.items():
        proportion = area / total_zone_area
        zone_height = height * proportion
        
        # Plano divisor circular para cada zona
        z_plane = z_offset + zone_height
        x_plane = radius * np.cos(theta)
        y_plane = radius * np.sin(theta)
        
        fig.add_trace(go.Scatter3d(
            x=x_plane, y=y_plane, z=[z_plane]*len(theta),
            mode='lines',
            line=dict(color=zone_colors[zone], width=5),
            name=zone_names[zone],
            hovertext=f"{zone_names[zone]}<br>{area:.1f} m²",
            showlegend=True
        ))
        
        z_offset += zone_height
    
    return fig


def _create_box_3d(dimensions: dict, zones: dict, zone_colors: dict,
                   zone_names: dict, fig: go.Figure) -> go.Figure:
    """
    Cria visualização 3D de um habitat retangular (box).
    
    Args:
        dimensions: Dicionário com length, width, height
        zones: Dicionário com áreas de cada zona
        zone_colors: Cores das zonas
        zone_names: Nomes das zonas
        fig: Figura Plotly para adicionar traces
    
    Returns:
        Figura Plotly atualizada
    """
    length = dimensions["length"]
    width = dimensions["width"]
    height = dimensions["height"]
    
    # Criar caixa retangular com 8 vértices
    x = [0, length, length, 0, 0, length, length, 0]
    y = [0, 0, width, width, 0, 0, width, width]
    z = [0, 0, 0, 0, height, height, height, height]
    
    # Definir faces da caixa (índices i, j, k)
    i = [0, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 5]
    j = [1, 2, 3, 4, 5, 6, 5, 2, 0, 1, 6, 6]
    k = [2, 3, 7, 7, 6, 7, 1, 1, 5, 5, 7, 2]
    
    # Adiciona mesh 3D da caixa
    fig.add_trace(go.Mesh3d(
        x=x, y=y, z=z,
        i=i, j=j, k=k,
        colorscale=[[0, '#667eea'], [1, '#764ba2']],
        opacity=0.7,
        showscale=False,
        name="Habitat Structure"
    ))
    
    # Adicionar divisões horizontais para zonas
    total_zone_area = sum(zones.values())
    z_offset = 0
    
    for zone, area in zones.items():
        proportion = area / total_zone_area
        zone_height = height * proportion
        
        # Plano divisor horizontal para cada zona
        z_plane = z_offset + zone_height
        
        # Criar retângulo de divisão
        x_plane = [0, length, length, 0, 0]
        y_plane = [0, 0, width, width, 0]
        z_plane_list = [z_plane] * 5
        
        fig.add_trace(go.Scatter3d(
            x=x_plane, 
            y=y_plane, 
            z=z_plane_list,
            mode='lines',
            line=dict(color=zone_colors[zone], width=5),
            name=zone_names[zone],
            hovertext=f"{zone_names[zone]}<br>{area:.1f} m²",
            showlegend=True
        ))
        
        z_offset += zone_height
    
    return fig
