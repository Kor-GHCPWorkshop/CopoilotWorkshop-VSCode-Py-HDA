def get_discounted_price(price, customer_type):
    if customer_type == "regular":
        if price > 100:
            return price * 0.9
        else:
            return price
    elif customer_type == "member":
        if price > 100:
            return price * 0.85
        else:
            return price * 0.95
    elif customer_type == "vip":
        if price > 100:
            return price * 0.8
        else:
            return price * 0.9
    else:
        return price



