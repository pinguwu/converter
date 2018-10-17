from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/USDEUR")
def render_money():
    return render_template('USDEUR.html')

@app.route("/pk")
def render_weight():
    return render_template('pk.html')

@app.route("/FC")
def render_temp():
    return render_template('FC.html')

@app.route("/responseLBS")
def render_responseLBS():
    lbs = float(request.args['lbs'])
    ans = lbs * 2.25

    return render_template('responseLBS.html', response = ans)

@app.route("/responseTEMP")
def render_responseTEMP():
    temp = float(request.args['fh'])
    ans = (temp - 32) * 5/9

    return render_template('responseTEMP', response = ans)

@app.route("/responseUSD")
def render_responseUSD():
    mon = float(request.args['usd'])
    ans = mon * 0.87

    return render_template('responseUSD', response = ans)


if __name__=="__main__":
    app.run(debug=False, port=54321)
