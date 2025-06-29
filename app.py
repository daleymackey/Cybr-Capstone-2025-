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

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Everything Organic - Cybersecurity Dashboard"

# Load data once at startup
print("Loading data for dashboard...")
datasets = load_datasets()

# Define the main layout
app.layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H1("🛡️ Everything Organic - Cybersecurity Dashboard", 
                   className="text-center mb-4", 
                   style={'color': '#2c3e50', 'fontWeight': 'bold'}),
            html.Hr(style={'borderWidth': '3px', 'borderColor': '#3498db'})
        ])
    ]),
    
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
        return create_network_tab()
    elif active_tab == "incidents":
        return create_incidents_tab()


def create_network_tab():
    df = datasets['network_traffic']
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H3("📡 Network Traffic Analytics", className="mb-3"),
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Traffic Records: {len(df):,}", className="card-title"),
                        html.P("Network monitoring dashboard", className="card-text")
                    ])
                ], color="info", outline=True)
            ])
        ])
    ])

def create_incidents_tab():
    df = datasets['security_incidents']
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H3("🚨 Security Incident Analytics", className="mb-3"),
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Total Incidents: {len(df):,}", className="card-title"),
                        html.P("Incident response dashboard", className="card-text")
                    ])
                ], color="danger", outline=True)
            ])
        ])
    ])

if __name__ == "__main__":
    app.run(debug=True, port=8050)
