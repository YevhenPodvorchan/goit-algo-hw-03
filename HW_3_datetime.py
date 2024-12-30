from datetime import datetime


def get_days_from_today(date):

    try:
        str_to_date = datetime.strptime(date, "%Y. %m. %d").date()  # форматуємо строку в вормат datetime

        differ_date =  (datetime.today().date() - str_to_date).days  # якщо задана дата пізніша за поточну, результат має бути від'ємним.
        print(differ_date)
    except:
        print("Дата введена не коректно\nВведіть дату у форматі РРРР-ММ-ДД")

get_days_from_today("2024. 02. 24")