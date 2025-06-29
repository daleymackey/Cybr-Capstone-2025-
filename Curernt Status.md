# Everything Organic - Cybersecurity Dashboard Project

## Project Overview

**Objective**: Build a professional data science web app with 5 main tabs analyzing cybersecurity data. Each tab should have 2-4 sub-features/visualizations to demonstrate security posture analysis.

**Tech Stack**: Python Dash, Plotly, Polars (data processing), Bootstrap components

**Timeline**:
- **Phase 1** (Due June 30): Design presentation
- **Phase 2** (Due July 14): Build first 2 features  
- **Phase 3** (Due July 23): Complete app + final presentation

---

## Current Status & Environment ✅

### COMPLETED:
- ✅ Python 3.12 in virtual environment with all dependencies
- ✅ Clean project structure with main files in root
- ✅ 5 CSV datasets successfully loading with data_loader.py
- ✅ **Working 5-tab dashboard** with navigation and data integration
- ✅ Bootstrap styling with color-coded interface
- ✅ Live data display showing record counts and metrics
- ✅ **COMPLETE Tab 1: Web Server Analytics** with 4 functional charts
- ✅ Modular tab structure using separate files

### Current Functionality:
- 🌐 **Web Server Logs (1000 records) - COMPLETE WITH 4 CHARTS**
  - ✅ HTTP Status Code Distribution (Pie Chart)
  - ✅ Traffic Timeline by Hour (Line Chart) 
  - ✅ Server Response Time Distribution (Histogram)
  - ✅ Top 15 Most Accessed URLs (Horizontal Bar Chart)
- 🔐 Authentication (1000 records) - Basic layout only
- 🦠 Malware Alerts (1000 records) - Basic layout only
- 📡 Network Traffic (1000 records) - Basic layout only
- 🚨 Security Incidents (1000 records) - Basic layout only

### Project Structure:
```
├── app.py (✅ working 5-tab dashboard)
├── data_loader.py (✅ working)
├── data/ (5 CSV files, 1000 rows each)
├── tabs/ (5 empty .py files - for future expansion)
├── components/ (empty - for future shared components)
└── assets/ (CSS)
```

### Datasets Available (1000 rows each)
1. **Web Server Access Logs**: timestamp, IP, method, status_code, response_size, user_agent, referrer
2. **User Authentication Logs**: timestamp, username, auth_result, IP, user_agent, session_duration
3. **Malware Threat Alerts**: timestamp, threat_type, severity, source_IP, affected_system, action_taken
4. **Network Traffic Summary**: timestamp, inbound/outbound_bytes, protocol, suspicious_activity, source_IP
5. **Security Incident Reports**: incident_ID, timestamp, category, detected_by, response_time, resolution_status

---

## Phase 1 Presentation Structure (8-10 slides)

### Slide 1: Title & Team Introduction
- "Everything Organic Cybersecurity Dashboard"
- Team member names + brief intro
- Project timeline overview

### Slide 2: Business Problem & App Purpose
- Everything Organic needs unified security visibility
- 5 separate data sources = blind spots
- Goal: Real-time security posture monitoring

### Slide 3: Tech Stack & Architecture
- Python Dash + Plotly for interactive analytics
- Polars for fast data processing
- 5 integrated datasets (1000 records each)
- Bootstrap UI for professional look

### Slide 4: Dataset Overview & Integration Strategy
- Show the 5 datasets with key columns
- Explain how you'll cross-reference IPs across datasets
- Timeline correlation across all data sources

### Slide 5: Tab 1 - Web Server Analytics (Deep Dive)
- 4 planned features with specific charts
- Which columns you'll use (status_code, timestamp, IP, response_size)
- Security insights: attack patterns, unusual traffic

### Slide 6: Tab 2 - Authentication Security (Deep Dive)
- 4 planned features with specific charts  
- Key columns (auth_result, IP, session_duration, timestamp)
- Security insights: brute force detection, anomalies

### Slide 7: Tabs 3-5 Overview
- Quick feature summary for Malware, Network, Incidents
- Cross-dataset analysis opportunities (same IPs across logs)
- Timeline correlations between incidents and logs

### Slide 8: Advanced Analytics Planned
- IP reputation scoring (appears in multiple datasets)
- Time-based correlation analysis
- Security KPI dashboard with actionable metrics

### Slide 9: Demo of Current Progress
- Screenshot of working 5-tab interface
- Show data loading successfully
- Preview of where charts will go

### Slide 10: Next Steps & Timeline
- Phase 2: Complete Web Server + Authentication tabs (July 14)
- Phase 3: Remaining tabs + final presentation (July 23)
- Questions?

---

## Detailed Feature Breakdown by Tab

### 🌐 Tab 1: Web Server Analytics
- **Feature 1:** Status Code Distribution (pie/bar chart)
  - Columns: `status_code`
  - Security Insight: Identify attack patterns (404s, 500s)
- **Feature 2:** Traffic Timeline (line chart by hour/day)
  - Columns: `timestamp`, count of requests
  - Security Insight: Detect traffic spikes, DDoS patterns
- **Feature 3:** Top IPs by Request Volume (bar chart)
  - Columns: `IP`, count of requests
  - Security Insight: Identify potential attackers
- **Feature 4:** Response Size Analysis (histogram)
  - Columns: `response_size`
  - Security Insight: Detect data exfiltration

