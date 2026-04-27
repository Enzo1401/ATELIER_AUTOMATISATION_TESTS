from flask import Flask, render_template_string
import storage
import sys

app = Flask(__name__)

# Le style CSS "Dark Mode" pour le Dashboard
CSS = '''
<style>
    body { 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
        background: #0b1020; 
        color: #e9edff; 
        padding: 40px; 
        display: flex; 
        justify-content: center; 
    }
    .card { 
        background: #121a33; 
        border: 1px solid #23305c; 
        border-radius: 16px; 
        padding: 30px; 
        width: 100%; 
        max-width: 900px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.5); 
    }
    h1 { color: #77baff; margin-bottom: 5px; }
    .subtitle { color: #a0a8c0; margin-bottom: 25px; font-size: 0.9em; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    th { background: #1c264d; color: #77baff; padding: 15px; text-align: left; font-size: 0.85em; text-transform: uppercase; letter-spacing: 1px; }
    td { padding: 15px; border-bottom: 1px solid #23305c; font-size: 0.95em; }
    tr:hover { background: #192345; }
    .status-ok { color: #62d6a0; font-weight: bold; background: rgba(98, 214, 160, 0.1); padding: 4px 8px; border-radius: 4px; }
    .status-bad { color: #ff6b7a; font-weight: bold; background: rgba(255, 107, 122, 0.1); padding: 4px 8px; border-radius: 4px; }
    .latency { color: #ffcc66; font-family: monospace; }
    .btn-health { display: inline-block; margin-top: 20px; color: #77baff; text-decoration: none; font-size: 0.8em; border: 1px solid #77baff; padding: 5px 10px; border-radius: 5px; }
    .btn-health:hover { background: #77baff; color: #121a33; }
</style>
'''

@app.route('/')
def dashboard():
    history = storage.get_history()
    
    # Construction des lignes du tableau
    rows = ""
    for r in history:
        status_class = "status-ok" if r[3] == 0 else "status-bad"
        status_text = "PASS" if r[3] == 0 else "FAIL"
        rows += f'''
        <tr>
            <td>{r[1]}</td>
            <td><b style="color:#62d6a0">{r[2]}</b></td>
            <td><b style="color:#ff6b7a">{r[3]}</b></td>
            <td class="latency">{r[4]} ms</td>
            <td><span class="{status_class}">{status_text}</span></td>
        </tr>
        '''

    html = f'''
    <!DOCTYPE html>
    <html>
    <head><title>API Monitoring - Enzo</title>{CSS}</head>
    <body>
        <div class="card">
            <h1>📊 API Monitoring Dashboard</h1>
            <p class="subtitle">Étudiant : <b>Enzo</b> | Cible : <b>Agify API</b> | Statut : <span style="color:#62d6a0">Online</span></p>
            
            <table>
                <thead>
                    <tr>
                        <th>Date du Run</th>
                        <th>Succès</th>
                        <th>Échecs</th>
                        <th>Latence (QoS)</th>
                        <th>Résultat</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
            <a href="/health" class="btn-health">Accéder au JSON Healthcheck</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/health')
def health():
    return {
        "status": "healthy",
        "api_target": "Agify",
        "database": "SQLite connected",
        "student": "Enzo"
    }, 200
