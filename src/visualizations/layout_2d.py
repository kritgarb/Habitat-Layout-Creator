"""
Visualizações 2D interativas com Plotly
"""
import plotly.graph_objects as go


def create_2d_layout_plotly(zones: dict, floor_area: float, shape_type: str, 
                            dimensions: dict, zone_colors: dict, zone_names: dict) -> go.Figure:
    """
    Cria visualização 2D interativa do layout do habitat usando Plotly.
    
    Args:
        zones: Dicionário com áreas de cada zona
        floor_area: Área total de piso (m²)
        shape_type: Tipo de forma ("Cylinder" ou "Rectangular")
        dimensions: Dicionário com dimensões do habitat
        zone_colors: Dicionário com cores das zonas
        zone_names: Dicionário com nomes das zonas
    
    Returns:
        Figura Plotly com o layout 2D
    """
    fig = go.Figure()
    
    # Calcula grid layout
    total_zone_area = sum(zones.values())
    y_offset = 0
    
    shapes = []
    annotations = []
    
    for zone, area in zones.items():
        proportion = area / total_zone_area
        height = proportion * 10  # altura proporcional
        
        # Adiciona retângulo para a zona
        shapes.append(dict(
            type="rect",
            x0=0, y0=y_offset,
            x1=10, y1=y_offset + height,
            fillcolor=zone_colors[zone],
            opacity=0.7,
            line=dict(color=zone_colors[zone], width=3)
        ))
        
        # Adiciona label
        annotations.append(dict(
            x=5, y=y_offset + height/2,
            text=f"<b>{zone_names[zone]}</b><br>{area:.1f} m²",
            showarrow=False,
            font=dict(size=14, color="white"),
            bgcolor=zone_colors[zone],
            borderpad=8,
            bordercolor=zone_colors[zone],
            borderwidth=2,
            opacity=0.9
        ))
        
        y_offset += height
    
    fig.update_layout(
        shapes=shapes,
        annotations=annotations,
        xaxis=dict(range=[-1, 11], showgrid=False, zeroline=False, visible=False),
        yaxis=dict(range=[-1, 11], showgrid=False, zeroline=False, visible=False),
        plot_bgcolor='rgba(15, 20, 25, 0.9)',
        paper_bgcolor='rgba(15, 20, 25, 0)',
        height=600,
        margin=dict(l=20, r=20, t=40, b=20),
        title=dict(
            text="<b>HABITAT FLOOR PLAN - TOP VIEW</b>",
            font=dict(size=20, color="#A0AEC0"),
            x=0.5,
            xanchor='center'
        )
    )
    
    return fig
