from flask import Flask

app = Flask(__name__)

@app.route("/")
def bomdia_princesa():
    return "<p>Bom dia princesa</p>"