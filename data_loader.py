import polars as pl
import os

def load_datasets():
    """Load all cybersecurity datasets"""
    data_dir = "data"
    
    try:
        print("Loading datasets...")
        
        # Load web server logs (XLSX)
        web_logs = pl.read_csv(os.path.join(data_dir, "Dataset 1__Web_Server_Access_Logs.csv"))
        print(f"✓ Web logs loaded: {web_logs.shape}")
        
        # Load authentication logs (CSV)
        auth_logs = pl.read_csv(os.path.join(data_dir, "Dateset 2__User_Authentication_Logs.csv"))
        print(f"✓ Auth logs loaded: {auth_logs.shape}")
        
        # Load malware alerts (CSV)
        malware_alerts = pl.read_csv(os.path.join(data_dir, "Dataset 3__Malware_Threat_Alerts.csv"))
        print(f"✓ Malware alerts loaded: {malware_alerts.shape}")
        
        # Load network traffic (CSV)
        network_traffic = pl.read_csv(os.path.join(data_dir, "Dataset 4__Network_Traffic_Summary.csv"))
        print(f"✓ Network traffic loaded: {network_traffic.shape}")
        
        # Load security incidents (CSV)
        security_incidents = pl.read_csv(os.path.join(data_dir, "Dataset 5__Security_Incident_Reports.csv"))
        print(f"✓ Security incidents loaded: {security_incidents.shape}")
        
        return {
            'web_logs': web_logs,
            'auth_logs': auth_logs,
            'malware_alerts': malware_alerts,
            'network_traffic': network_traffic,
            'security_incidents': security_incidents
        }
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def get_data_summary():
    """Get a quick summary of all datasets"""
    datasets = load_datasets()
    
    if datasets:
        for name, df in datasets.items():
            print(f"\n=== {name.upper()} ===")
            print(f"Shape: {df.shape}")
            print(f"Columns: {list(df.columns)}")
            print("Sample data:")
            print(df.head(2))
    
    return datasets