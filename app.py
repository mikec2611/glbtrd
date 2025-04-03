import os
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)

MAPBOX_TOKEN = os.getenv('MAPBOX_TOKEN')

@app.route('/')
def index():
    if not MAPBOX_TOKEN:
        # Handle case where token is not found
        return "Mapbox token not found in .env file", 500
    return render_template('index.html', mapbox_token=MAPBOX_TOKEN)

if __name__ == '__main__':
    # Use watchdog reloader for better compatibility on Windows
    app.run(debug=True, use_reloader=True, reloader_type='watchdog') 