from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")

@app.route("/")
def hello():
    return "Hello World"


@app.route("/color")
def styled_name():
    color = "green"
    return render_template('my_page.html', content=color)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
