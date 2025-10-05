"""
Visualizações 2D interativas com Plotly
"""
import plotly.graph_objects as go
import math
import numpy as np


def create_2d_layout_plotly(zones: dict, floor_area: float, shape_type: str, 
                            dimensions: dict, zone_colors: dict, zone_names: dict) -> go.Figure:
    """
    Cria visualização 2D interativa avançada do layout do habitat usando Plotly.
    
    Args:
        zones: Dicionário com áreas de cada zona
        floor_area: Área total de piso (m²)
        shape_type: Tipo de forma ("Cylinder" ou "Box")
        dimensions: Dicionário com dimensões do habitat
        zone_colors: Dicionário com cores das zonas
        zone_names: Dicionário com nomes das zonas
    
    Returns:
        Figura Plotly com o layout 2D profissional
    """
    fig = go.Figure()
    
    # Configurações de layout
    if shape_type == "Cylinder":
        diameter = dimensions.get("diameter", 8.0)
        radius = diameter / 2
        
        # Layout circular inteligente
        total_zone_area = sum(zones.values())
        current_angle = 0
        
        for zone, area in zones.items():
            # Calcula ângulo proporcional à área
            angle_span = (area / total_zone_area) * 2 * math.pi
            
            # Cria setor circular (fatia de pizza)
            theta = np.linspace(current_angle, current_angle + angle_span, 50)
            r_outer = radius
            r_inner = radius * 0.3  # Deixa espaço central
            
            # Pontos externos
            x_outer = r_outer * np.cos(theta)
            y_outer = r_outer * np.sin(theta)
            
            # Pontos internos (invertidos)
            x_inner = r_inner * np.cos(theta[::-1])
            y_inner = r_inner * np.sin(theta[::-1])
            
            # Combina pontos para formar setor
            x_sector = list(x_outer) + list(x_inner) + [x_outer[0]]
            y_sector = list(y_outer) + list(y_inner) + [y_outer[0]]
            
            # Adiciona setor da zona
            fig.add_trace(go.Scatter(
                x=x_sector,
                y=y_sector,
                fill='toself',
                fillcolor=zone_colors[zone],
                opacity=0.85,
                line=dict(color=zone_colors[zone], width=3),
                mode='lines',
                name=zone_names[zone],
                hovertemplate=f"<b>{zone_names[zone]}</b><br>" +
                             f"Area: {area:.1f} m²<br>" +
                             f"Percentage: {(area/total_zone_area)*100:.1f}%<extra></extra>",
                showlegend=True
            ))
            
            # Adiciona label no centro do setor
            mid_angle = current_angle + angle_span / 2
            label_radius = (r_outer + r_inner) / 2
            label_x = label_radius * np.cos(mid_angle)
            label_y = label_radius * np.sin(mid_angle)
            
            fig.add_annotation(
                x=label_x,
                y=label_y,
                text=f"<b>{zone_names[zone]}</b><br>{area:.1f} m²",
                showarrow=False,
                font=dict(size=11, color="white", family="Arial Black"),
                bgcolor=zone_colors[zone],
                borderpad=6,
                bordercolor="white",
                borderwidth=1,
                opacity=0.95
            )
            
            current_angle += angle_span
        
        # Adiciona círculo central (área comum/corredor)
        theta_center = np.linspace(0, 2*np.pi, 100)
        x_center = r_inner * np.cos(theta_center)
        y_center = r_inner * np.sin(theta_center)
        
        fig.add_trace(go.Scatter(
            x=x_center,
            y=y_center,
            fill='toself',
            fillcolor='rgba(160, 174, 192, 0.3)',
            line=dict(color='#A0AEC0', width=2, dash='dash'),
            mode='lines',
            name='Central Corridor',
            hovertemplate="<b>Central Corridor</b><br>Common Area<extra></extra>",
            showlegend=True
        ))
        
        # Adiciona outline circular externo
        theta_outer = np.linspace(0, 2*np.pi, 100)
        x_outline = radius * np.cos(theta_outer)
        y_outline = radius * np.sin(theta_outer)
        
        fig.add_trace(go.Scatter(
            x=x_outline,
            y=y_outline,
            mode='lines',
            line=dict(color='#A68CFF', width=4),
            name='Hull',
            hovertemplate=f"<b>Habitat Hull</b><br>Diameter: {diameter:.1f} m<extra></extra>",
            showlegend=True
        ))
        
        # Configuração de eixos para circular
        axis_range = [-radius * 1.15, radius * 1.15]
        
    else:  # Box/Rectangular
        length = dimensions.get("length", 8.0)
        width = dimensions.get("width", 6.0)
        
        # Layout em grid inteligente
        total_zone_area = sum(zones.values())
        zone_list = list(zones.items())
        
        # Calcula grid layout otimizado
        num_zones = len(zone_list)
        cols = math.ceil(math.sqrt(num_zones))
        rows = math.ceil(num_zones / cols)
        
        cell_width = length / cols
        cell_height = width / rows
        
        idx = 0
        for row in range(rows):
            for col in range(cols):
                if idx >= num_zones:
                    break
                
                zone, area = zone_list[idx]
                
                # Calcula posição da célula
                x0 = col * cell_width
                x1 = x0 + cell_width
                y0 = row * cell_height
                y1 = y0 + cell_height
                
                # Adiciona retângulo da zona com margem
                margin = 0.1
                fig.add_trace(go.Scatter(
                    x=[x0+margin, x1-margin, x1-margin, x0+margin, x0+margin],
                    y=[y0+margin, y0+margin, y1-margin, y1-margin, y0+margin],
                    fill='toself',
                    fillcolor=zone_colors[zone],
                    opacity=0.85,
                    line=dict(color=zone_colors[zone], width=3),
                    mode='lines',
                    name=zone_names[zone],
                    hovertemplate=f"<b>{zone_names[zone]}</b><br>" +
                                 f"Area: {area:.1f} m²<br>" +
                                 f"Percentage: {(area/total_zone_area)*100:.1f}%<extra></extra>",
                    showlegend=True
                ))
                
                # Adiciona label
                center_x = (x0 + x1) / 2
                center_y = (y0 + y1) / 2
                
                fig.add_annotation(
                    x=center_x,
                    y=center_y,
                    text=f"<b>{zone_names[zone]}</b><br>{area:.1f} m²",
                    showarrow=False,
                    font=dict(size=11, color="white", family="Arial Black"),
                    bgcolor=zone_colors[zone],
                    borderpad=6,
                    bordercolor="white",
                    borderwidth=1,
                    opacity=0.95
                )
                
                idx += 1
        
        # Adiciona outline do habitat
        fig.add_trace(go.Scatter(
            x=[0, length, length, 0, 0],
            y=[0, 0, width, width, 0],
            mode='lines',
            line=dict(color='#A68CFF', width=4),
            name='Hull',
            hovertemplate=f"<b>Habitat Hull</b><br>Dimensions: {length:.1f}m × {width:.1f}m<extra></extra>",
            showlegend=True
        ))
        
        # Adiciona grid de referência
        for i in range(1, cols):
            x_line = i * cell_width
            fig.add_shape(
                type="line",
                x0=x_line, y0=0,
                x1=x_line, y1=width,
                line=dict(color='rgba(160, 174, 192, 0.3)', width=1, dash='dot')
            )
        
        for i in range(1, rows):
            y_line = i * cell_height
            fig.add_shape(
                type="line",
                x0=0, y0=y_line,
                x1=length, y1=y_line,
                line=dict(color='rgba(160, 174, 192, 0.3)', width=1, dash='dot')
            )
        
        # Configuração de eixos para retangular
        axis_range_x = [-length * 0.1, length * 1.1]
        axis_range_y = [-width * 0.1, width * 1.1]
    
    # Layout final
    fig.update_layout(
        xaxis=dict(
            range=axis_range if shape_type == "Cylinder" else axis_range_x,
            showgrid=True,
            gridcolor='rgba(160, 174, 192, 0.1)',
            zeroline=False,
            visible=True,
            title=dict(
                text="Length (m)" if shape_type == "Rectangular" else "",
                font=dict(color='#A0AEC0')
            )
        ),
        yaxis=dict(
            range=axis_range if shape_type == "Cylinder" else axis_range_y,
            showgrid=True,
            gridcolor='rgba(160, 174, 192, 0.1)',
            zeroline=False,
            visible=True,
            scaleanchor="x",
            scaleratio=1,
            title=dict(
                text="Width (m)" if shape_type == "Rectangular" else "",
                font=dict(color='#A0AEC0')
            )
        ),
        plot_bgcolor='rgba(11, 15, 26, 0.95)',
        paper_bgcolor='rgba(11, 15, 26, 0)',
        height=700,
        margin=dict(l=50, r=50, t=80, b=50),
        title=dict(
            text=f"<b>HABITAT FLOOR PLAN</b> · {shape_type} Configuration · {len(zones)} Zones · {floor_area:.1f} m² Total Area",
            font=dict(size=18, color="#E2E8F0", family="Arial Black"),
            x=0.5,
            xanchor='center',
            y=0.98,
            yanchor='top'
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
            yanchor='top'
        ),
        hovermode='closest',
        hoverlabel=dict(
            bgcolor='rgba(11, 15, 26, 0.95)',
            font_size=12,
            font_family="Arial",
            bordercolor='#A68CFF'
        )
    )
    
    return fig
