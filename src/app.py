
from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('python.html'), "surendra python dev"

if __name__ == "__main__":
    app.run()

