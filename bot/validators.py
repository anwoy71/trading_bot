def validate_order(symbol, side, order_type, quantity, price=None):
    if not symbol:
        return "Symbol required"
    
    if side not in ["BUY", "SELL"]:
        return "Side must be BUY or SELL"
    
    if order_type not in ["MARKET", "LIMIT"]:
        return "Invalid order type"
    
    if quantity <= 0:
        return "Quantity must be > 0"
    
    if order_type == "LIMIT" and price is None:
        return "Price required for LIMIT order"
    
    return None