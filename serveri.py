from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", rnd=random.randint(1,10))

@app.route('/koodauskerho')
def hello_world():
    return "????"

if __name__ == "__main__":
    por = int(os.environ.get('PORT', 33507))
    app.run(debug=True, port=por)
