from binance.client import Client

API_KEY = 'ISGxuHpUJ06bNrIpGyAKN4OCmj2DFTI61YgjtFpmrEV9SxGppAy3GfnHQW8Pv2d2'
API_SECRET = 'vnDXIanz63cjBpUhSUKJA0XbzUzsW9YeCfEZeMcI5caXhPFQjIQqUHpeNEfwWp1s'

client = Client(API_KEY, API_SECRET,testnet=True)

print("Account Information:",client.get_account())

client.futures_account()  # This is for FUTURES accounts
print("Futures Account Information:", client.futures_account())
