import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import polars as pl

def create_web_logs_tab(web_logs):
    
    def get_status_code_chart(data):
        status_counts = data.group_by("status_code").count().sort("count", descending=True)
        
        status_codes = status_counts['status_code'].to_list()
        counts = status_counts['count'].to_list()
        
        # Use Graph Objects instead of Express
        import plotly.graph_objects as go
        
        fig = go.Figure(data=[go.Pie(labels=status_codes, 
                                    values=counts,
                                    textinfo='label+percent')])
        
        fig.update_layout(title="HTTP Status Code Distribution")
        return fig
    
    def get_traffic_timeline_chart(data):
    # Convert timestamp to datetime and extract hour
        timeline_data = data.with_columns([
            pl.col("timestamp").str.to_datetime().dt.hour().alias("hour")
        ]).group_by("hour").count().sort("hour")
        
        hours = timeline_data['hour'].to_list()
        counts = timeline_data['count'].to_list()
        
        import plotly.graph_objects as go
        
        fig = go.Figure(data=go.Scatter(x=hours, y=counts, mode='lines+markers'))
        fig.update_layout(
            title="Web Traffic by Hour of Day",
            xaxis_title="Hour (24h format)",
            yaxis_title="Number of Requests"
        )
        return fig
    
    def get_response_time_chart(data):
    # Create response time histogram
        response_times = data['response_time_ms'].to_list()
        
        import plotly.graph_objects as go
        
        fig = go.Figure(data=[go.Histogram(x=response_times, nbinsx=20)])
        fig.update_layout(
            title="Server Response Time Distribution",
            xaxis_title="Response Time (milliseconds)",
            yaxis_title="Number of Requests",
            bargap=0.1
        )
        
        # Add a vertical line at the average
        avg_time = sum(response_times) / len(response_times)
        fig.add_vline(x=avg_time, line_dash="dash", line_color="red", 
                    annotation_text=f"Avg: {avg_time:.1f}ms")
        
        return fig
    
    def get_top_urls_chart(data):
    # Get top 15 most accessed URLs
        top_urls = (data.group_by("url_accessed")
                    .count()
                    .sort("count", descending=True)
                    .head(15))
        
        urls = top_urls['url_accessed'].to_list()
        counts = top_urls['count'].to_list()
        
        # Shorten long URLs for display
        display_urls = [url if len(url) <= 30 else url[:27] + "..." for url in urls]
        
        import plotly.graph_objects as go
        
        fig = go.Figure(data=[go.Bar(x=counts, y=display_urls, orientation='h')])
        fig.update_layout(
            title="Top 15 Most Accessed URLs/Endpoints",
            xaxis_title="Number of Requests",
            yaxis_title="URL Path",
            height=600
        )
        
        # Color bars based on count - highest in red (potential targets)
        max_count = max(counts)
        colors = ['darkred' if c == max_count else 'steelblue' for c in counts]
        fig.data[0].marker.color = colors
        
        return fig
        
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H3("📊 Web Server Analytics", className="mb-3"),
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Total Requests: {len(web_logs):,}", className="card-title"),
                        html.P(f"Data Range: {web_logs.shape[0]} records", className="card-text")
                    ])
                ], color="primary", outline=True)
            ], width=6),
            dbc.Col([
                dcc.Graph(
                    figure=get_status_code_chart(web_logs),
                    style={'height': '500px'}
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_traffic_timeline_chart(web_logs),
                    style={'height': '500px'}
                )
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_response_time_chart(web_logs),
                    style={'height': '500px'}
                )
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=get_top_urls_chart(web_logs),
                    style={'height': '500px'}
                )
            ], width=12)
        ])
    ])