from flask import Flask
from flask import render_template
import pickle

app = Flask(__name__)

with open("card_data.pickle", "rb") as f:
    x = pickle.load(f)

record = x.values.tolist()
header = x.columns


@app.route("/")
def index():
    return render_template('index.html', header=header, record=record)


if __name__ == "__main__":
    app.run(debug=True)