### 🔐 Tab 2: Authentication Security
- **Feature 1:** Success/Failure Rate Over Time (line chart)
  - Columns: `timestamp`, `auth_result`
  - Security Insight: Identify attack campaigns
- **Feature 2:** Failed Login Attempts by IP (bar chart)
  - Columns: `IP`, `auth_result` (failed only)
  - Security Insight: Brute force detection
- **Feature 3:** Session Duration Distribution (histogram)
  - Columns: `session_duration`
  - Security Insight: Anomalous session behavior
- **Feature 4:** Authentication Method Breakdown (pie chart)
  - Columns: `auth_result`
  - Security Insight: Overall authentication health

### 🦠 Tab 3: Malware & Threats
- **Feature 1:** Threat Severity Timeline (stacked area chart)
  - Columns: `timestamp`, `severity`
  - Security Insight: Escalating threat levels
- **Feature 2:** Threat Types Distribution (pie chart)
  - Columns: `threat_type`
  - Security Insight: Most common attack vectors
- **Feature 3:** Actions Taken Effectiveness (bar chart)
  - Columns: `action_taken`
  - Security Insight: Response effectiveness
- **Feature 4:** Top Source IPs for Threats (bar chart)
  - Columns: `source_IP`, count of threats
  - Security Insight: Major threat sources

### 📡 Tab 4: Network Traffic
- **Feature 1:** Inbound vs Outbound Traffic Timeline (dual-axis line)
  - Columns: `timestamp`, `inbound_bytes`, `outbound_bytes`
  - Security Insight: Data flow anomalies
- **Feature 2:** Protocol Usage Distribution (pie chart)
  - Columns: `protocol`
  - Security Insight: Unusual protocol activity
- **Feature 3:** Suspicious Activity Detection Rate (gauge/KPI)
  - Columns: `suspicious_activity`
  - Security Insight: Overall network health
- **Feature 4:** Traffic Volume by Source IP (treemap)
  - Columns: `source_IP`, total bytes
  - Security Insight: Heavy network users

### 🚨 Tab 5: Security Incidents
- **Feature 1:** Incident Categories Breakdown (horizontal bar)
  - Columns: `category`
  - Security Insight: Most common incident types
- **Feature 2:** Response Time Analysis (box plot)
  - Columns: `response_time`
  - Security Insight: Response efficiency
- **Feature 3:** Resolution Status Tracking (donut chart)
  - Columns: `resolution_status`
  - Security Insight: Incident closure rate
- **Feature 4:** Detection Method Effectiveness (bar chart)
  - Columns: `detected_by`
  - Security Insight: Best detection sources

---

## Cross-Dataset Analysis Opportunities

### IP Address Correlation
- Track same IPs across: Web Server Logs, Authentication, Malware Alerts, Network Traffic
- Build IP reputation scoring system
- Identify coordinated attacks

### Timeline Correlation
- Correlate incidents with:
  - Authentication failures
  - Malware alerts
  - Traffic spikes
  - Web server errors

### Advanced Security KPIs
- **Security Posture Score**: Weighted metric across all datasets
- **Threat Response Time**: From detection to resolution
- **Attack Success Rate**: Failed vs successful authentication attempts
- **Network Anomaly Index**: Suspicious activity percentage

---

## Next Steps: Implementation Priority

### ✅ COMPLETED - Phase 1 Ready (For June 30 Presentation):
1. ✅ **Tab 1: Web Server Analytics - COMPLETE**
   - ✅ HTTP Status Code Distribution (Security insight: 15.2% 404s + 13.2% 403s suggest scanning attacks)
   - ✅ Traffic Timeline by Hour (Shows activity patterns and potential attack windows)
   - ✅ Server Response Time Distribution (Performance monitoring with 201.5ms average)
   - ✅ Top Accessed URLs/Endpoints (Security targeting analysis)

### Immediate Next Steps (Post-Presentation):
1. **Tab 2: Authentication Security** (Next priority for Phase 2)
   - Login success/failure patterns over time
   - Failed login attempts by IP (brute force detection)
   - Geographic analysis of authentication attempts
   - Session duration analysis

### Phase 2 (Due July 14):
1. Complete Tab 2: Authentication Security (4 charts)
2. Begin Tab 3: Malware & Threats (2 charts minimum)
3. Implement cross-dataset IP correlation analysis

### Phase 3 (Due July 23):
1. Complete remaining tabs (Malware, Network, Incidents)
2. Implement advanced analytics and KPIs
3. Final presentation with full demonstration

---

## Technical Implementation Notes

### Current Dashboard Status:
- ✅ **Tab 1 (Web Server Analytics): COMPLETE** - 4 functional charts implemented
- Dashboard navigation and data loading working properly
- Modular structure established for remaining tabs

### **IMPORTANT: ARM64 Environment Considerations**
- **Pandas installation fails** on ARM64 Windows architecture
- **Solution**: Using Plotly Graph Objects instead of Plotly Express
- **Impact**: More verbose chart code but same functionality
- **Workaround proven successful** for all chart types

### Recommended Chart Libraries:
- **Plotly Graph Objects**: Primary choice (ARM64 compatible)
- **Plotly Express**: Avoid due to pandas dependency
- **Dash Bootstrap Components**: Working perfectly for styling

### Data Processing Strategy:
- ✅ **Polars for data operations** (groupby, filtering, sorting)
- ✅ **Direct list extraction** from Polars DataFrames (.to_list())
- ✅ **No pandas conversion needed** with Graph Objects approach
- ✅ **Fast performance** maintained