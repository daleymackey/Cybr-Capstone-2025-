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

# Cybersecurity Dashboard

A Python Dash application for monitoring cybersecurity data across 5 domains: web server logs, authentication, malware alerts, network traffic, and security incidents.

## Setup and Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your browser to: http://localhost:8050

## Requirements

- Python 3.12 or higher
- All dependencies listed in requirements.txt

## Project Structure

- `app.py` - Main application file
- `data_loader.py` - Data processing functions
- `data/` - CSV data files (5 datasets)
- `tabs/` - Individual dashboard tabs
- `assets/` - CSS styling

## Troubleshooting

If you get import errors, make sure your virtual environment is activated and all dependencies are installed.

If the app won't start, check that Python 3.12+ is installed and all CSV files are present in the data directory.