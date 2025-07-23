import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from data_loader import load_datasets
from tabs.web_logs import create_web_logs_tab
from tabs.auth_logs import create_auth_logs_tab
from tabs.malware_alerts import create_malware_alerts_tab
from tabs.network_traffic import create_network_traffic_tab
from tabs.incidents import create_incidents_tab

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Everything Organic - Cybersecurity Dashboard"

# Load data once at startup
print("Loading data for dashboard...")
datasets = load_datasets()

# Define the main layout
app.layout = dbc.Container([
    # Enhanced Header
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1([
                    html.I(className="fas fa-shield-alt me-3", style={'color': '#e74c3c'}),
                    "Everything Organic - Cybersecurity Command Center"
                ], className="text-center mb-3", 
                   style={'color': '#2c3e50', 'fontWeight': 'bold', 'fontSize': '2.5rem'}),
                html.P("Real-time Security Monitoring & Threat Intelligence Dashboard", 
                       className="text-center text-muted lead mb-4"),
                html.Hr(style={'borderWidth': '3px', 'borderColor': '#e74c3c'})
            ])
        ])
    ]),
    
    # KPI Summary Cards (moved to top)
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("🚨 Critical Alerts", className="text-danger"),
                    html.H2("548", className="text-danger mb-0"),
                    html.P("Failed Login Attempts", className="text-muted")
                ])
            ], color="danger", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("🔥 Active Threats", className="text-warning"), 
                    html.H2("307", className="text-warning mb-0"),
                    html.P("High Severity Malware", className="text-muted")
                ])
            ], color="warning", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("⚡ Response Time", className="text-info"),
                    html.H2("91min", className="text-info mb-0"), 
                    html.P("Average Incident Response", className="text-muted")
                ])
            ], color="info", outline=True)
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("✅ Resolution Rate", className="text-success"),
                    html.H2("59.6%", className="text-success mb-0"),
                    html.P("Incidents Resolved", className="text-muted")
                ])
            ], color="success", outline=True)
        ], width=3)
    ], className="mb-4"),
    
    # Navigation Tabs
    dbc.Row([
        dbc.Col([
            dcc.Tabs(id="main-tabs", value="web-logs", 
                    style={'fontSize': '16px', 'fontWeight': 'bold'},
                    children=[
                dcc.Tab(label="🌐 Web Server Logs", value="web-logs"),
                dcc.Tab(label="🔐 Authentication", value="auth-logs"),
                dcc.Tab(label="🦠 Malware Alerts", value="malware-alerts"),
                dcc.Tab(label="📡 Network Traffic", value="network-traffic"),
                dcc.Tab(label="🚨 Security Incidents", value="incidents")
            ])
        ])
    ], className="mb-4"),
    
    # Tab Content Area
    dbc.Row([
        dbc.Col([
            html.Div(id="tab-content")
        ])
    ])
], fluid=True)

# Main callback to render tab content
@callback(
    Output("tab-content", "children"),
    [Input("main-tabs", "value")]
)
def render_tab_content(active_tab):
    if datasets is None:
        return dbc.Alert("Error loading data. Please check your datasets.", color="danger")
    
    if active_tab == "web-logs":
        return create_web_logs_tab(datasets['web_logs'])
    elif active_tab == "auth-logs":
        return create_auth_logs_tab(datasets['auth_logs'])
    elif active_tab == "malware-alerts":
        return create_malware_alerts_tab(datasets['malware_alerts'])
    elif active_tab == "network-traffic":
        return create_network_traffic_tab(datasets['network_traffic'])
    elif active_tab == "incidents":
        return create_incidents_tab(datasets['security_incidents'])



if __name__ == "__main__":
    app.run(debug=True, port=8050)
