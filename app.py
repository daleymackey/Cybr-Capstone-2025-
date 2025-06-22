from flask import Flask, render_template, request, jsonify, redirect, url_for
import database
import datetime
import sqlite3

app = Flask(__name__)

# Initialize database on startup
database.init_db()

@app.route('/')
def home():
    """Main honeypot login page"""
    # Log that someone visited the page
    database.log_attack(
        ip=request.remote_addr,
        attack_type='page_visit',
        user_agent=str(request.user_agent)
    )
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """Handle login attempts - this is where the magic happens"""
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    
    # Log the login attempt
    database.log_attack(
        ip=request.remote_addr,
        username=username,
        password=password,
        user_agent=str(request.user_agent),
        attack_type='login_attempt'
    )
    
    # Always fail login but make it look realistic
    return render_template('login.html', error="Invalid username or password")

@app.route('/admin')
def admin():
    """Admin dashboard to view attacks"""
    conn = sqlite3.connect(database.DB_NAME)
    
    # Get recent attacks
    attacks = conn.execute('''SELECT * FROM attacks 
                             ORDER BY timestamp DESC LIMIT 100''').fetchall()
    
    # Get attack statistics
    stats = conn.execute('''SELECT 
                              COUNT(*) as total_attacks,
                              COUNT(DISTINCT ip_address) as unique_ips,
                              COUNT(DISTINCT username) as unique_usernames
                           FROM attacks''').fetchone()
    
    conn.close()
    
    return render_template('admin.html', attacks=attacks, stats=stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)