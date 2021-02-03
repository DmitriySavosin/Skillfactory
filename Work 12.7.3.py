money = input("Введите сумму депозита:")

money = int(money)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

my_dict = []

my_dict.append(per_cent['ТКБ'] / 100 * money)

my_dict.append(per_cent['СКБ'] / 100 * money)

my_dict.append(per_cent['ВТБ'] / 100 * money)

my_dict.append(per_cent['СБЕР'] / 100 * money)

round_dict = [round(num) for num in my_dict]

print(round_dict)

print('Максимальная сумма, которую вы можете заработать — ', max(round_dict))
