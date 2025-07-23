import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import polars as pl

def create_incidents_tab(security_incidents):
    
    def get_incident_categories_chart(data):
        # Incident types breakdown
        category_counts = data.group_by("category").count().sort("count", descending=True)
        
        categories = category_counts['category'].to_list()
        counts = category_counts['count'].to_list()
        
        fig = go.Figure(data=[go.Bar(x=counts, y=categories, orientation='h')])
        fig.update_layout(
            title="Security Incident Categories",
            xaxis_title="Number of Incidents",
            yaxis_title="Incident Category",
            height=500
        )
        return apply_grey_theme(fig)

    def get_response_time_chart(data):
        # Response time distribution
        response_times = data['response_time_minutes'].to_list()
        
        fig = go.Figure(data=[go.Histogram(x=response_times, nbinsx=20)])
        fig.update_layout(
            title="Incident Response Time Distribution",
            xaxis_title="Response Time (minutes)",
            yaxis_title="Number of Incidents",
            bargap=0.1
        )
        
        # Add average line
        avg_time = sum(response_times) / len(response_times)
        fig.add_vline(x=avg_time, line_dash="dash", line_color="red", 
                      annotation_text=f"Avg: {avg_time:.1f} min")

        return apply_grey_theme(fig)

    def get_resolution_status_chart(data):
        # Resolution effectiveness
        status_counts = data.group_by("resolution_status").count().sort("count", descending=True)
        
        statuses = status_counts['resolution_status'].to_list()
        counts = status_counts['count'].to_list()
        
        # Color code: green=resolved, yellow=in progress, red=unresolved
        color_map = {'Resolved': 'green', 'In Progress': 'orange', 'Unresolved': 'red'}
        colors = [color_map.get(status, 'gray') for status in statuses]
        
        fig = go.Figure(data=[go.Pie(labels=statuses, values=counts)])
        fig.update_traces(marker_colors=colors, textinfo='label+percent')
        fig.update_layout(title="Incident Resolution Status")
        return apply_grey_theme(fig)

    def get_detection_method_chart(data):
        # How incidents are being detected
        detection_counts = data.group_by("detected_by").count().sort("count", descending=True)
        
        methods = detection_counts['detected_by'].to_list()
        counts = detection_counts['count'].to_list()
        
        fig = go.Figure(data=[go.Bar(x=methods, y=counts)])
        fig.update_layout(
            title="Incident Detection Methods",
            xaxis_title="Detection Source",
            yaxis_title="Number of Incidents Detected"
        )
        return apply_grey_theme(fig)

    def apply_grey_theme(fig):
        """Apply consistent grey theme to all charts"""
        fig.update_layout(
            plot_bgcolor='#bdc3c7',      # Grey chart background
            paper_bgcolor='#bdc3c7',     # Grey outer background  
            font=dict(color="#425a72"),  # Dark grey text
            title=dict(font=dict(color='#2c3e50', size=16))
        )
        return fig
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H3("🚨 Security Incident Analytics", className="mb-3"),
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Total Security Incidents: {len(security_incidents):,}", className="card-title"),
                        html.P(f"Data Range: {security_incidents.shape[0]} records", className="card-text")
                    ])
                ], color="danger", outline=True)
            ], width=6),
            dbc.Col([
                dcc.Graph(
                    figure=get_resolution_status_chart(security_incidents),
                    style={'height': '500px'}
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_response_time_chart(security_incidents),
                    style={'height': '500px'}
                )
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_incident_categories_chart(security_incidents),
                    style={'height': '500px'}
                )
            ], width=6),
            dbc.Col([
                dcc.Graph(
                    figure=get_detection_method_chart(security_incidents),
                    style={'height': '500px'}
                )
            ], width=6)
        ])
    ])