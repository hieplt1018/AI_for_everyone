def total_cost(money):
    if money >= 2000:
        money = money - money * 0.2
    elif money >= 1000:
        money = money - money * 0.1
    else:
        money = money - money * 0.05
    return money
print(total_cost(3000))
print(total_cost(800))
print(total_cost(1500))