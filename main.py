from datetime import date, datetime, timedelta


def day_change(birthday_arr: dict, b_date: date, user):
    get_day = b_date.strftime("%A")

    if get_day == "Saturday":
        user["birthday"] = b_date + timedelta(days=2)
        birthday_arr.update({user["name"]: user["birthday"]})
    elif get_day == "Sunday":
        user["birthday"] = b_date + timedelta(days=1)
        birthday_arr.update({user["name"]: user["birthday"]})
    else:
        user["birthday"] = b_date
        birthday_arr.update({user["name"]: user["birthday"]})
    return birthday_arr


def combine_list(list: dict):
    result = {}
    for name, date_bd in list.items():
        date_bd: date = date_bd
        result.setdefault(date_bd.strftime("%A"), []).append(name)
    return result


def get_birthdays_per_week(users):
    current_date = date.today()
    birthday_arr = {}
    print(current_date)
    print(users)

    for user in users:
        bd: date = user["birthday"]

        if bd.year > current_date.year:
            day_change(birthday_arr, bd, user)
        else:
            if bd.month == 1 and bd.day < 6:
                bd = bd.replace(year=current_date.year + 1)
                day_change(birthday_arr, bd, user)
            else:
                bd = bd.replace(year=current_date.year)

            if bd.month >= current_date.month:
                if bd.day <= current_date.day and bd.month == current_date.month:
                    if bd.day == current_date.day:
                        day_change(birthday_arr, bd, user)
                    else:
                        continue
                else:
                    day_change(birthday_arr, bd, user)

    res = combine_list(birthday_arr)
    return res


if __name__ == "__main__":
    users = [
        # {"name": "Jan Koum", "birthday": date(2024, 6, 30)},
        # {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        # {"name": "Bill", "birthday": date(1990, 10, 30)},
        # {"name": "Marry", "birthday": date(2000, 12, 30)},
        # {"name": "Jinny", "birthday": date(2000, 12, 31)},
        # {"name": "Jan Koum", "birthday": datetime(1976, 11, 1).date()},
        # {"name": "Jan Koum", "birthday": datetime(1976, 10, 1).date()},
        # {"name": "Jan Koum", "birthday": datetime(1976, 2, 28).date()},
        #
        # {'name': 'John', 'birthday': datetime(2023, 12, 27).date()},
        # {'name': 'Doe', 'birthday': datetime(2023, 12, 29).date()},
        # {'name': 'Alice', 'birthday': datetime(2023, 12, 23).date()},
        #
        # {'name': 'John', 'birthday': datetime(2023, 12, 21).date()},
        # {'name': 'Doe', 'birthday': datetime(2023, 12, 20).date()},
        # {'name': 'Alice', 'birthday': datetime(2021, 1, 1).date()},
        #
        {"name": "John", "birthday": datetime(2023, 12, 31).date()},
        {"name": "Doe", "birthday": datetime(2024, 1, 1).date()},
        {"name": "Alice", "birthday": datetime(2023, 12, 29).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)

    for day_name, names in result.items():
        print(day_name, ":", names)
