from datetime import timedelta, date, datetime


def day_change(birthday_arr: list, b_date: date, user, current_date: date):
    get_day = b_date.strftime("%A")

    if get_day == "Saturday":
        b_date = b_date + timedelta(days=2)
        user["birthday"] = b_date
        birthday_arr.append(user)
    elif get_day == "Sunday":
        b_date = b_date + timedelta(days=2)
        user["birthday"] = b_date
        birthday_arr.append(user)
    else:
        user["birthday"] = b_date
        birthday_arr.append(user)
    return birthday_arr


def get_birthdays_per_week(users):
    current_date = date.today()
    birthday_arr = []

    for user in users:
        bd: date = user["birthday"]
        bd = bd.replace(year=current_date.year)


        if bd.month >= current_date.month:
            if bd.day <= current_date.day and bd.month == current_date.month:
                if bd.day == current_date.day:
                    day_change(birthday_arr, bd, user, current_date)
                else:
                    continue
            else:
                day_change(birthday_arr, bd, user, current_date)
    return birthday_arr


if __name__ == "__main__":
    users = [
        # {"name": "Jan Koum", "birthday": date(2024, 6, 30)},
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill", "birthday": date(1990, 10, 30)},
        {"name": "Marry", "birthday": date(2000, 12, 30)},
        {"name": "Jinny", "birthday": date(2000, 12, 31)},
        {"name": "Jan Koum", "birthday": datetime(1976, 11, 1).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 1).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 2, 28).date()},
    ]

    result: list = get_birthdays_per_week(users)

    if result:
        for user in result:
            print(f"{user['name']}: {user['birthday']}")
    else:
        print("Birthday list is empty")
