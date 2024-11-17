car_prices = [20000, 25000, 30000, 45000, 70000]

def max_price(car_prices):
    max_cost = 0
    for price in car_prices:
        if price > max_cost:
            max_cost = price
    return max_cost


print("The max price is $", format(max(car_prices), ',.2f'), sep='')
print("The min price is $", format(min(car_prices), ',.2f'), sep='')


print("The max price (custom) is $", format(max_price(car_prices), ',.2f'), sep='')
