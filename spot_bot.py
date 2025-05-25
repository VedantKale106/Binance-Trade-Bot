# spot_bot.py
from binance.client import Client
from binance.enums import *
import logging

# Setup logging
logging.basicConfig(filename='trading_bot.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SpotBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.API_URL = 'https://testnet.binance.vision/api'
        try:
            self.client.get_account()
            print("✅ Connected to Binance Spot Testnet")
        except Exception as e:
            logging.error(f"Connection Error: {str(e)}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            side_enum = SIDE_BUY if side == 'BUY' else SIDE_SELL

            if order_type == 'MARKET':
                order = self.client.order_market(
                    symbol=symbol,
                    side=side_enum,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.order_limit(
                    symbol=symbol,
                    side=side_enum,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            else:
                return {"status": "error", "message": "Invalid order type"}

            logging.info(f"Order Placed: {order}")
            return {"status": "success", "order": order}
        except Exception as e:
            logging.error(f"Order Error: {str(e)}")
            return {"status": "error", "message": str(e)}
