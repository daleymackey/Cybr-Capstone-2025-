import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import polars as pl

def create_auth_logs_tab(auth_logs):
    
    def get_login_status_chart(data):
        # Success vs Failure distribution
        status_counts = data.group_by("login_status").count().sort("count", descending=True)
        
        statuses = status_counts['login_status'].to_list()
        counts = status_counts['count'].to_list()
        
        # Color code: green for success, red for failure
        colors = ['green' if status == 'Success' else 'red' for status in statuses]
        
        fig = go.Figure(data=[go.Pie(labels=statuses, values=counts)])
        fig.update_traces(marker_colors=colors, textinfo='label+percent')
        fig.update_layout(title="Login Success vs Failure Rate")
        return fig
    
    def get_failed_logins_by_ip_chart(data):
        # Get only failed logins and count by IP
        failed_logins = (data.filter(pl.col("login_status") == "Failure")
                            .group_by("ip_address")
                            .count()
                            .sort("count", descending=True)
                            .head(10))
        
        ips = failed_logins['ip_address'].to_list()
        counts = failed_logins['count'].to_list()
        
        fig = go.Figure(data=[go.Bar(x=counts, y=ips, orientation='h')])
        fig.update_layout(
            title="Top 10 IPs with Failed Login Attempts",
            xaxis_title="Failed Attempts",
            yaxis_title="IP Address",
            height=500
        )
        return fig
    
    def get_login_timeline_chart(data):
        # Login attempts over time by hour
        timeline_data = data.with_columns([
            pl.col("login_timestamp").str.to_datetime().dt.hour().alias("hour")
        ]).group_by(["hour", "login_status"]).count().sort("hour")
        
        # Separate success and failure data
        success_data = timeline_data.filter(pl.col("login_status") == "Success")
        failure_data = timeline_data.filter(pl.col("login_status") == "Failure")
        
        fig = go.Figure()
        
        if len(success_data) > 0:
            fig.add_trace(go.Scatter(
                x=success_data['hour'].to_list(),
                y=success_data['count'].to_list(),
                mode='lines+markers',
                name='Successful Logins',
                line=dict(color='green')
            ))
        
        if len(failure_data) > 0:
            fig.add_trace(go.Scatter(
                x=failure_data['hour'].to_list(),
                y=failure_data['count'].to_list(),
                mode='lines+markers',
                name='Failed Logins',
                line=dict(color='red')
            ))
        
        fig.update_layout(
            title="Login Attempts by Hour of Day",
            xaxis_title="Hour (24h format)",
            yaxis_title="Number of Attempts"
        )
        return fig
    
    def get_geo_location_chart(data):
        # Login attempts by geographic location
        geo_counts = data.group_by("geo_location").count().sort("count", descending=True).head(10)
        
        locations = geo_counts['geo_location'].to_list()
        counts = geo_counts['count'].to_list()
        
        fig = go.Figure(data=[go.Bar(x=counts, y=locations, orientation='h')])
        fig.update_layout(
            title="Top 10 Login Locations",
            xaxis_title="Number of Login Attempts",
            yaxis_title="Geographic Location",
            height=500
        )
        return fig
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H3("🔐 Authentication Security Analytics", className="mb-3"),
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Total Login Attempts: {len(auth_logs):,}", className="card-title"),
                        html.P(f"Data Range: {auth_logs.shape[0]} records", className="card-text")
                    ])
                ], color="success", outline=True)
            ], width=6),
            dbc.Col([
                dcc.Graph(
                    figure=get_login_status_chart(auth_logs),
                    style={'height': '400px'}
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_login_timeline_chart(auth_logs),
                    style={'height': '400px'}
                )
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_failed_logins_by_ip_chart(auth_logs),
                    style={'height': '500px'}
                )
            ], width=6),
            dbc.Col([
                dcc.Graph(
                    figure=get_geo_location_chart(auth_logs),
                    style={'height': '500px'}
                )
            ], width=6)
        ])
    ])