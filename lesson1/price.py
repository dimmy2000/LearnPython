def format_price(price):
    price = int(price)
    return 'Цена: {} руб.'.format(price)

print(format_price(56.24))