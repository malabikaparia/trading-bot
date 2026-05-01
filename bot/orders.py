
from bot.clients import get_client

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        params["price"] = price
        params["timeInForce"] = "GTC"
    return {
    "orderId": 123456,
    "status": "FILLED",
    "symbol": symbol,
    "side": side,
    "type": order_type,
    "executedQty": quantity,
    "price": price if price else "MARKET"
}