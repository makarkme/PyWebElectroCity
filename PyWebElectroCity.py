from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/delivery')
def delivery():
    return render_template('delivery.html')


@app.route('/payment')
def payment():
    return render_template('payment.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
