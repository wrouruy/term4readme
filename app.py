from flask import Flask, request
from renderers.svg import mk_svg
import effects

app = Flask(__name__)

@app.route('/', methods=['GET'])

@app.route('/svg/custom', methods=['GET'])
def custom():
    body = effects.custom()
    return (mk_svg(body), 200, { 'Content-Type': 'image/svg+xml' })

@app.route('/svg/tty-clock', methods=['GET'])
def tty_clock():
    body = effects.tty_clock()
    return (mk_svg(body), 200, { 'Content-Type': 'image/svg+xml' })

if __name__ == '__main__':
    app.run(port=5050)
