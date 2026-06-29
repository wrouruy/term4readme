from flask import Flask, request
from renderers.svg import mk_svg
import effects

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ({ "hello": "world!!" }, 200, { 'Content-Type': 'application/json' })

@app.route('/svg/custom', methods=['GET'])
def custom():
    body = effects.custom()
    print(body['content'])
    return (mk_svg(body), 200, { 'Content-Type': 'image/svg+xml' })

if __name__ == '__main__':
    app.run(port=5050)
