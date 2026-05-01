from bot.client import get_client
import logging
from bot.logging_config import setup_logger

setup_logger()


def place_market_order(symbol, side, quantity):
    client = get_client()
    
    try:
        logging.info(f"Placing MARKET order: {symbol} {side} {quantity}")
        
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        
        logging.info(f"Order response: {order}")
        return order
    
    except Exception as e:
        logging.error(f"MARKET order failed: {str(e)}")
        return {"error": str(e)}


def place_limit_order(symbol, side, quantity, price):
    client = get_client()
    
    try:
        logging.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")
        
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        
        logging.info(f"Order response: {order}")
        return order
    
    except Exception as e:
        logging.error(f"LIMIT order failed: {str(e)}")
        return {"error": str(e)}