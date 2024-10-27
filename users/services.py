import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

######################################################
# Библиотека работает не корректно. ##################
# from forex_python.converter import CurrencyRates####
# def convert_rub_to_usd(amount):#####################
# ####"""Конвертирует рубли в доллары."""#############
# ####c = CurrencyRates()#############################
# ####rate = c.get_rate("RUB", "USD")#################
# ####return int(amount * rate)#######################
######################################################


def convert_rub_to_usd(amount):
    """Конвертирует рубли в доллары."""
    return int(amount * 0.013)


def create_stripe_price(amount):
    """Создает цену в Stripe."""
    product = stripe.Product.create(name="Payment")

    price = stripe.Price.create(
        product=product.id,
        unit_amount=amount * 100,
        currency="usd",
    )
    return price


def create_stripe_session(price):
    """Создает сессию на оплату в Stripe."""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
