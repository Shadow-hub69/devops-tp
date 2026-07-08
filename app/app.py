from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

VERSION = "1.1"

@app.route("/")
def home():
    return render_template(
        "index.html",
        version=VERSION,
        message="Nouvelle version déployée automatiquement avec Jenkins + Docker !",
        date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
