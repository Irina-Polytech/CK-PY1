money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
money_capital -= (spend - salary)
month += 1
while money_capital + salary > spend * (1+ increase):
    spend += spend * increase
    money_capital -= (spend - salary)
    month += 1
# TODO Оформить решение

print(month)
