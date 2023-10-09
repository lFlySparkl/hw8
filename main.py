from datetime import date
from datetime import datetime


def day_change(birthday_arr: list, b_date: date, user, current_date: date):
    get_day = b_date.strftime("%A")

    if b_date.month == 12 and b_date.day == 30 and get_day == "Saturday":
        b_date = b_date.replace(day=1, month=1, year=current_date.year + 1)
        user["birthday"] = b_date
        birthday_arr.append(user)
    elif b_date.month == 12 and b_date.day == 30 and get_day == "Sunday":
        b_date = b_date.replace(day=1, month=1, year=current_date.year + 1)
        user["birthday"] = b_date
        birthday_arr.append(user)
    elif b_date.month == 12 and b_date.day == 31 and get_day == "Saturday":
        b_date = b_date.replace(day=2, month=1, year=current_date.year + 1)
        user["birthday"] = b_date
        birthday_arr.append(user)
    elif b_date.month == 12 and b_date.day == 31 and get_day == "Sunday":
        b_date = b_date.replace(day=1, month=1, year=current_date.year + 1)
        user["birthday"] = b_date
        birthday_arr.append(user)
    else:
        if get_day == "Saturday":
            if b_date.day == 30:
                b_date = b_date.replace(day=1, month=current_date.month + 1)
                user["birthday"] = b_date
                birthday_arr.append(user)
            elif b_date.day == 31:
                b_date = b_date.replace(day=1, month=current_date.month + 1)
                user["birthday"] = b_date
                birthday_arr.append(user)
            else:
                b_date = b_date.replace(day=b_date.day + 2)
                user["birthday"] = b_date
                birthday_arr.append(user)
        elif get_day == "Sunday":
            if b_date.day == 30:
                b_date = b_date.replace(
                    day=current_date.day + 1, month=current_date.month + 1
                )
                user["birthday"] = b_date
                birthday_arr.append(user)
            elif b_date.day == 31:
                b_date = b_date.replace(
                    day=current_date.day + 1, month=current_date.month + 1
                )
                user["birthday"] = b_date
                birthday_arr.append(user)
            else:
                b_date = b_date.replace(day=b_date.day + 1)
                user["birthday"] = b_date
                birthday_arr.append(user)
        else:
            user["birthday"] = b_date
            birthday_arr.append(user)
    return birthday_arr


def get_birthdays_per_week(users):
    # current_date = date.today()
    current_date = date(2024, 6, 30)
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
        {"name": "Jan Koum", "birthday": date(2024, 6, 30)},
    ]

    result: list = get_birthdays_per_week(users)

    if result:
        for user in result:
            print(f"{user['name']}: {user['birthday']}")
    else:
        print("Birthday list is empty")
