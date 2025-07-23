import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import polars as pl

def create_network_traffic_tab(network_traffic):
    
    def get_traffic_volume_timeline_chart(data):
        # Traffic over time - inbound vs outbound
        timeline_data = data.with_columns([
            pl.col("sample_time").str.to_datetime().dt.hour().alias("hour")
        ]).group_by("hour").agg([
            pl.col("inbound_bytes").sum().alias("total_inbound"),
            pl.col("outbound_bytes").sum().alias("total_outbound")
        ]).sort("hour")
        
        hours = timeline_data['hour'].to_list()
        inbound = timeline_data['total_inbound'].to_list()
        outbound = timeline_data['total_outbound'].to_list()
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=hours, y=inbound,
            mode='lines+markers',
            name='Inbound Traffic',
            line=dict(color='blue')
        ))
        
        fig.add_trace(go.Scatter(
            x=hours, y=outbound,
            mode='lines+markers',
            name='Outbound Traffic',
            line=dict(color='red')
        ))
        
        fig.update_layout(
            title="Network Traffic Volume by Hour",
            xaxis_title="Hour of Day (24h format)",
            yaxis_title="Traffic Volume (bytes)"
        )
        return apply_grey_theme(fig)
    
    def get_protocol_distribution_chart(data):
        # Protocol usage breakdown
        protocol_counts = data.group_by("protocol").count().sort("count", descending=True)
        
        protocols = protocol_counts['protocol'].to_list()
        counts = protocol_counts['count'].to_list()
        
        fig = go.Figure(data=[go.Pie(labels=protocols, values=counts)])
        fig.update_traces(textinfo='label+percent')
        fig.update_layout(title="Network Protocol Distribution")
        return apply_grey_theme(fig)

    def get_suspicious_activity_chart(data):
        # Suspicious vs normal activity
        suspicious_counts = data.group_by("suspicious_activity").count().sort("count", descending=True)
        
        activities = suspicious_counts['suspicious_activity'].to_list()
        counts = suspicious_counts['count'].to_list()
        
        # Color code: red for suspicious, green for normal
        colors = ['red' if activity == 'Yes' else 'green' for activity in activities]
        
        fig = go.Figure(data=[go.Bar(x=activities, y=counts, marker_color=colors)])
        fig.update_layout(
            title="Suspicious Activity Detection",
            xaxis_title="Activity Type",
            yaxis_title="Number of Connections"
        )
        return apply_grey_theme(fig)
    
    def get_top_traffic_sources_chart(data):
        # Top IPs by total traffic volume
        traffic_by_ip = data.group_by("source_ip").agg([
            (pl.col("inbound_bytes") + pl.col("outbound_bytes")).sum().alias("total_bytes")
        ]).sort("total_bytes", descending=True).head(15)
        
        ips = traffic_by_ip['source_ip'].to_list()
        volumes = traffic_by_ip['total_bytes'].to_list()
        
        fig = go.Figure(data=[go.Bar(x=volumes, y=ips, orientation='h')])
        fig.update_layout(
            title="Top 15 Traffic Sources by Volume",
            xaxis_title="Total Traffic (bytes)",
            yaxis_title="Source IP Address",
            height=600
        )
        return apply_grey_theme(fig)

    def apply_grey_theme(fig):
        """Apply consistent grey theme to all charts"""
        fig.update_layout(
            plot_bgcolor='#e0e5e8',      # Grey chart background
            paper_bgcolor='#e0e5e8',     # Grey outer background  
            font=dict(color="#425a72"),  # Dark grey text
            title=dict(font=dict(color='#2c3e50', size=16))
        )
        return fig
        
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H3("📡 Network Traffic Analytics", className="mb-3"),
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Total Traffic Records: {len(network_traffic):,}", className="card-title"),
                        html.P(f"Data Range: {network_traffic.shape[0]} records", className="card-text")
                    ])
                ], color="info", outline=True)
            ], width=6),
            dbc.Col([
                dcc.Graph(
                    figure=get_protocol_distribution_chart(network_traffic),
                    style={'height': '500px'}
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_traffic_volume_timeline_chart(network_traffic),
                    style={'height': '500px'}
                )
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_suspicious_activity_chart(network_traffic),
                    style={'height': '500px'}
                )
            ], width=6),
            dbc.Col([
                dcc.Graph(
                    figure=get_top_traffic_sources_chart(network_traffic),
                    style={'height': '600px'}
                )
            ], width=6)
        ])
    ])