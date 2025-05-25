# app.py
from flask import Flask, render_template, request
from spot_bot import SpotBot
from dotenv import load_dotenv
import os

app = Flask(__name__)



# Load .env file
load_dotenv()

# Get credentials
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

bot = SpotBot(API_KEY, API_SECRET)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
        side = request.form['side'].upper()
        order_type = request.form['order_type'].upper()
        quantity = float(request.form['quantity'])
        price = request.form.get('price')

        if order_type == 'LIMIT' and not price:
            result = {"status": "error", "message": "Price required for LIMIT order"}
        else:
            response = bot.place_order(symbol, side, order_type, quantity, price if price else None)
            result = response

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
