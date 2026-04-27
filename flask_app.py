from flask import Flask, render_template_string
import storage
import sys

app = Flask(__name__)

@app.route('/')
def dashboard():
    history = storage.get_history()
    html = '<h1>📊 Monitoring API (Agify)</h1><table border="1"><tr><th>Date</th><th>Succès</th><th>Échecs</th><th>Latence</th></tr>'
    for r in history:
        html += f'<tr><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]} ms</td></tr>'
    return html + '</table><br><a href="/health">Voir Healthcheck</a>'

@app.route('/health')
def health():
    return {"status": "healthy", "api": "Agify"}, 200
