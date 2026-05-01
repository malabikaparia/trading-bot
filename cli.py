
import argparse
import logging
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_input(args.symbol, args.side, args.type, args.qty, args.price)

    print("Placing order...")
    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

    print("SUCCESS ✅")
    print(f"""
Order Summary:
Symbol: {order['symbol']}
Side: {order['side']}
Type: {order['type']}
Status: {order['status']}
Quantity: {order['executedQty']}
""")

    logging.info(order)

except Exception as e:
    print("ERROR ❌:", e)
    logging.error(str(e))