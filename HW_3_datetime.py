from datetime import datetime


def get_days_from_today(date):

    try:
        str_to_date = datetime.strptime(date, "%Y-%m-%d").date()  # форматуємо строку в вормат datetime
        return  (datetime.today().date() - str_to_date).days # якщо задана дата пізніша за поточну, результат має бути від'ємним.
    except:
        print("Дата введена не коректно\nВведіть дату у форматі РРРР-ММ-ДД")

print(get_days_from_today("2025-01-31"))
