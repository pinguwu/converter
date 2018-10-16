from flask import Flask, url_for, render_template

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

@app.route("/response")
def render_response():
    fh = float(request.args['fh'])
    lbs = float(request.args['lbs'])
    usd = float(request.args['usd'])

    if (fh != None or fh != ''):
        ans = (fh - 32) * 5/9
        return render_template('response.html', response = ans)

    elif (lbs != None or lbs != ''):
        ans = lbs / 2.205
        return render_template('response.html', response = ans)

    elif (usd != None or usd != ''):
        ans = usd / 1.16
        return render_template('response.html', response = ans)


if __name__=="__main__":
    app.run(debug=False, port=54321)
