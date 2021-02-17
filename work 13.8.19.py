tickets = int(input('Введите количество билетов'))

price = int()
for i in range(tickets):
    age = int(input('Введите возраст'))
    if age < 18:
        price = price + 0

    if age > 18 and age <= 25:
        price = price + 990

    if age >= 26 and age <= 99:
        price = price + 1390
    if age > 99:
        print('неверный возраст')
if tickets > 3:
    price = price * 0.9
print(price)
