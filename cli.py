import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order

parser = argparse.ArgumentParser(description="Trading Bot CLI")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()


error = validate_order(args.symbol, args.side, args.type, args.quantity, args.price)
if error:
    print(f"Error: {error}")
    exit()



if args.type == "MARKET":
    result = place_market_order(args.symbol, args.side, args.quantity)

elif args.type == "LIMIT":
    if args.price is None:
        print("Price required for LIMIT order")
        exit()
    result = place_limit_order(args.symbol, args.side, args.quantity, args.price)

print(result)