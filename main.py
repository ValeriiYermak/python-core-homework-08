from datetime import datetime, timedelta, date


def get_birthdays_per_week(users):
    now = date.today()
    end_date = now + timedelta(days=6)
    weekdays ={"Monday":[],
               "Tuesday":[],
               "Wednesday":[],
               "Thursday":[],
               "Friday":[],
               }
    if not users :
        return {}
    
    for user in users:
        if end_date.year > now.year and user['birthday'].month == 1:
            user_birthday = datetime(year=end_date.year, month=user['birthday'].month,
                                 day=user['birthday'].day).date()
        else:
             user_birthday = datetime(year=now.year, month=user['birthday'].month,
                                 day=user['birthday'].day).date()
       
        if now <= user_birthday <= end_date:
            
            if user_birthday.strftime('%A') in weekdays:
                weekdays[user_birthday.strftime('%A')].append(user['name'])
            else:
                weekdays["Monday"].append(user['name'])
    delete_key = [key for key,value in weekdays.items() if not value]
    for key in delete_key:
            del weekdays[key]
    print(weekdays)
    return weekdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": date(2023, 11, 1)}, # Wednesday
        {"name": "Luccy", "birthday": date(2023, 11, 14)},   # Tuesday
    ]
    result = get_birthdays_per_week(users)
   
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")