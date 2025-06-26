# Cybersecurity Dashboard - Environment Setup Guide

## Project Structure
```
Cybr-Capstone-2025-/
├── app.py                    # Main Dash application
├── data_loader.py           # Data loading utilities
├── requirements.txt         # Python dependencies
├── config.py               # Configuration settings
├── assets/
│   └── style.css           # Custom CSS styles
├── components/
│   ├── charts.py           # Reusable chart components
│   └── layouts.py          # Common layout components
├── tabs/
│   ├── web_logs.py         # Dataset 1: Web Server Access Logs
│   ├── auth_logs.py        # Dataset 2: User Authentication Logs
│   ├── malware_alerts.py   # Dataset 3: Malware Threat Alerts
│   ├── network_traffic.py  # Dataset 4: Network Traffic Summary
│   └── incidents.py        # Dataset 5: Security Incident Reports
└── data/
    ├── Dataset 1__Web_Server_Access_Logs.xlsx
    ├── Dateset 2__User_Authentication_Logs.csv
    ├── Dataset 3__Malware_Threat_Alerts.csv
    ├── Dataset 4__Network_Traffic_Summary.csv
    └── Dataset 5__Security_Incident_Reports.csv
```

## Environment Setup Instructions

### 1. Install Python
```powershell
# Install Python 3.12 via winget
winget install Python.Python.3.12
```

### 2. Create Virtual Environment
```powershell
# Navigate to project directory
cd Cybr-Capstone-2025-

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\Activate.ps1

# If execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies
```powershell
# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

### 4. Verify Installation
```powershell
# Test all imports
python -c "import dash; import plotly; import dash_bootstrap_components; import polars; print('SUCCESS: Environment ready!')"
```

### 5. Run the Dashboard
```powershell
# Start the application
python app.py

# Open browser to: http://127.0.0.1:8050/
```

## Dependencies (requirements.txt)
```
dash>=3.0.0
plotly>=6.0.0
dash-bootstrap-components>=2.0.0
polars>=1.30.0
openpyxl>=3.1.0
```

## Key Features
- **5 Main Tabs**: One for each dataset
- **Polars**: Fast data processing (pandas alternative)
- **Bootstrap**: Professional styling
- **Modular Structure**: Easy to maintain and extend

## Troubleshooting

### Python Not Found
- Ensure Python is in PATH
- Restart terminal after installation
- Use full path if needed

### Pandas/Numpy Compilation Issues
- We use Polars instead (no compilation required)
- Works perfectly on ARM64 Windows

### Import Errors
- Ensure virtual environment is activated
- Check all dependencies installed correctly