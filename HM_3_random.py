import random


def get_numbers_tiket(min, max, quantity):

        if min >= max or quantity <= 0 or quantity >= (max - min + 1):  #перевіряємо валідність данних
            return []  #як є помилка повертаємо пустий список

        return sorted(random.sample(range(min, max +1), quantity))  #random.sample генерує унікальні числа без додаткових перевірок sorted відсортовані

lottery_numers = get_numbers_tiket(1, 49, 6)  #задаємо параметри розіграшу лотереї
print("Виграшні числа лотереї:", lottery_numers)