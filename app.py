from flask import Flask, render_template
import json
import requests


app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello():
    return "Hello World"


@app.route("/color")
def styled_name():
    color = "blue"
    return render_template("my_page.html", content=color)


@app.route("/dummy")
def get_dummy_products():
    r = requests.get("https://dummyjson.com/products")
    products = json.loads(r.content).get("products")
    print(products)
    return render_template("dummy_page.html", content=products)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

