import frappe
from bitcoin_value import currency


jenvs = {
    "methods": [
        "estate_app.jinja.exponent",
        # "estate_app.jinja.property_in_btc",
    ],
    "filters": [
        "estate_app.jinja.add",
        "estate_app.jinja.property_in_btc",
    ]
}

def property_in_btc(price, btc_cur):
    cur = currency(btc_cur).fetch()
    return f"BTC {float(price)/cur}"

def exponent(num):
    return float(num)**2

def add(v1, v2):
    if (float(v1) + float(v2)) % 2 == 0:
        return int(v1)+int(v2)
    return float(v1) + float(v2)
