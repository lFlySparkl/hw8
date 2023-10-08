from datetime import date, datetime


def get_birthdays_per_week(users):
    current_date = date.today()
    birthday_arr = []

    for user in users:
        bd: date = user["birthday"]
        bd = bd.replace(year=current_date.year)

        if bd.month >= current_date.month:
            if bd.day <= current_date.day and bd.month == current_date.month:
                continue
            else:
                get_day = bd.strftime("%A")

                if get_day == "Saturday":
                    bd = bd.replace(day=bd.day + 2)
                    user["birthday"] = bd
                    birthday_arr.append(user)
                elif get_day == "Sunday":
                    bd = bd.replace(day=bd.day + 1)
                    user["birthday"] = bd
                    birthday_arr.append(user)
                else:
                    user["birthday"] = bd
                    birthday_arr.append(user)
    return birthday_arr


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill", "birthday": date(1990, 10, 29)},
        {"name": "Marry", "birthday": date(2000, 10, 2)},
        {"name": "Jinny", "birthday": date(2000, 10, 10)},
        {"name": "Jan Koum", "birthday": datetime(1976, 11, 1).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 1).date()},
    ]

    result: list = get_birthdays_per_week(users)

    if result:
        for user in result:
            print(f"{user['name']}: {user['birthday']}")
    else:
        print("Birthday list is empty")
