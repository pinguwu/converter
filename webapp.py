from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("EU")
def render_money():
    return render_template('USDEUR.html')

@app.route("LBG")
def render_weight():
    return render_template('pk.html')

@app.route("FC")
def render_temp():
    return render_template('FC.html')



if __name__=="__main__":
    app.run(debug=False, port=54321)
